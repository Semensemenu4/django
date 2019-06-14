from django.shortcuts import render
from .all_var import *
from .forms import *


def main_page(request):

    return render(request, 'Main/index.html', context = {

        'data':data,

        'USD_nac':USD_nac, 'EUR_nac':EUR_nac, 'RUB_nac':RUB_nac,
        'XAU_nac':XAU_nac, 'XAU_nac_1':XAU_nac_1, 'XAG_nac':XAG_nac, 'XAG_nac_1':XAG_nac_1, 'XPT_nac':XPT_nac, 'XPT_nac_1':XPT_nac_1,

        'USD_pb_buy':USD_pb_buy, 'EUR_pb_buy':EUR_pb_buy, 'RUR_pb_buy':RUR_pb_buy, 'USD_pb_sale':USD_pb_sale, 'EUR_pb_sale':EUR_pb_sale,
        'RUR_pb_sale':RUR_pb_sale,
        'USD_pbbez_buy':USD_pbbez_buy, 'EUR_pbbez_buy':EUR_pbbez_buy, 'RUR_pbbez_buy':RUR_pbbez_buy, 'USD_pbbez_sale':USD_pbbez_sale,
        'EUR_pbbez_sale':EUR_pbbez_sale, 'RUR_pbbez_sale':RUR_pbbez_sale,

        'USD_aval_buy':USD_aval_buy, 'USD_aval_sale':USD_aval_sale, 'EUR_aval_buy':EUR_aval_buy, 'EUR_aval_sale':EUR_aval_sale,
        'RUB_aval_buy':RUB_aval_buy, 'RUB_aval_sale':RUB_aval_sale,

        'USD_sib_buy':USD_sib_buy, 'USD_sib_sale':USD_sib_sale, 'EUR_sib_buy':EUR_sib_buy, 'EUR_sib_sale':EUR_sib_sale,
        'RUB_sib_buy':RUB_sib_buy, 'RUB_sib_sale':RUB_sib_sale,

        'Bitcoin':Bitcoin, 'Bitcoin_g':Bitcoin_g, 'XRP':XRP, "XRP_g":XRP_g, 'ETHUSDT':ETHUSDT, 'ETHUSDT_g':ETHUSDT_g, 'BitcoinCash':BitcoinCash,
        'BitcoinCash_g':BitcoinCash_g, 'EOSUSDT':EOSUSDT, 'EOSUSDT_g':EOSUSDT_g, 'XLMUSDT':XLMUSDT, 'XLMUSDT_g':XLMUSDT_g, 'LTCUSDT':LTCUSDT,
        'LTCUSDT_g':LTCUSDT_g, 'BCHSVUSDT':BCHSVUSDT, 'BCHSVUSDT_g':BCHSVUSDT_g, 'TRXUSDT':TRXUSDT, 'TRXUSDT_g':TRXUSDT_g, 'IOTAUSDT_g':IOTAUSDT_g,
        'IOTAUSDT':IOTAUSDT

    })
