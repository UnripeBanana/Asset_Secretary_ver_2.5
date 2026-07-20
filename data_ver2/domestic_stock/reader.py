#[['날짜', '시가', '고가', '저가', '종가', '거래량', '외국인소진율'],
#["20240213", 74800, 75200, 74400, 75200, 21966745, 54.52]]
#-> 이런 식으로 구성돼있음

import requests
import pandas as pd
from io import StringIO

def domestic_stock_data_reader():
    start_day = 20240211
    end_day = 20260720
    
    start = f"&startTime={start_day}"
    end = f"&endTime={end_day}"
    
    url = (
        "https://m.stock.naver.com/front-api/external/chart/domestic/info",
        "?symbol=005930",
        "&requestType=1",
        start,
        end,
        "&timeframe=day"
    )
    
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    
    response = requests.get(url, headers=headers)
    
    df = pd.read_csv(StringIO(response.text))
    
    print(df.head())
