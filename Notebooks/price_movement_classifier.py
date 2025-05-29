import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report

# Load data
df = pd.read_csv("simulated_crypto_data_7days.csv")

# Prepare and sort
df['last_updated'] = pd.to_datetime(df['last_updated'])
df.sort_values(by=['coin_name', 'last_updated'], inplace=True)

# Create next-day price column
df['price_usd_tomorrow'] = df.groupby('coin_name')['price_usd'].shift(-1)

# Define classification rule
def classify_movement(today, tomorrow, threshold=0.005):
    if pd.isna(tomorrow):
        return None
    diff = tomorrow - today
    if diff > threshold:
        return 'Up'
    elif diff < -threshold:
        return 'Down'
    else:
        return 'Same'

# Apply classification
df['price_movement'] = df.apply(lambda row: classify_movement(row['price_usd'], row['price_usd_tomorrow']), axis=1)
df_clean = df.dropna(subset=['price_movement'])

# Define features and labels
features = ['price_usd', 'volume_24h_usd', 'change_pct_24h', 'high_24h_usd', 'low_24h_usd']
X = df_clean[features]
y = df_clean['price_movement']

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)


# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Create results DataFrame
X_test_df = pd.DataFrame(X_test, columns=features)
X_test_df['actual_movement'] = y_test.values
X_test_df['predicted_movement'] = y_pred

# Save results
X_test_df.to_csv("classified_price_movement.csv", index=False)

# Print classification report
report = classification_report(y_test, y_pred)
print(report)
