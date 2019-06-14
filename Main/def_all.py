from datetime import datetime
from urllib import request
import json
from bs4 import BeautifulSoup
import requests


def Time():
    x = datetime.strftime(datetime.now(), "%d.%m.%Y") # чвс, минуты и секунды - %H:%M:%S
    return x


def Nac_Bank(coin):
  '''input only 'USD' or 'EUR' or 'RUB' /'''
  try:
    murl = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
    json_response = request.urlopen(murl).read()
    response = json.loads(json_response)
    for i in response:
      for i in response:
        if i['cc'] == coin:
          x = i['rate']
          return x
  except:
    return 'Помилка :('



def PB_nal(coin, buy_sale):
     '''первый аргумент - input only 'USD' or 'EUR' or 'RUR'
        второй - 'buy' or 'sale'
     '''
     murl = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
     json_response = request.urlopen(murl).read()
     response = json.loads(json_response)
     for i in response:
         for i in response:
             if i['ccy'] == coin:
                 x = i[buy_sale]
                 return x


def PB_beznal(coin, buy_sale):
     '''первый аргумент - input only 'USD' or 'EUR' or 'RUR'
        второй - 'buy' or 'sale'
     '''
     murl = 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'
     json_response = request.urlopen(murl).read()
     response = json.loads(json_response)
     for i in response:
         for i in response:
             if i['ccy'] == coin:
                 x = i[buy_sale]
                 return x


def sib():
    '''
    возвращает словарь, ключ - валюта 'USD', 'EUR', 'RUB', 'GBP'фунт стерлингов, 'CHF'швейцарский франк
    values список из двух цифр 1 - покупка, 2 - продажа. Пример - {'USD':[27.400, 27.800]}
    '''
    url = 'https://my.ukrsibbank.com/ru/personal/operations/currency_exchange/'
    r = requests.get(url)
    html = r.text

    soup = BeautifulSoup(html, 'lxml')
    data = soup.find('div', class_="currency__wrapper").find('tbody').find_all('tr')
    all_coin = dict()
    for i in data:
        all = i.text.strip()
        all = all.split('\n')
        key = all[0][0:3]
        buy = float(all[1][7:-1])
        sale = float(all[2][7:-1])
        all_coin[key] = [buy, sale]
    return all_coin


def aval():
    '''
    возвращает словарь, ключ - валюта 'USD', 'EUR', 'RUB'
    values список из двух цифр 1 - покупка, 2 - продажа. Пример - {'USD':[27.400, 27.800]}
    '''
    url = 'https://www.aval.ua/'
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, 'lxml')
    data = soup.find_all('div', class_="rate-numbers")
    coin = ['USD', 'EUR', 'RUB']
    all_coin = dict()
    t = 0
    for i in data:
        x = i.text.split('\n')
        buy = x[2].replace(' ', '')
        sale = x[5].replace(' ', '')
        all_coin[coin[t]] = [buy, sale]
        t+=1

    return all_coin


def crypto():
  '''
    return only coin (dict) in var - coin
  '''
  murl = 'https://api.binance.com//api/v3/ticker/price'
  json_response = request.urlopen(murl).read()
  response = json.loads(json_response)

  coin = ['BTCUSDT', 'XRPUSDT', 'ETHUSDT', 'BCHABCUSDT', 'EOSUSDT', 'XLMUSDT', 'LTCUSDT', 'BCHSVUSDT', 'TRXUSDT', 'IOTAUSDT']
  my_coin = []

  for i in coin:
    for x in response:
      if x['symbol'] == i:
        my_coin.append(x)

  return my_coin
