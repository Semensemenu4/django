from datetime import datetime
from urllib import request
import json


def Nac_Bank_date(date):
    try:
        murl = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date='+date+'&json'
        json_response = request.urlopen(murl).read()
        response = json.loads(json_response)
        for i in response:
            for i in response:
                if i['cc'] == 'USD':
                    x = i['rate']
                    return round(x, 3)
    except:
        return ':('


def Time2():
    x = datetime.strftime(datetime.now(), "%d-%m-%Y") # чвс, минуты и секунды - %H:%M:%S
    return x

date = Time2()
