def make_market_df(data, ticker, name):

    df = pd.DataFrame(data["result"])

    df = df[["localTradedAt", "closePrice"]]

    df = df.rename(columns={
        "localTradedAt": "date",
        "closePrice": "close"
    })

    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

    df["close"] = (
        df["close"]
        .str.replace(",", "", regex=False)
        .astype(int)
    )

    df["ticker"] = ticker
    df["name"] = name

    df = df[
        ["date", "ticker", "name", "close"]
    ]

    return (
        df
        .sort_values("date")
        .reset_index(drop=True)
    )
