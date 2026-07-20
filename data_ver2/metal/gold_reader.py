import requests
import pandas as pd

def gold_reader():
    url = (
        "https://m.stock.naver.com/front-api/marketIndex/prices"
        "?category=metals"
        "&reutersCode=M04020000"
        "&page=1"
    )
    
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://m.stock.naver.com/"
    }
    
    response = requests.get(url, headers=headers)
    
    data = response.json()

    krx_gold_data = make_market_df(data, "M04020000", "KRX Gold")


    

#{'isSuccess': True, 'detailCode': '', 'message': '', 'result': [{'localTradedAt': '2026-07-20T00:00:00+09:00', 'closePrice': '190,000', 'fluctuationsType': {'code': '5', 'text': '하락', 'name': 'FALLING'}, 'fluctuations': '-1,420', 'fluctuationsRatio': '-0.74', 'openPrice': '0', 'highPrice': '0', 'lowPrice': '0'}, {'localTradedAt': '2026-07-16T00:00:00+09:00', 'closePrice': '191,420', 'fluctuationsType': {'code': '5', 'text': '하락', 'name': 'FALLING'}, 'fluctuations': '-580', 'fluctuationsRatio': '-0.30', 'openPrice': '0', 'highPrice': '0', 'lowPrice': '0'}, {'localTradedAt': '2026-07-15T00:00:00+09:00', 'closePrice': '192,000', 'fluctuationsType': {'code': '5', 'text': '하락', 'name': 'FALLING'}, 'fluctuations': '-980', 'fluctuationsRatio': '-0.51', 'openPrice': '0', 'highPrice': '0', 'lowPrice': '0'}, {'localTradedAt': '2026-07-14T00:00:00+09:00', 'closePrice': '192,980', 'fluctuationsType': {'code': '5', 'text': '하락', 'name': 'FALLING'}, 'fluctuations': '-2,530', 'fluctuationsRatio': '-1.29', 'openPrice': '0', 'highPrice': '0', 'lowPrice': '0'}, {'localTradedAt': '2026-07-13T00:00:00+09:00', 'closePrice': '195,510', 'fluctuationsType': {'code': '5', 'text': '하락', 'name': 'FALLING'}, 'fluctuations': '-2,760', 'fluctuationsRatio': '-1.39', 'openPrice': '0', 'highPrice': '0', 'lowPrice': '0'}, {'localTradedAt': '2026-07-10T00:00:00+09:00', 'closePrice': '198,270', 'fluctuationsType': {'code': '2', 'text': '상승', 'name': 'RISING'}, 'fluctuations': '460', 'fluctuationsRatio': '0.23', 'openPrice': '0', 'highPrice': '0', 'lowPrice': '0'}, {'localTradedAt': '2026-07-09T00:00:00+09:00', 'closePrice': '197,810', 'fluctuationsType': {'code': '5', 'text': '하락', 'name': 'FALLING'}, 'fluctuations': '-1,100', 'fluctuationsRatio': '-0.55', 'openPrice': '0', 'highPrice': '0', 'lowPrice': '0'}, {'localTradedAt': '2026-07-08T00:00:00+09:00', 'closePrice': '198,910', 'fluctuationsType': {'code': '5', 'text': '하락', 'name': 'FALLING'}, 'fluctuations': '-3,100', 'fluctuationsRatio': '-1.53', 'openPrice': '0', 'highPrice': '0', 'lowPrice': '0'}, {'localTradedAt': '2026-07-07T00:00:00+09:00', 'closePrice': '202,010', 'fluctuationsType': {'code': '5', 'text': '하락', 'name': 'FALLING'}, 'fluctuations': '-1,770', 'fluctuationsRatio': '-0.87', 'openPrice': '0', 'highPrice': '0', 'lowPrice': '0'}, {'localTradedAt': '2026-07-06T00:00:00+09:00', 'closePrice': '203,780', 'fluctuationsType': {'code': '5', 'text': '하락', 'name': 'FALLING'}, 'fluctuations': '-560', 'fluctuationsRatio': '-0.27', 'openPrice': '0', 'highPrice': '0', 'lowPrice': '0'}]}
