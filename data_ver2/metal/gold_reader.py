import requests

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

    print(data)
