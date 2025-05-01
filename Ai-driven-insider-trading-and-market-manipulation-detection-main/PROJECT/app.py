import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from sklearn.ensemble import RandomForestClassifier
from joblib import load
import time

# Load the trained model (previously saved)
model = load('random_forest_model.joblib')

# Function to fetch real-time data for a symbol
def fetch_real_time_data(symbol, period='1d', interval='1m'):
    data = yf.download(symbol, period=period, interval=interval)
    return data

# Preprocess the fetched data
def preprocess_data(data):
    # Feature engineering
    data['price_change'] = data['Close'].pct_change()
    data['volume_change'] = data['Volume'].pct_change()
    # Drop rows with NaN values
    data.dropna(inplace=True)
    # Select features
    X = data[['price_change', 'volume_change']]
    return X

# Function to plot candlestick chart
def plot_candlestick(data, symbol):
    fig = go.Figure(data=[go.Candlestick(x=data.index,
                    open=data['Open'],
                    high=data['High'],
                    low=data['Low'],
                    close=data['Close'],
                    name=symbol)])

    fig.update_layout(title=f'{symbol} Real-Time Candlestick Chart',
                      yaxis_title='Price (USD)',
                      xaxis_title='Timestamp',
                      xaxis_rangeslider_visible=False)
    
    return fig

# Streamlit UI
st.title('Real-Time Stock, Forex, and Crypto Candle Plot Viewer')

# User input for selecting symbols
symbols = st.multiselect(
    'Select symbols to track (Stocks, Forex, Crypto):',
    options=["AAPL", "GOOGL", "MSFT", "EURUSD=X", "GBPUSD=X", "JPY=X", "BTC-USD", "ETH-USD"],
    default=["AAPL", "BTC-USD"]
)

refresh_rate = st.slider("Refresh rate (seconds)", 10, 300, 60)

# Start real-time tracking loop
if st.button("Start Tracking"):
    while True:
        for symbol in symbols:
            st.subheader(f"Processing symbol: {symbol}")
            
            # Fetch real-time data
            data = fetch_real_time_data(symbol)
            
            if not data.empty:
                # Display the candle chart
                fig = plot_candlestick(data, symbol)
                st.plotly_chart(fig)

                # Preprocess data for model prediction
                X = preprocess_data(data)
                X = X.astype('float64')
                
                if not X.empty:
                    # Make prediction
                    prediction = model.predict(X.tail(1))  # Predict based on the latest available data
                    prediction_label = "Positive" if prediction[0] else "Negative"
                    st.write(f"Real-time prediction for {symbol}: {prediction_label}")
            
            st.write("-" * 50)
        
        # Wait for the specified refresh time before fetching new data
        time.sleep(refresh_rate)
        st.experimental_rerun()
