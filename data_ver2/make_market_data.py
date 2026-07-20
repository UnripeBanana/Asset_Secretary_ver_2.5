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
        .astype(int)
    )

    df["change"] = (
        df["change"]
        .str.replace(",", "", regex=False)
        .astype(int)
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
