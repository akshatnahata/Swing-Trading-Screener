from datetime import date
import numpy as np
import pandas as pd
import pandas_datareader as pdr

def get_sma(prices, rate):
    return prices.rolling(rate).mean()

def get_bollinger_bands(prices, rate=20):
    sma = get_sma(prices, rate)
    std = prices.rolling(rate).std()
    bollinger_up = sma + std * 1.5 # Calculate top band
    bollinger_down = sma - std * 1.5 # Calculate bottom band
    return bollinger_up, bollinger_down

from nsepy import get_history
import talib

stocks = ['3MINDIA',
'ABB',
'ACC',
'AIAENG',
'APLAPOLLO',
'AUBANK',
'AARTIDRUGS',
'AAVAS',
'ABBOTINDIA',
'ADANIENT',
'ADANIGREEN',
'ADANIPORTS',
'ATGL',
'ADANITRANS',
'ABCAPITAL',
'ABFRL',
'ABSLAMC',
'ADVENZYMES',
'AEGISCHEM',
'AFFLE',
'AJANTPHARM',
'APLLTD',
'ALKEM',
'ALKYLAMINE',
'ALLCARGO',
'AMARAJABAT',
'AMBER',
'AMBUJACEM',
'ANGELONE',
'ANURAS',
'APOLLOHOSP',
'APOLLOTYRE',
'APTUS',
'ASAHIINDIA',
'ASHOKLEY',
'ASIANPAINT',
'ASTERDM',
'ASTRAZEN',
'ASTRAL',
'ATUL',
'AUROPHARMA',
'AVANTIFEED',
'DMART',
'AXISBANK',
'BASF',
'BSE',
'BAJAJ-AUTO',
'BAJAJELEC',
'BAJFINANCE',
'BAJAJFINSV',
'BAJAJHLDNG',
'BALAMINES',
'BALKRISIND',
'BALRAMCHIN',
'BANDHANBNK',
'BANKBARODA',
'MAHABANK',
'BATAINDIA',
'BAYERCROP',
'BERGEPAINT',
'BDL',
'BEL',
'BHARATFORG',
'BHEL',
'BPCL',
'BHARTIARTL',
'BIOCON',
'BIRLACORPN',
'BSOFT',
'BLUEDART',
'BLUESTARCO',
'BORORENEW',
'BOSCHLTD',
'BRIGADE',
'BRITANNIA',
'MAPMYINDIA',
'CCL',
'CGPOWER',
'CRISIL',
'CSBBANK',
'CANFINHOME',
'CANBK',
'CAPLIPOINT',
'CGCL',
'CARBORUNIV',
'CASTROLIND',
'CEATLTD',
'CENTRALBK',
'CDSL',
'CENTURYPLY',
'CENTURYTEX',
'CERA',
'CHALET',
'CHAMBLFERT',
'CHEMPLASTS',
'CHOLAHLDNG',
'CHOLAFIN',
'CIPLA',
'CUB',
'CLEAN',
'COALINDIA',
'COCHINSHIP',
'COFORGE',
'COLPAL',
'CAMS',
'CONCOR',
'COROMANDEL',
'CREDITACC',
'CROMPTON',
'CUMMINSIND',
'CYIENT',
'DCMSHRIRAM',
'DABUR',
'DALBHARAT',
'DEEPAKNTR',
'DELTACORP',
'DEVYANI',
'DHANI',
'DBL',
'DIVISLAB',
'DIXON',
'LALPATHLAB',
'DRREDDY',
'EIDPARRY',
'EIHOTEL',
'EPL',
'EASEMYTRIP',
'EDELWEISS',
'EICHERMOT',
'ELGIEQUIP',
'EMAMILTD',
'ENDURANCE',
'ESCORTS',
'EXIDEIND',
'NYKAA',
'FEDERALBNK',
'FACT',
'FINEORG',
'FINCABLES',
'FINPIPE',
'FSL',
'FORTIS',
'GRINFRA',
'GMRINFRA',
'GALAXYSURF',
'GICRE',
'GLAND',
'GLAXO',
'GLS',
'GLENMARK',
'GODFRYPHLP',
'GODREJAGRO',
'GODREJCP',
'GODREJIND',
'GODREJPROP',
'GRANULES',
'GRAPHITE',
'GRASIM',
'GESHIP',
'GRINDWELL',
'GUJALKALI',
'GAEL',
'FLUOROCHEM',
'GUJGASLTD',
'GNFC',
'GPPL',
'GSFC',
'GSPL',
'HEG',
'HCLTECH',
'HDFCAMC',
'HDFCBANK',
'HDFCLIFE',
'HFCL',
'HLEGLAS',
'HAPPSTMNDS',
'HATHWAY',
'HAVELLS',
'HEMIPROP',
'HEROMOTOCO',
'HIKAL',
'HINDALCO',
'HGS',
'HAL',
'HINDCOPPER',
'HINDPETRO',
'HINDUNILVR',
'HINDZINC',
'POWERINDIA',
'HOMEFIRST',
'HONAUT',
'HUDCO',
'HDFC',
'ICICIBANK',
'ICICIGI',
'ICICIPRULI',
'ISEC',
'IDBI',
'IDFCFIRSTB',
'IFBIND',
'INDIACEM',
'IBULHSGFIN',
'IBREALEST',
'INDIAMART',
'INDIANB',
'IEX',
'INDHOTEL',
'IOB',
'IRCTC',
'INDIGOPNTS',
'ICIL',
'INDOCO',
'IGL',
'INDUSTOWER',
'INDUSINDBK',
'NAUKRI',
'INFY',
'INOXLEISUR',
'INTELLECT',
'INDIGO',
'IPCALAB',
'JBCHEPHARM',
'JKCEMENT',
'JKLAKSHMI',
'JKPAPER',
'JMFINANCIL',
'JSWENERGY',
'JSWSTEEL',
'JAMNAAUTO',
'JSL',
'JINDALSTEL',
'JUBLFOOD',
'JUBLINGREA',
'JUSTDIAL',
'JYOTHYLAB',
'KPRMILL',
'KEI',
'KNRCON',
'KPITTECH',
'KRBL',
'KAJARIACER',
'KALPATPOWR',
'KALYANKJIL',
'KANSAINER',
'KARURVYSYA',
'KEC',
'KOTAKBANK',
'LTTS',
'LICHSGFIN',
'LAXMIMACH',
'LTI',
'LT',
'LATENTVIEW',
'LAURUSLABS',
'LXCHEM',
'LINDEINDIA',
'LUXIND',
'MMTC',
'MOIL',
'MRF',
'MTARTECH',
'MGL',
'MAHINDCIE',
'MHRIL',
'MAHLOG',
'MANAPPURAM',
'MRPL',
'MARICO',
'MARUTI',
'MASTEK',
'MFSL',
'MAXHEALTH',
'MAZDOCK',
'MEDPLUS',
'METROBRAND',
'METROPOLIS',
'MINDTREE',
'MOTILALOFS',
'MPHASIS',
'MCX',
'MUTHOOTFIN',
'NBCC',
'NCC',
'NHPC',
'NLCINDIA',
'NMDC',
'NOCIL',
'NTPC',
'NATIONALUM',
'NAVINFLUOR',
'NAZARA',
'NESTLEIND',
'NETWORK18',
'NAM-INDIA',
'OBEROIRLTY',
'ONGC',
'OIL',
'PAYTM',
'OFSS',
'ORIENTELEC',
'POLICYBZR',
'PIIND',
'PNBHOUSING',
'PNCINFRA',
'PAGEIND',
'PERSISTENT',
'PETRONET',
'PFIZER',
'PHOENIXLTD',
'PIDILITIND',
'PEL',
'POLYMED',
'POLYCAB',
'POONAWALLA',
'PFC',
'POWERGRID',
'PRAJIND',
'PRESTIGE',
'PRINCEPIPE',
'PRSMJOHNSN',
'PRIVISCL',
'PGHL',
'PGHH',
'PNB',
'QUESS',
'RBLBANK',
'RECLTD',
'RITES',
'RADICO',
'RVNL',
'RAILTEL',
'RAIN',
'RAJESHEXPO',
'RALLIS',
'RCF',
'RTNINDIA',
'REDINGTON',
'RELAXO',
'RELIANCE',

'ROUTE',
'SBICARD',
'SBILIFE',
'SIS',
'SKFINDIA',
'SRF',
'SANOFI',
'SAPPHIRE',
'SAREGAMA',
'SCHAEFFLER',
'SEQUENT',
'SFL',
'SHILPAMED',
'SCI',
'RENUKA',
'SHRIRAMCIT',
'SRTRANSFIN',
'SHYAMMETL',
'SIEMENS',
'SOBHA',
'SOLARA',
'SONACOMS',
'SONATSOFTW',
'SPICEJET',
'STARHEALTH',
'SBIN',
'SAIL',
'SWSOLAR',
'STLTECH',
'STAR',
'SUDARSCHEM',
'SUMICHEM',
'SPARC',
'SUNPHARMA',
'SUNTV',
'SUNDARMFIN',
'SUNDRMFAST',
'SUNTECK',
'SUPRAJIT',
'SUPREMEIND',
'SUVENPHAR',
'SYMPHONY',
'SYNGENE',
'TCNSBRANDS',
'TTKPRESTIG',
'TV18BRDCST',
'TVSMOTOR',
'TANLA',
'TATACHEM',
'TATACOFFEE',
'TATACOMM',
'TCS',
'TATACONSUM',
'TATAELXSI',
'TATAINVEST',
'TATAMTRDVR',
'TATAMOTORS',
'TATAPOWER',
'TATASTLLP',
'TATASTEEL',
'TTML',
'TEAMLEASE',
'TECHM',
'NIACL',
'RAMCOCEM',
'THERMAX',
'TIMKEN',
'TITAN',
'TORNTPHARM',
'TORNTPOWER',
'TRENT',
'TRIDENT',
'TRIVENI',
'TRITURBINE',
'TIINDIA',
'UFLEX',
'UPL',
'UTIAMC',
'ULTRACEMCO',
'UNIONBANK',
'UBL',
'VGUARD',
'VMART',
'VIPIND',
'VAIBHAVGBL',
'VAKRANGEE',
'VTL',
'VARROC',
'VBL',
'VEDL',
'VENKEYS',
'VIJAYA',
'VOLTAS',
'WELCORP',
'WELSPUNIND',
'WESTLIFE',
'WHIRLPOOL',
'WIPRO',
'WOCKPHARMA',
'YESBANK',
'ZEEL',
'ZENSARTECH',
'ZOMATO',
'ZYDUSLIFE',
'ZYDUSWELL',
'ECLERX']
num=1
for stock in stocks:
    sbin = get_history(symbol=stock,start=date(2022,9,1),end=date(2022,10,7))

    df = pd.DataFrame(sbin)
    sma = get_sma(df['Close'], 20) # Get 20 day SMA
    bollinger_up, bollinger_down = get_bollinger_bands(df['Close'])

    # print(bollinger_down[-1],bollinger_up[-1])
    do=bollinger_down[-1]
    up=bollinger_up[-1]
    print(num)
    num=num+1
    if(do>df['High'][-1] and do>df['Low'][-1]):
        print(stock)

# sbin = get_history(symbol="SBIN",start=date(2021,1,1),end=date(2022,10,7))
# df = pd.DataFrame(sbin)

# print(df["High"][-1])















