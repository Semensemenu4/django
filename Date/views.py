from django.shortcuts import render
from .def_date import *



# Create your views here.
def date_page(request):

    date_coin_get = request.GET.get('date_coin', '')
    date_coin = date_coin_get.replace('-', '')
    USD_date = Nac_Bank_date(date_coin)
    if len(date_coin_get) == 0:
        date_coin_get = 'поточну дату'

        print(date)

    return render(request, 'Date/index.html', context = {
        'date_coin_get':date_coin_get, 'USD_date':USD_date, 'date':date

    })
