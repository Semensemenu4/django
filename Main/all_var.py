from .def_all import *
from .forms import *



# Date !! --------------------------------------------------------------------
data = Time()

#Nac_Bank !! ------------------------------------------------------------------
USD_nac = Nac_Bank('USD')
if USD_nac == 'Помилка :(' or 'Оновлення':
    USD_nac = float(PB_nal('USD', 'buy'))
EUR_nac = Nac_Bank('EUR')
if EUR_nac == None:
    EUR_nac = "Оновлення"
RUB_nac = Nac_Bank('RUB')
if RUB_nac == None:
    RUB_nac = "Оновлення"

XAU_nac = Nac_Bank('XAU') # Gold
if XAU_nac != 'Помилка :(':
    XAU_nac *= 10 # 311 gramm
    XAU_nac_1 = XAU_nac / 311.03 # 1 gramm
    XAU_nac_1 = round(XAU_nac_1, 3)
else:
    XAU_nac = "Оновлення"
    XAU_nac_1 = "Оновлення"

XAG_nac = Nac_Bank('XAG') # Silver
if XAG_nac != 'Помилка :(':
    XAG_nac *= 10 # 311 gramm
    XAG_nac_1 = XAG_nac / 311.03 # 1 gramm
    XAG_nac_1 = round(XAG_nac_1, 3)
else:
    XAG_nac = "Оновлення"
    XAG_nac_1 = "Оновлення"


XPT_nac = Nac_Bank('XPT') # Platinum
if XPT_nac != 'Помилка :(':
    XPT_nac *= 10# 311 gramm
    XPT_nac_1 = XPT_nac / 311.03 # 1 gramm
    XPT_nac_1 = round(XPT_nac_1, 3)
else:
    XPT_nac = "Оновлення"
    XPT_nac_1 = "Оновлення"

# PRIVAT BANK !! --------------------------------------------------------------
USD_pb_buy = PB_nal('USD', 'buy')
EUR_pb_buy = PB_nal('EUR', 'buy')
RUR_pb_buy = PB_nal('RUR', 'buy')

USD_pb_sale = PB_nal('USD', 'sale')
EUR_pb_sale = PB_nal('EUR', 'sale')
RUR_pb_sale = PB_nal('RUR', 'sale')

USD_pbbez_buy = PB_beznal('USD', 'buy')
EUR_pbbez_buy = PB_beznal('EUR', 'buy')
RUR_pbbez_buy = PB_beznal('RUR', 'buy')

USD_pbbez_sale = PB_beznal('USD', 'sale')
EUR_pbbez_sale = PB_beznal('EUR', 'sale')
RUR_pbbez_sale = PB_beznal('RUR', 'sale')

#BANK ukrsibbank !! ------------------------------------------------------------
sib = sib()
USD_sib_buy = sib['USD'][0]
USD_sib_sale = sib['USD'][1]
EUR_sib_buy = sib['EUR'][0]
EUR_sib_sale = sib['EUR'][1]
RUB_sib_buy = sib['RUB'][0]
RUB_sib_sale = sib['RUB'][1]

#BANK AVAL --------------------------------------------------------------------
aval = aval()
USD_aval_buy = aval['USD'][0]
USD_aval_sale = aval['USD'][1]
EUR_aval_buy = aval['EUR'][0]
EUR_aval_sale = aval['EUR'][1]
RUB_aval_buy = aval['RUB'][0]
RUB_aval_sale = aval['RUB'][1]

# CRIPTO !! ------------------------------------------------------------------
my_coin = crypto()
Bitcoin = my_coin[0]['price']
Bitcoin_g = round((float(Bitcoin) * USD_nac),2)
XRP = my_coin[1]['price']
XRP_g = round((float(XRP) * USD_nac),2)
ETHUSDT = my_coin[2]['price']
ETHUSDT_g = round((float(ETHUSDT) * USD_nac),2)
BitcoinCash = my_coin[3]['price']
BitcoinCash_g = round((float(BitcoinCash) * USD_nac),2)
EOSUSDT = my_coin[4]['price']
EOSUSDT_g = round((float(EOSUSDT) * USD_nac),2)
XLMUSDT = my_coin[5]['price']
XLMUSDT_g = round((float(XLMUSDT) * USD_nac),2)
LTCUSDT = my_coin[6]['price']
LTCUSDT_g = round((float(LTCUSDT) * USD_nac),2)
BCHSVUSDT = my_coin[7]['price']
BCHSVUSDT_g = round((float(BCHSVUSDT) * USD_nac),2)
TRXUSDT = my_coin[8]['price']
TRXUSDT_g = round((float(TRXUSDT) * USD_nac),2)
IOTAUSDT = my_coin[9]['price']
IOTAUSDT_g = round((float(IOTAUSDT) * USD_nac),2)
