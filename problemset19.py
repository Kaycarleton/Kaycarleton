import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib as mtl

end_date=pd.Timestamp.today()
start_date=end_date-pd.Timedelta(days=365)

st.sidebar.title("Stock Price")
symbol=st.sidebar.text_input("Please enter stock symbol", value="GOOG")

start_date=st.sidebar.date_input("Start Date:", value=start_date)
end_date=st.sidebar.date_input("End date", value=end_date)

ticks=yf.ticker(symbol)
data=ticks.history(start=start_date, end=end_date, interval='1d')

mtl.plot(data)