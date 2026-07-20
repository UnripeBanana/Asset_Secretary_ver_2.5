#[['날짜', '시가', '고가', '저가', '종가', '거래량', '외국인소진율'],
#["20240213", 74800, 75200, 74400, 75200, 21966745, 54.52]]
#-> 이런 식으로 구성돼있음

import requests
import pandas as pd
from io import StringIO
import ast

def domestic_stock_data_reader():
    start = 20240211
    end = 20260720
    ticker = "005930"
    
    url = (
        f"https://m.stock.naver.com/front-api/external/chart/domestic/info"
        f"?symbol={ticker}"
        f"&requestType=1"
        f"&startTime={start}"
        f"&endTime={end}"
        f"&timeframe=day"
    )
    
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    
    response = requests.get(
        url, 
        headers=headers,
        timeout=10
    )

    #print(response.headers["Content-Type"])

    try:
        data = response.json()
        print(type(data))
        print(data[:2])
    except Exception as e:
        print(e)

    """
    df = pd.read_csv(StringIO(response.text))

    print(response.text[:200])
    #print(df.head())
    


    data = ast.literal_eval(response.text)
    
    df = pd.DataFrame(
        data[1:],      # 데이터
        columns=data[0]  # 헤더
    )

    print(df.head())
    """


"""
    # 네이버는 브라우저가 아닌 프로그램의 요청을 차단하는 경우가 있어서, 브라우저인 척 속이는 역할 수행
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    url = (
        f"https://polling.finance.naver.com/api/realtime"
        f"?query=SERVICE_ITEM:{ticker}"
    )

    data = requests.get(
        url,
        headers=headers,
        timeout=10 # 최대 10초까지만 기다리겠다는 의미.
    ).json()

    krx_item = data["result"]["areas"][0]["datas"][0]
    nxt_item = data["result"]["areas"][0]["datas"][0]["nxtOverMarketPriceInfo"]
  
    return {
        "cd": krx_item["cd"],      # 티커
        "nm": krx_item["nm"],      # 종목명
        "nv": krx_item["nv"],      # 현재가
        "cv": krx_item["cv"],      # 전일 대비 가격 변화(원)
        "cr": krx_item["cr"],      # 등락률(%)
        "rf": krx_item["rf"],      # 등락 구분(2:상승/3:보합/5:하락을 나타내는 코드)
        "ms": krx_item["ms"],      # 장상태(OPEN/CLOSE)
        "pcv": krx_item["pcv"],    # Previous Close Value, 전일종가
        "ov": krx_item["ov"],      # 시가
        "hv": krx_item["hv"],      # 고가
        "lv": krx_item["lv"],      # 저가
        "aq": krx_item["aq"],      # 거래량
        "aa": krx_item["aa"],      # 거래대금 : 하루동안 얼마가 거래되었는가 (평균 거래대금보다 많은 양이 거래될 시 신뢰도 있는 등락이라고 판단)
        "countOfListedStock": krx_item["countOfListedStock"]  # 상장주식수
    }

def to_int(value):
    if value in (None, "", "-"):
        return None
    return int(value.replace(",", ""))

def get_gold_prop():
    # 직접 접속 : https://m.stock.naver.com/marketindex/metals/M04020000
    url = "https://m.stock.naver.com/front-api/realTime/marketIndex/metals"
    
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Origin": "https://m.stock.naver.com",
        "Referer": "https://m.stock.naver.com/marketindex/metals/M04020000",
    }
    
    payload = {
        "reutersCodes": ["M04020000"]
    }
    
    response = requests.post(
        url,
        headers=headers,
        json=payload,
        timeout=10
    )
"""
