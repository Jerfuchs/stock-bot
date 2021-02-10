import yfinance as yf
from datetime import datetime
import pandas as pd

def getLastPrice(stock): #works/tested
    date_format = "%Y-%m-%d"
    today = datetime.today().strftime(date_format)
    start = datetime.date(pd.Timestamp(datetime.today())).strftime(date_format)
    df = yf.download(stock, start=start, end=today, progress=False)
    answer = str(df["Close"].tolist()[-1])
    answer = float(answer)
    answer = round(answer, 2)
    answer = str(answer) + '$'
    return answer

def getInfo(stock): #dict
    data = yf.Ticker(stock)
    answer = data.info()
    return answer

def getDividends(stock): #series
    data = yf.Ticker(stock)
    answer = data.dividends
    answer = float(answer)
    answer = round(answer, 2)
    answer = str(answer) + '$'
    return answer

def getmajor_holders(stock): #Dataframe
    data = yf.Ticker(stock)
    answer = data.major_holders()
    return answer

def getbalance_sheet(stock): #Dataframe
    data = yf.Ticker(stock)
    answer = data.balance_sheet()
    answer = float(answer)
    answer = round(answer, 2)
    answer = str(answer) + '$'
    return answer

