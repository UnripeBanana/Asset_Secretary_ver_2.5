import requests
import pandas as pd

def make_market_df(data, ticker, name):

    # 네이버 증권에서 받은 오리지널 데이터
    df = pd.DataFrame(data["result"])

    # 오리지널 데이터에서 불필요한 부분 제거
    df = df[["localTradedAt", "closePrice", "fluctuations", "fluctuationsRatio"]]

    # 기존에 사용 중인 명칭으로 변경
    df = df.rename(columns={
        "localTradedAt": "date",
        "closePrice": "close",
        "fluctuations": "change",
        "fluctuationsRatio": "rate"
    })

    # 기존에 사용중인 형식으로 변경
    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

    # str -> int
    df["close"] = (
        df["close"]
        .str.replace(",", "", regex=False)
        .astype(float)
    )

    # str -. int
    df["change"] = (
        df["change"]
        .str.replace(",", "", regex=False)
        .astype(float)
    )

    # str -> float
    df["rate"] = (
        df["rate"]
        .astype(float)
    )

    # 사용자로부터 입력받은 데이터 입력
    df["ticker"] = ticker
    df["name"] = name

    # 데이터프레임 컬럼 순서 설정
    df = df[
        ["date", "ticker", "name", "close", "change", "rate"]
    ]

    # 날짜 순으로 정렬 후 return
    return (
        df
        .sort_values("date")
        .reset_index(drop=True)
    )

def gold_reader(start, end, ticker, name):
    start = pd.to_datetime(str(start), format="%Y%m%d")
    end = pd.to_datetime(str(end), format="%Y%m%d")
    #ticker = "M04020000"
    #name = "KRX Gold"

    page = 1
    dfs = []
    
    while True:
        url = (
            "https://m.stock.naver.com/front-api/marketIndex/prices"
            "?category=metals"
            f"&reutersCode={ticker}"
            f"&page={page}"
        )
        
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Referer": "https://m.stock.naver.com/"
        }
        
        response = requests.get(url, headers=headers)
        
        data = response.json()

        if not data.get("result"):
            break    

        page_df = make_market_df(data, ticker, name)

        page_df["date"] = pd.to_datetime(page_df["date"])

        dfs.append(page_df)
        
        oldest = pd.to_datetime(page_df["date"]).min()
    
        if oldest <= start:
            break
    
        page += 1        

    krx_gold_data = pd.concat(dfs, ignore_index=True)

    krx_gold_data = krx_gold_data[
        (krx_gold_data["date"] >= start) &
        (krx_gold_data["date"] <= end)
    ]
    
    krx_gold_data = (
        krx_gold_data
        .sort_values("date")
        .reset_index(drop=True)
    )
    
    krx_gold_data["date"] = krx_gold_data["date"].dt.strftime("%Y-%m-%d")
    
    print(krx_gold_data)

    return krx_gold_data



    

#{'isSuccess': True, 'detailCode': '', 'message': '', 'result': [{'localTradedAt': '2026-07-20T00:00:00+09:00', 'closePrice': '190,000', 'fluctuationsType': {'code': '5', 'text': '하락', 'name': 'FALLING'}, 'fluctuations': '-1,420', 'fluctuationsRatio': '-0.74', 'openPrice': '0', 'highPrice': '0', 'lowPrice': '0'}, {'localTradedAt': '2026-07-16T00:00:00+09:00', 'closePrice': '191,420', 'fluctuationsType': {'code': '5', 'text': '하락', 'name': 'FALLING'}, 'fluctuations': '-580', 'fluctuationsRatio': '-0.30', 'openPrice': '0', 'highPrice': '0', 'lowPrice': '0'}, {'localTradedAt': '2026-07-15T00:00:00+09:00', 'closePrice': '192,000', 'fluctuationsType': {'code': '5', 'text': '하락', 'name': 'FALLING'}, 'fluctuations': '-980', 'fluctuationsRatio': '-0.51', 'openPrice': '0', 'highPrice': '0', 'lowPrice': '0'}, {'localTradedAt': '2026-07-14T00:00:00+09:00', 'closePrice': '192,980', 'fluctuationsType': {'code': '5', 'text': '하락', 'name': 'FALLING'}, 'fluctuations': '-2,530', 'fluctuationsRatio': '-1.29', 'openPrice': '0', 'highPrice': '0', 'lowPrice': '0'}, {'localTradedAt': '2026-07-13T00:00:00+09:00', 'closePrice': '195,510', 'fluctuationsType': {'code': '5', 'text': '하락', 'name': 'FALLING'}, 'fluctuations': '-2,760', 'fluctuationsRatio': '-1.39', 'openPrice': '0', 'highPrice': '0', 'lowPrice': '0'}, {'localTradedAt': '2026-07-10T00:00:00+09:00', 'closePrice': '198,270', 'fluctuationsType': {'code': '2', 'text': '상승', 'name': 'RISING'}, 'fluctuations': '460', 'fluctuationsRatio': '0.23', 'openPrice': '0', 'highPrice': '0', 'lowPrice': '0'}, {'localTradedAt': '2026-07-09T00:00:00+09:00', 'closePrice': '197,810', 'fluctuationsType': {'code': '5', 'text': '하락', 'name': 'FALLING'}, 'fluctuations': '-1,100', 'fluctuationsRatio': '-0.55', 'openPrice': '0', 'highPrice': '0', 'lowPrice': '0'}, {'localTradedAt': '2026-07-08T00:00:00+09:00', 'closePrice': '198,910', 'fluctuationsType': {'code': '5', 'text': '하락', 'name': 'FALLING'}, 'fluctuations': '-3,100', 'fluctuationsRatio': '-1.53', 'openPrice': '0', 'highPrice': '0', 'lowPrice': '0'}, {'localTradedAt': '2026-07-07T00:00:00+09:00', 'closePrice': '202,010', 'fluctuationsType': {'code': '5', 'text': '하락', 'name': 'FALLING'}, 'fluctuations': '-1,770', 'fluctuationsRatio': '-0.87', 'openPrice': '0', 'highPrice': '0', 'lowPrice': '0'}, {'localTradedAt': '2026-07-06T00:00:00+09:00', 'closePrice': '203,780', 'fluctuationsType': {'code': '5', 'text': '하락', 'name': 'FALLING'}, 'fluctuations': '-560', 'fluctuationsRatio': '-0.27', 'openPrice': '0', 'highPrice': '0', 'lowPrice': '0'}]}
