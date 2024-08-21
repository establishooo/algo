from dotenv import load_dotenv
import os
from pycoingecko import CoinGeckoAPI

# تحميل المتغيرات البيئية من ملف .env
load_dotenv()

# الحصول على مفتاح API CoinGecko من المتغيرات البيئية
coingecko_api_key = os.getenv('COINGECKO_API_KEY')

# إنشاء كائن CoinGeckoAPI باستخدام المفتاح
cg = CoinGeckoAPI(api_key=coingecko_api_key)

def get_bitcoin_price():
    try:
        bitcoin_price = cg.get_price(ids='bitcoin', vs_currencies='usd')
        return f"سعر البيتكوين: ${bitcoin_price['bitcoin']['usd']}"
    except Exception as e:
        return f"حدث خطأ أثناء جلب سعر البيتكوين: {e}"

def get_market_data():
    try:
        market_data = cg.get_coins_markets(vs_currency='usd')
        return f"عدد العملات المشفرة المدرجة: {len(market_data)}"
    except Exception as e:
        return f"حدث خطأ أثناء جلب بيانات السوق: {e}"

def get_historical_data():
    try:
        historical_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)
        return f"عدد نقاط البيانات التاريخية للبيتكوين (آخر 30 يوم): {len(historical_data['prices'])}"
    except Exception as e:
        return f"حدث خطأ أثناء جلب البيانات التاريخية: {e}"

def get_detailed_bitcoin_data():
    try:
        bitcoin_data = cg.get_coin_by_id(id='bitcoin')
        return f"اسم العملة: {bitcoin_data['name']}\n" \
               f"السعر الحالي بالدولار: ${bitcoin_data['market_data']['current_price']['usd']}\n" \
               f"القيمة السوقية: ${bitcoin_data['market_data']['market_cap']['usd']}\n" \
               f"حجم التداول (24 ساعة): ${bitcoin_data['market_data']['total_volume']['usd']}"
    except Exception as e:
        return f"حدث خطأ أثناء جلب البيانات المفصلة للبيتكوين: {e}"

if __name__ == "__main__":
    print(get_bitcoin_price())
    print(get_market_data())
    print(get_historical_data())
    print(get_detailed_bitcoin_data())