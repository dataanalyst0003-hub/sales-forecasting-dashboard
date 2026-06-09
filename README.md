# 📈 Sales Forecasting Dashboard using Prophet

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Prophet](https://img.shields.io/badge/Forecasting-Prophet-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 🔍 Project Overview

Businesses rely on accurate sales forecasts to make informed decisions regarding inventory management, budgeting, workforce planning, and revenue growth.

This project leverages **Facebook Prophet**, a powerful time-series forecasting model, to predict future sales trends based on historical sales data. The results are presented through an interactive **Streamlit Dashboard** that provides actionable business insights.

---

## 🎯 Business Problem

Organizations need reliable forecasts to answer questions such as:

* What will future sales look like?
* How much inventory should be stocked?
* Are there seasonal sales patterns?
* What is the expected revenue in the coming weeks?

This project addresses these challenges by building an end-to-end forecasting pipeline.

---

## 🚀 Solution

The solution consists of:

### Data Processing

* Data cleaning and preprocessing
* Date formatting and validation
* Daily sales aggregation
* Missing value handling

### Forecasting Model

* Prophet Time Series Forecasting
* Trend detection
* Seasonality analysis
* Future sales prediction

### Interactive Dashboard

* KPI Metrics
* Forecast Trend Visualization
* Forecast Data Explorer
* CSV Download Functionality

---

## 🛠️ Tech Stack

| Category        | Tools         |
| --------------- | ------------- |
| Programming     | Python        |
| Data Analysis   | Pandas, NumPy |
| Visualization   | Plotly        |
| Forecasting     | Prophet       |
| Dashboard       | Streamlit     |
| Model Storage   | Joblib        |
| Version Control | Git & GitHub  |

---

## 📂 Project Structure

```text
sales_forecasting_project/
│
├── app/
│   └── app.py
│
├── data/
│
├── models/
│   └── sales_forecast.pkl
│
├── notebooks/
│   └── forecasting.ipynb
│
├── outputs/
│   └── forecast.csv
│
├── requirements.txt
│
└── README.md
```

---

## 📊 Dashboard Features

### 📌 KPI Metrics

The dashboard highlights key forecasting indicators:

* Average Forecast Sales
* Maximum Forecast Sales
* Next 30 Days Forecast

---

### 📈 Forecast Trend Analysis

Interactive Plotly visualization showing:

* Historical forecast trends
* Future sales projections
* Business growth patterns

---

### 📋 Forecast Data Table

Displays:

* Forecast Date
* Predicted Sales
* Lower Confidence Interval
* Upper Confidence Interval

---

### 📥 Export Forecast Results

Users can download the complete forecast dataset as a CSV file directly from the dashboard.

---

## 🤖 Forecasting Model

### Prophet

Prophet is an open-source forecasting library developed by Meta.

Key Advantages:

✅ Handles seasonality automatically

✅ Robust to missing data

✅ Works well with business time-series data

✅ Generates prediction intervals

✅ Easy to interpret

---

## 📈 Sample Insights

| Metric                 | Value  |
| ---------------------- | ------ |
| Average Forecast Sales | 1,830  |
| Maximum Forecast Sales | 3,903  |
| Next 30 Days Forecast  | 97,449 |

---

## ▶️ Installation

### Clone Repository

```bash
git clone https://github.com/dataanalyst0003-hub/sales-forecasting-dashboard.git
```

### Navigate to Project

```bash
cd sales-forecasting-dashboard
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Launch Dashboard

```bash
streamlit run app/app.py
```

---

## 📌 Future Enhancements

* Model Performance Metrics (MAE, RMSE)
* Multiple Forecast Horizons
* Interactive Date Filters
* Streamlit Cloud Deployment
* Automated Retraining Pipeline
* Real-Time Data Integration

---

## 💡 Key Learnings

Through this project, I gained hands-on experience in:

* Time Series Forecasting
* Data Cleaning & Transformation
* Prophet Modeling
* Interactive Dashboard Development
* Git & GitHub Version Control
* End-to-End Data Science Workflow

---

## 👨‍💻 Author

### Asif Ali

Aspiring Data Analyst

Skills:

* Python
* SQL
* Power BI
* Machine Learning
* Data Visualization


