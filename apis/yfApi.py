import yfinance as yf
from datetime import datetime
import pandas as pd
import json

start_index = 4
end_index = 7


def get_LastPrice(stock): #Dataframe
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


async def get_api_answer(userinput, botanswer):
    userinput = userinput[start_index:end_index].upper()

    if "price" in botanswer:
        try:
            apidata = get_LastPrice(userinput)
        except:
            return "No data could be found"

        botanswer = botanswer + " " + str(apidata)
        return botanswer

    elif "website" in botanswer:
        try:
            apidata = get_website(userinput)
        except:
            return "No data could be found"

        botanswer = botanswer + " " + str(apidata)
        return botanswer

    elif "close" in botanswer:
        try:
            apidata = get_previousClose(userinput)
        except:
            return "No data could be found"

        botanswer = botanswer + " " + str(apidata)
        return botanswer

    elif "market open" in botanswer:
        try:
            apidata = get_regularMarketOpen(userinput)
        except:
            return "No data could be found"

        botanswer = botanswer + " " + str(apidata)
        return botanswer

    elif "200 avaerage" in botanswer:
        try:
            apidata = get_twoHundredDayAverage(userinput)
        except:
            return "No data could be found"

        botanswer = botanswer + " " + str(apidata)
        return botanswer

    elif "volume" in botanswer:
        try:
            apidata = get_volume24Hr(userinput)
        except:
            return "No data could be found"

        botanswer = botanswer + " " + str(apidata)
        return botanswer

    elif "regular high" in botanswer:
        try:
            apidata = get_regularMarketDayHigh(userinput)
        except:
            return "No data could be found"

        botanswer = botanswer + " " + str(apidata)
        return botanswer

    elif "regular low" in botanswer:
        try:
            apidata = get_regularMarketDayLow(userinput)
        except:
            return "No data could be found"

        botanswer = botanswer + " " + str(apidata)
        return botanswer

    elif "currency" in botanswer:
        try:
            apidata = get_currency(userinput)
        except:
            return "No data could be found"

        botanswer = botanswer + " " + str(apidata)
        return botanswer

    elif "market volume" in botanswer:
        try:
            apidata = get_regularMarketVolume(userinput)
        except:
            return "No data could be found"

        botanswer = botanswer + " " + str(apidata)
        return botanswer

    elif "year high" in botanswer:
        try:
            apidata = get_fiftyTwoWeekHigh(userinput)
        except:
            return "No data could be found"

        botanswer = botanswer + " " + str(apidata)
        return botanswer

    elif "year low" in botanswer:
        try:
            apidata = get_fiftyTwoWeekLow(userinput)
        except:
            return "No data could be found"

        botanswer = botanswer + " " + str(apidata)
        return botanswer

    elif "market cap" in botanswer:
        try:
            apidata = get_marketCap(userinput)
        except:
            return "No data could be found"

        botanswer = botanswer + " " + str(apidata)
        return botanswer

    elif "dividend" in botanswer:
        try:
            apidata = get_dividendYield(userinput)
        except:
            return "No data could be found"

        botanswer = botanswer + " " + str(apidata)
        return botanswer

    elif "market" in botanswer:
        try:
            apidata = get_market(userinput)
        except:
            return "No data could be found"

        botanswer = botanswer + " " + str(apidata)
        return botanswer

    elif "trailing pe" in botanswer:
        try:
            apidata = get_trailingPE(userinput)
        except:
            return "No data could be found"

        botanswer = botanswer + " " + str(apidata)
        return botanswer

    else:
        return botanswer
