import requests
import pandas as pd
from data_ver2.make_market_data import make_market_df

def exchange_reader():
    i = 1
    ticker = "FX_USDKRW"

    exchange_data = pd.DataFrame()
    
    while i < 5:
        url = (
            "https://m.stock.naver.com/front-api/marketIndex/prices"
            "?category=exchange"
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
        exchange_data = pd.concat(
            [exchange_data, page_df],
            ignore_index=True
        )
        i += 1

    
    exchange_data = (
        exchange_data
        .sort_values("date")
        .reset_index(drop=True)
    )

    print(exchange_data)

    return exchange_data


    
