import requests
import pandas as pd
from data_ver2.make_market_data import make_market_df

def gold_reader():
    i = 1
    ticker = "M04020000"

    krx_gold_data = pd.DataFrame()
    
    while i < 5:
        url = (
            "https://m.stock.naver.com/front-api/marketIndex/prices"
            "?category=metals"
            f"&reutersCode={ticker}"
            f"&page={i}"
        )
        
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Referer": "https://m.stock.naver.com/"
        }
        
        response = requests.get(url, headers=headers)
        
        data = response.json()

        page_df = make_market_df(data, "M04020000", "KRX Gold")

        # 기존 데이터 + 이번 페이지 데이터 합치기
        krx_gold_data = pd.concat(
            [krx_gold_data, page_df],
            ignore_index=True
        )
        i += 1

    
    krx_gold_data = (
        krx_gold_data
        .sort_values("date")
        .reset_index(drop=True)
    )

    print(krx_gold_data)

    return krx_gold_data


    

#{'isSuccess': True, 'detailCode': '', 'message': '', 'result': [{'localTradedAt': '2026-07-20T00:00:00+09:00', 'closePrice': '190,000', 'fluctuationsType': {'code': '5', 'text': '하락', 'name': 'FALLING'}, 'fluctuations': '-1,420', 'fluctuationsRatio': '-0.74', 'openPrice': '0', 'highPrice': '0', 'lowPrice': '0'}, {'localTradedAt': '2026-07-16T00:00:00+09:00', 'closePrice': '191,420', 'fluctuationsType': {'code': '5', 'text': '하락', 'name': 'FALLING'}, 'fluctuations': '-580', 'fluctuationsRatio': '-0.30', 'openPrice': '0', 'highPrice': '0', 'lowPrice': '0'}, {'localTradedAt': '2026-07-15T00:00:00+09:00', 'closePrice': '192,000', 'fluctuationsType': {'code': '5', 'text': '하락', 'name': 'FALLING'}, 'fluctuations': '-980', 'fluctuationsRatio': '-0.51', 'openPrice': '0', 'highPrice': '0', 'lowPrice': '0'}, {'localTradedAt': '2026-07-14T00:00:00+09:00', 'closePrice': '192,980', 'fluctuationsType': {'code': '5', 'text': '하락', 'name': 'FALLING'}, 'fluctuations': '-2,530', 'fluctuationsRatio': '-1.29', 'openPrice': '0', 'highPrice': '0', 'lowPrice': '0'}, {'localTradedAt': '2026-07-13T00:00:00+09:00', 'closePrice': '195,510', 'fluctuationsType': {'code': '5', 'text': '하락', 'name': 'FALLING'}, 'fluctuations': '-2,760', 'fluctuationsRatio': '-1.39', 'openPrice': '0', 'highPrice': '0', 'lowPrice': '0'}, {'localTradedAt': '2026-07-10T00:00:00+09:00', 'closePrice': '198,270', 'fluctuationsType': {'code': '2', 'text': '상승', 'name': 'RISING'}, 'fluctuations': '460', 'fluctuationsRatio': '0.23', 'openPrice': '0', 'highPrice': '0', 'lowPrice': '0'}, {'localTradedAt': '2026-07-09T00:00:00+09:00', 'closePrice': '197,810', 'fluctuationsType': {'code': '5', 'text': '하락', 'name': 'FALLING'}, 'fluctuations': '-1,100', 'fluctuationsRatio': '-0.55', 'openPrice': '0', 'highPrice': '0', 'lowPrice': '0'}, {'localTradedAt': '2026-07-08T00:00:00+09:00', 'closePrice': '198,910', 'fluctuationsType': {'code': '5', 'text': '하락', 'name': 'FALLING'}, 'fluctuations': '-3,100', 'fluctuationsRatio': '-1.53', 'openPrice': '0', 'highPrice': '0', 'lowPrice': '0'}, {'localTradedAt': '2026-07-07T00:00:00+09:00', 'closePrice': '202,010', 'fluctuationsType': {'code': '5', 'text': '하락', 'name': 'FALLING'}, 'fluctuations': '-1,770', 'fluctuationsRatio': '-0.87', 'openPrice': '0', 'highPrice': '0', 'lowPrice': '0'}, {'localTradedAt': '2026-07-06T00:00:00+09:00', 'closePrice': '203,780', 'fluctuationsType': {'code': '5', 'text': '하락', 'name': 'FALLING'}, 'fluctuations': '-560', 'fluctuationsRatio': '-0.27', 'openPrice': '0', 'highPrice': '0', 'lowPrice': '0'}]}
