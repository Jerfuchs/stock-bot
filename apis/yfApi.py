import yfinance as yf
from datetime import datetime
import pandas as pd
import json


def get_LastPrice(stock): #Dataframe
    date_format = "%Y-%m-%d"
    today = datetime.today().strftime(date_format)
    start = datetime.date(pd.Timestamp(datetime.today())).strftime(date_format)
    df = yf.download(stock, start=start, end=today, progress=False)
    answer = str(df["Close"].tolist()[-1])
    answer = float(answer)
    answer = round(answer, 2)
    answer = str(answer)
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


def get_api_answer(userinput, botanswer):
    #temp = userinput.split(" ")
    #print(temp)
    ticker = userinput.split(" ")[1].upper()

    if "price" in userinput:
        try:
            apidata = get_LastPrice(ticker)
        except:
            return "No data could be found"

        botanswer ="It is: " + str(apidata) + " $"
        return botanswer

    elif "website" in userinput:
        try:
            apidata = get_website(ticker)
        except:
            return "No data could be found"

        botanswer = "It is: " + str(apidata)
        return botanswer

    elif "close" in userinput:
        try:
            apidata = get_previousClose(ticker)
        except:
            return "No data could be found"

        botanswer = "It is: " + str(apidata) + " $"
        return botanswer

    elif "market open" in userinput:
        try:
            apidata = get_regularMarketOpen(ticker)
        except:
            return "No data could be found"

        botanswer = "It is: " + str(apidata) + " $"
        return botanswer

    elif "200 avaerage" in userinput:
        try:
            apidata = get_twoHundredDayAverage(ticker)
        except:
            return "No data could be found"

        botanswer = "It is: " + str(apidata) + " $"
        return botanswer

    elif "volume" in userinput:
        try:
            apidata = get_volume24Hr(ticker)
        except:
            return "No data could be found"

        botanswer = "It is: " + str(apidata)
        return botanswer

    elif "regular high" in userinput:
        try:
            apidata = get_regularMarketDayHigh(ticker)
        except:
            return "No data could be found"

        botanswer = "It is: " + str(apidata) + " $"
        return botanswer

    elif "regular low" in userinput:
        try:
            apidata = get_regularMarketDayLow(ticker)
        except:
            return "No data could be found"

        botanswer = "It is: " + str(apidata) + " $"
        return botanswer

    elif "currency" in userinput:
        try:
            apidata = get_currency(ticker)
        except:
            return "No data could be found"

        botanswer = "It is: " + str(apidata)
        return botanswer

    elif "market volume" in userinput:
        try:
            apidata = get_regularMarketVolume(ticker)
        except:
            return "No data could be found"

        botanswer = "It is: " + str(apidata)
        return botanswer

    elif "year high" in userinput:
        try:
            apidata = get_fiftyTwoWeekHigh(ticker)
        except:
            return "No data could be found"

        botanswer = "It is: " + str(apidata) + " $"
        return botanswer

    elif "year low" in userinput:
        try:
            apidata = get_fiftyTwoWeekLow(ticker)
        except:
            return "No data could be found"

        botanswer = "It is: " + str(apidata) + " $"
        return botanswer

    elif "market cap" in userinput:
        try:
            apidata = get_marketCap(ticker)
        except:
            return "No data could be found"

        botanswer = "It is: " + str(apidata)
        return botanswer

    elif "dividend" in userinput:
        try:
            apidata = get_dividendYield(ticker)
        except:
            return "No data could be found"

        botanswer = "It is: " + str(apidata)
        return botanswer

    elif "market" in userinput:
        try:
            apidata = get_market(ticker)
        except:
            return "No data could be found"

        botanswer = "It is: " + str(apidata)
        return botanswer

    elif "trailing pe" in userinput:
        try:
            apidata = get_trailingPE(ticker)
        except:
            return "No data could be found"

        botanswer = "It is: " + str(apidata)
        return botanswer

    else:
        return botanswer
