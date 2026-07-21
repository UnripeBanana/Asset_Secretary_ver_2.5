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
