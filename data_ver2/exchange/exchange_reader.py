import requests
import pandas as pd

def make_market_df(data, ticker, name):

    df = pd.DataFrame(data["result"])

    df = df[["localTradedAt", "closePrice", "fluctuations", "fluctuationsRatio"]]

    df = df.rename(columns={
        "localTradedAt": "date",
        "closePrice": "close",
        "fluctuations": "change",
        "fluctuationsRatio": "rate"
    })

    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

    df["close"] = (
        df["close"]
        .str.replace(",", "", regex=False)
        .astype(float)
    )

    df["change"] = (
        df["change"]
        .str.replace(",", "", regex=False)
        .astype(float)
    )

    df["rate"] = (
        df["rate"]
        .astype(float)
    )

    df["ticker"] = ticker
    df["name"] = name

    df = df[
        ["date", "ticker", "name", "close", "change", "rate"]
    ]

    return (
        df
        .sort_values("date")
        .reset_index(drop=True)
    )

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


    
