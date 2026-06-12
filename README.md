# 📊 NIFTY-50 AI-Powered Investment Intelligence Platform

An institutional-grade, risk-adjusted quantitative decision support system that fuses predictive Machine Learning with classical Modern Portfolio Theory (MPT) and advanced statistical anomaly tracking. This platform converts multi-asset raw market noise into structured, transparent, and actionable wealth management strategies.

---

# Platform Core Architecture

The system operates as a unified, risk-first **Decision Support Framework** designed to prevent catastrophic asset drawdowns while capturing market alpha across four intelligent backend components.

## Predictive Core

Deploys a dual-engine LightGBM (Gradient Boosted Tree) architecture:

* **Model Alpha** handles binary trend direction classification.
* **Model Beta** performs continuous time-series regression to estimate exact 5-day forward percentage returns.

## Risk Assessment Module

Evaluates ten years of historical data to compute:

* Annualized Volatility
* Sharpe Ratio
* Sortino Ratio (downside-risk adjusted)
* Maximum Drawdown

Assets are normalized into a standardized **Risk Score (0–100)** profile.

## Portfolio Construction Module

Uses Markowitz Efficient Frontier optimization through **PyPortfolioOpt** to dynamically construct:

* Conservative Portfolios
* Balanced Portfolios
* Aggressive Portfolios

based on investor risk appetite.

## Market Anomaly Detection Engine

Applies a rolling 50-day statistical Z-score framework across:

* Trading Volume
* True Range Expansion

to identify abnormal market conditions and potential regime shifts.

---

# 🛠️ Local Environment Setup

## 📋 Prerequisites

Ensure the following are installed:

* Python 3.9 – 3.11
* pip package manager

---

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

---

## 2️⃣ Create a Virtual Environment (Recommended)

### Windows

```bash
python -m venv venv
.\venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Verify Project Structure

```text
nifty50-investment-intelligence/
│
├── app.py
├── requirements.txt
├── README.md
│
├── pages/
│   ├── 1_Stock_Explorer.py
│   ├── 2_Predictor.py
│   ├── 3_Risk_Analyzer.py
│   ├── 4_Portfolio_Builder.py
│   └── 5_Investment_Insights.py
│
├── notebooks/
│   └── pipeline_engine.ipynb
│
├── data/
│   ├── processed_base.csv
│   ├── feature_dataset.csv
│   ├── risk_metrics.csv
│   ├── conservative_portfolio.csv
│   ├── balanced_portfolio.csv
│   ├── aggressive_portfolio.csv
│   └── investment_recommendations.csv
│
└── models/
    ├── lgb_classifier.pkl
    └── lgb_regressor.pkl
```

---

# 🚀 Running the Application

Launch the Streamlit dashboard:

```bash
streamlit run app.py
```

The application will automatically open in your browser at:

```text
http://localhost:8501
```

---

# 🔄 Reproducing Pipeline Results

The platform is fully reproducible through the notebook located at:

```text
/notebooks/pipeline_engine.ipynb
```

To rebuild all datasets and model artifacts:

1. Open `pipeline_engine.ipynb`
2. Run all cells sequentially
3. Wait for pipeline completion

---

## 📋 Pipeline Execution Stages

### Data Engineering

**Cells 1–7**

* Load raw market datasets
* Handle missing values
* Generate technical indicators:

  * SMA
  * EMA
  * RSI
  * MACD
  * Bollinger Bands

### Train/Test Segmentation

**Cells 8–10**

Chronological split:

```text
Training Data ≤ 2018-12-31
Testing Data  ≥ 2019-01-01
```

This prevents look-ahead bias and data leakage.

### Risk Analytics

**Cells 11–12**

* Annualized Volatility
* Sharpe Ratio
* Sortino Ratio
* Maximum Drawdown
* Risk Category Assignment

### Portfolio Optimization

**Cells 13–15**

* Efficient Frontier Construction
* Quadratic Optimization
* Capital Allocation Normalization

### Advanced Analytics

**Cells 16–21**

* 50-Day Rolling Z-Score Anomaly Detection
* LightGBM Classification
* LightGBM Regression
* Out-of-Sample Evaluation
* Investment Recommendation Generation

Upon completion, the pipeline automatically updates:

```text
/data/*.csv
/models/*.pkl
```

with fresh outputs.

---

# 🧰 Technology Stack

## Machine Learning

* LightGBM
* Scikit-learn

## Portfolio Optimization

* PyPortfolioOpt

## Data Processing

* Pandas
* NumPy

## Visualization

* Plotly
* Matplotlib

## Web Application

* Streamlit

## Development Environment

* Jupyter Notebook

---
