#For this one I will be watching over the Tesla stock price
import smtplib
import requests
import time
from email.message import EmailMessage
from newsapi import NewsApiClient


STOCK_API = "YOUR STOCK API KEY"
NEWS_API = "YOUR NEWS API KEY"
STOCK = "TSLA"
COMPANY_NAME = "Tesla"
month_prev_is_31days = [1, 2, 4, 6, 8, 9, 11]
newsapi = NewsApiClient(api_key=NEWS_API)
myemail = "rizkymaulanahadi27@gmail.com"
password = "YOUR GOOGLE API PASSWORD"


def leap_year_check(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
def date_formatting(date, current_times):
    global month_prev_is_31days
    leap_year = leap_year_check(current_times[0])
    if date <= 0:
        if current_times[1] in month_prev_is_31days:
            if current_times[1] == 1:
                return [str(current_times[0]-1), '12', str(date + 31)]
            else:
                return [str(current_times[0]), str(current_times[1]-1), str(date + 31)]
        elif current_times[1] == 3:
            if leap_year:
                return [str(current_times[0]), str(current_times[1]-1), str(date + 29)]
            else:
                return [str(current_times[0]), str(current_times[1]-1), str(date + 28)]
        else:
            return [str(current_times[0]), str(current_times[1]-1), str(date + 30)]
    else:
        return [str(current_times[0]), str(current_times[1]), str(date)]
    
def fetch_price(time, data):
    fetching_first_price = True
    fetching_second_price = True
    subtractor = 1
    date1 = date_formatting(time[2] - subtractor, time)
    price = []
    while fetching_first_price:
        try:
            time1 = f'{date1[0]}-{date1[1].zfill(2)}-{date1[2].zfill(2)}'
            price.append(float(data['Time Series (Daily)'][time1]['4. close']))
            fetching_first_price = False
        except KeyError:
            subtractor += 1
            date1 = date_formatting(time[2] - subtractor, time)
    subtractor += 1
    date2 = date_formatting(time[2] - subtractor, time)
    while fetching_second_price:
        try:
            time1 = f'{date2[0]}-{date2[1].zfill(2)}-{date2[2].zfill(2)}'
            price.append(float(data['Time Series (Daily)'][time1]['4. close']))
            fetching_second_price = False
        except KeyError:
            subtractor += 1
            date2 = date_formatting(time[2] - subtractor, time)
    return price



url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={STOCK}&apikey={STOCK_API}'
r = requests.get(url) 
datas = r.json()

current_time = time.localtime()
price_to_compare_list = fetch_price(current_time, datas)

price_diff_in_percent = ((price_to_compare_list[0] - price_to_compare_list[1])/price_to_compare_list[1]) * 100
if price_diff_in_percent >= 2 or price_diff_in_percent <= -2:
    symbol = "🔺" if price_diff_in_percent > 0 else "🔻"
    top_headlines = newsapi.get_top_headlines(q=COMPANY_NAME,
                                          category='business',
                                          language='en',
                                          country='us')
    try:
        news_title = top_headlines['articles'][0]['title']
        news_description = top_headlines['articles'][0]['description']
    except IndexError:
        news_title = 'No Top Headlines For Now'
        news_description = 'No Top Headlines For Now'
    subject = f"TSLA: {symbol} {round(price_diff_in_percent)}%"
    content = f"Headline: {news_title}\nBrief: {news_description}"
    msg = EmailMessage() #Solution found in stackoverflow, conventional ways of sending email (using sendmail()) would not display subject of utf-8 encoded text. https://stackoverflow.com/questions/5910104/how-to-send-utf-8-e-mail/71901202#71901202
    msg.set_content(content)
    msg['Subject'] = subject
    msg['From'] = myemail
    msg['To'] = myemail
    connector = smtplib.SMTP("smtp.gmail.com") #Create the object specifying our email provider's smtp link(?). Which for google is smtp.gmail.com
    connector.starttls()
    connector.login(user=myemail, password=password)
    connector.send_message(msg)
    connector.close()
    print('done')
    
#Did not use Twilio for SMS. I couldn't verify my phone number after many attempts. Therefore, I use email as an alternative.
#This is extremely redundant!!! I don't need all of those fetch price, leap year check, and stuff to access the stock prices. I mean.... obviously the latest stock price and second latest stock price is in index 0 and 1 from the json data that we received... right? goddammit
#Also, remember to use list comprehension!! It's a neat feature in python, don't forget to use it.
# ACTUALLY, DATETIME MODULE HAS THE ABILITY TO DO CALENDAR ARITHMETIC WITH TIMEDELTA SOO DEVELOPING THAT LEAPYEAR AND STUFF ALGORITHM IS A COMPLETE WASTE OF TIME HAHA, but it was fun so wahtever
