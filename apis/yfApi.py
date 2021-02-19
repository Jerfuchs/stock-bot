import yfinance as yf
from datetime import datetime
import pandas as pd
import json

def get_LastPrice(stock): #works/tested
    date_format = "%Y-%m-%d"
    today = datetime.today().strftime(date_format)
    start = datetime.date(pd.Timestamp(datetime.today())).strftime(date_format)
    df = yf.download(stock, start=start, end=today, progress=False)
    answer = str(df["Close"].tolist()[-1])
    answer = float(answer)
    answer = round(answer, 2)
    answer = str(answer) + '$'
    return answer

def get_website(stock): #Dataframe
    data = yf.Ticker(stock)
    answer = data.info
    answer = json.dumps(answer)
    answer = json.loads(answer)
    return answer["website"]

def get_previousClose(stock): #Dataframe
    data = yf.Ticker(stock)
    answer = data.info
    answer = json.dumps(answer)
    answer = json.loads(answer)
    return answer["previousClose"]

def get_regularMarketOpen(stock): #Dataframe
    data = yf.Ticker(stock)
    answer = data.info
    answer = json.dumps(answer)
    answer = json.loads(answer)
    return answer["regularMarketOpen"]

def get_twoHundredDayAverage(stock): #Dataframe
    data = yf.Ticker(stock)
    answer = data.info
    answer = json.dumps(answer)
    answer = json.loads(answer)
    return answer["twoHundredDayAverage"]

def get_volume24Hr(stock): #Dataframe
    data = yf.Ticker(stock)
    answer = data.info
    answer = json.dumps(answer)
    answer = json.loads(answer)
    return answer["volume24Hr"]

def get_regularMarketDayHigh(stock): #Dataframe
    data = yf.Ticker(stock)
    answer = data.info
    answer = json.dumps(answer)
    answer = json.loads(answer)
    return answer["regularMarketDayHigh"]

def get_regularMarketDayLow(stock): #Dataframe
    data = yf.Ticker(stock)
    answer = data.info
    answer = json.dumps(answer)
    answer = json.loads(answer)
    return answer["regularMarketDayLow"]

def get_currency(stock): #Dataframe
    data = yf.Ticker(stock)
    answer = data.info
    answer = json.dumps(answer)
    answer = json.loads(answer)
    return answer["currency"]

def get_regularMarketVolume(stock): #Dataframe
    data = yf.Ticker(stock)
    answer = data.info
    answer = json.dumps(answer)
    answer = json.loads(answer)
    return answer["regularMarketVolume"]

def get_fiftyTwoWeekHigh(stock): #Dataframe
    data = yf.Ticker(stock)
    answer = data.info
    answer = json.dumps(answer)
    answer = json.loads(answer)
    return answer["fiftyTwoWeekHigh"]

def get_fiftyTwoWeekLow(stock): #Dataframe
    data = yf.Ticker(stock)
    answer = data.info
    answer = json.dumps(answer)
    answer = json.loads(answer)
    return answer["fiftyTwoWeekLow"]

def get_market(stock): #Dataframe
    data = yf.Ticker(stock)
    answer = data.info
    answer = json.dumps(answer)
    answer = json.loads(answer)
    return answer["market"]

def get_dividendYield(stock): #Dataframe
    data = yf.Ticker(stock)
    answer = data.info
    answer = json.dumps(answer)
    answer = json.loads(answer)
    return answer["dividendYield"]

def get_marketCap(stock): #Dataframe
    data = yf.Ticker(stock)
    answer = data.info
    answer = json.dumps(answer)
    answer = json.loads(answer)
    return answer["marketCap"]

def get_trailingPE(stock): #Dataframe
    data = yf.Ticker(stock)
    answer = data.info
    answer = json.dumps(answer)
    answer = json.loads(answer)
    return answer["trailingPE"]
