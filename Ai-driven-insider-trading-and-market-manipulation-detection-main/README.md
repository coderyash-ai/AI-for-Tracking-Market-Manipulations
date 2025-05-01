# 📊 **AI for Tracking Market Manipulations** 🤖

## 📝 **Project Overview**

This project leverages AI and machine learning techniques to track potential market manipulations in real-time using historical stock data and advanced prediction models. It uses a Random Forest Classifier for classification and SMOTE for balancing class distributions.

---

## 🚀 **Features**

- **Historical Data Processing** 🗃️
  - Loads multiple CSV files containing stock market data.
  - Performs feature engineering, such as percentage changes in price and volume, and moving averages.

- **Model Training** 📈
  - Trains a Random Forest Classifier on the processed data to predict significant market events (e.g., large price or volume changes).
  
- **Class Imbalance Handling** ⚖️
  - Uses **SMOTE** (Synthetic Minority Over-sampling Technique) to handle class imbalance during training.

- **Hyperparameter Tuning** 🔧
  - Optimizes the Random Forest model using Grid Search for best performance.

- **Real-Time Prediction** ⏱️
  - Continuously tracks real-time market data for a set of stock symbols.
  - Predicts whether a market event (significant price or volume change) will occur based on the latest data.

---

## 🔧 **Technologies Used**

- **Python** 🐍
- **Pandas** 📚 - Data manipulation
- **Scikit-learn** 🤖 - Machine learning
- **Imbalanced-learn** ⚖️ - SMOTE for handling class imbalance
- **YFinance** 📉 - Fetches historical and real-time stock market data
- **Joblib** 💾 - Saving and loading the trained model
- **Time** ⏳ - Real-time tracking loop

---

## 📂 **How to Use**

### 1️⃣ **Clone the Repository**

If you're starting fresh, clone this repository to your local machine:

```bash
git clone https://github.com/your-repo/market-manipulation-tracker.git
cd market-manipulation-tracker
```

### 2️⃣ **Install Dependencies**

Ensure all required libraries are installed by running:

```bash
pip install -r requirements.txt
```

Or, install them manually:

```bash
pip install pandas scikit-learn imbalanced-learn yfinance joblib
```

### 3️⃣ **Prepare Your Data**

Make sure to place your CSV files with historical stock data in the directory defined in the script. The files should have columns such as `Date`, `Symbol`, `Close`, `Volume`, etc.

### 4️⃣ **Run the Script**

To start processing the data and tracking market manipulations, run:

```bash
python market_tracking.py
```

This will:
- Train the model on historical data.
- Save the trained model to `random_forest_model.joblib`.
- Begin real-time tracking for the specified stock symbols.

### 5️⃣ **Real-Time Market Tracking**

The script will track market data for the following symbols:

- 📱 Apple (`AAPL`)
- 🌐 Alphabet (`GOOGL`)
- 💻 Microsoft (`MSFT`)
- 💵 EUR/USD (`EURUSD=X`)
- 💷 GBP/USD (`GBPUSD=X`)
- 💴 JPY/USD (`JPY=X`)
- 🪙 Bitcoin (`BTC-USD`)
- 🧑‍💻 Ethereum (`ETH-USD`)

---

## 📈 **Model Evaluation**

After training, the model's performance is evaluated with:
- **Accuracy** 🎯
- **Classification Report** 📑 (including Precision, Recall, and F1-Score)

---

## 🌍 **Real-Time Data Processing**

The script fetches real-time market data every hour and makes predictions based on the latest available information. It predicts if there will be significant market movement based on the most recent data for each tracked symbol.

---

## ⚙️ **Customization**

- You can adjust the list of stock symbols in the `symbols` list to track additional symbols or different assets (e.g., commodities, other cryptocurrencies).
- Modify the `param_grid` for hyperparameter tuning to improve model performance or experiment with other classifiers.

---

## 📂 **File Structure**

```
market-manipulation-tracker/
│
├── market_tracking.py           # Main script for training and tracking
├── requirements.txt            # List of required dependencies
└── random_forest_model.joblib  # Saved model after training
```

---

## 👨‍💻 **Contributing**

Contributions are always welcome! Feel free to fork the repository, create an issue, or submit a pull request.

---

Happy tracking! 🚀📈
