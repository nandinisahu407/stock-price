import streamlit as st
import yfinance as yf
import datetime

st.write(""" 
            # Stock Price Analyser""")

#get data for apple's stock

col1,col2=st.columns(2)

with col1:
    start_date = st.date_input("Please Enter Start Date", datetime.date(2019, 7, 6))

with col2:   
    end_date = st.date_input("Please Enter End Date", datetime.date(2019, 7, 18)) 

# symbol="AAPL"

symbol = st.selectbox(
    'Which stock symbol you want to select?',
    ('AAPL', 'GOOG', 'TSLA','MSFT','NFLX'))

# start_date = st.date_input("Please Enter Start Date", datetime.date(2019, 7, 6))

# end_date = st.date_input("Please Enter End Date", datetime.date(2019, 7, 18))

ticker_data=yf.Ticker(symbol)
ticker_df=ticker_data.history(period="1d", start=start_date, end=end_date)

st.write(f"""
### {symbol}'s Stock price data""")

st.dataframe(ticker_df)

st.write(f"""
### {symbol}'s closing price data""")

st.line_chart(ticker_df["Close"])

st.line_chart(ticker_df["Volume"])

st.write("""
### Made By Nandini 💖""")



