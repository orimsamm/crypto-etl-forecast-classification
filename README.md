# Cryptocurrency Market Analysis and Forecasting using CoinGecko API

## 📌 Overview
This project demonstrates a full end-to-end data pipeline to extract, transform, and load real-time cryptocurrency data from the CoinGecko API. The project also integrates Power BI for visualization and forecasting, along with a Python-based classification model that predicts the direction of price movement (up or down). 

It is designed as a portfolio-ready project showcasing ETL, visualization, and machine learning skills using real-world data.

---

## 🎯 Objectives
- Extract live crypto market data from the CoinGecko API.
- Transform and clean the dataset for analysis.
- Load data into Power BI to visualize trends and generate forecasts.
- Apply Python classification techniques to predict price movement.
- Export and document both visuals and forecast results.

---

## 🛠️ Tools & Technologies
- Python (Pandas, Requests, Scikit-learn, Matplotlib)
- Jupyter Notebook
- CoinGecko API
- Power BI
- Git & GitHub

---

## 🔄 ETL Workflow
### Extract
Fetched real-time cryptocurrency data such as:
- Current price
- Market cap
- 24h volume
- Price change percentages
- Timestamps

### Transform
- Converted timestamps to readable format
- Cleaned missing or null values
- Created additional features (e.g., percent change, rolling averages)

### Load
- Saved the final dataset as a CSV file
- Loaded it into Power BI for analytics

---

## 📊 Power BI Visualizations
- Time-series line chart of crypto price movements
- Built-in forecasting using Power BI’s Analytics pane
- Highlights of predicted trends and key price indicators

---

## 🤖 Price Movement Classification (Python)
- Engineered features like past lag values and moving averages
- Created binary labels: Up (1) / Down (0)
- Trained and evaluated models (e.g., Logistic Regression, Random Forest)
- Output: Prediction accuracy and confusion matrix

---

## 📤 Exported Forecast
- Power BI forecast exported as image (PNG) and PDF
- Forecasts show expected trend direction for major coins like BTC, ETH

---

## 🗂️ Project Structure

