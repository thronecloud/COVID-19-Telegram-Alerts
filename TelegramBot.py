# -*- coding: UTF8 -*-
import requests
import datetime
import requests 

def dateAdjuster(date):
    date_time_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
    date = date_time_obj.strftime("%d %B")
    return date 

def fetchCity(city,state="Uttar Pradesh"):
    try:
        print(state)
        doc = requests.get('https://api.covid19india.org/districts_daily.json')
        city_today = doc.json()["districtsDaily"][state][city][-1]["confirmed"]
        city_yesterday = doc.json()["districtsDaily"][state][city][-2]["confirmed"]
        city_today_date = dateAdjuster(doc.json()["districtsDaily"][state][city][-1]["date"])
        city_yesterday_date = dateAdjuster(doc.json()["districtsDaily"][state][city][-2]["date"])
        city_status = city + "    " + str(city_today_date) + "   "   + str(city_today) + "   "   + str(city_yesterday_date)   + "   "   + str(city_yesterday)
        return city_status
    except requests.exceptions.RequestException as e:  
        raise SystemExit(e)


def fetchIndia():
    try:
        doc = requests.get('https://api.covid19india.org/data.json')
        india_today_date = doc.json()["cases_time_series"][-1]["date"]
        india_today_confirmed = doc.json()["cases_time_series"][-1]["dailyconfirmed"]
        india_today_total =doc.json()["cases_time_series"][-1]["totalconfirmed"] 
        india_status = ("India    " + str (india_today_date) + " New Cases " +  str(india_today_confirmed)  + " Total : " +  str(india_today_total) )
        return india_status
    except requests.exceptions.RequestException as e:  
        raise SystemExit(e)

def messageStitch():
    message = fetchCity("Ghaziabad") + "\n" +  fetchCity("Lucknow") + "\n" +fetchIndia()
    return message


class BotHandler:
    def __init__(self, token):
            self.token = token
            self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

token = '1164987049:AAFzZ51FDWL6lLvGeJCI-OkxwaIUnPFttPU' 
magnito_bot = BotHandler(token) 


def main():
    magnito_bot.send_message('@coronaghaziabad',messageStitch())

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()