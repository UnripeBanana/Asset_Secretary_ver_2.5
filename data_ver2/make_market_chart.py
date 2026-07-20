import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def make_market_chart(df):
    # ---------------------------------
    # 날짜를 datetime 형식으로 변환
    # ---------------------------------
    df["date"] = pd.to_datetime(df["date"])
    
    # ---------------------------------
    # 그래프 생성
    # ---------------------------------
    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.plot(
        df["date"],
        df["close"],
        marker="o",
        linewidth=2,
        markersize=5,
    )
    
    # ---------------------------------
    # 제목
    # ---------------------------------
    ax.set_title("KRX Gold Price", fontsize=18)
    
    # ---------------------------------
    # 축 이름
    # ---------------------------------
    ax.set_xlabel("Date")
    ax.set_ylabel("Price (KRW)")
    
    # ---------------------------------
    # x축 날짜 표시
    # 월요일만 표시
    # ---------------------------------
    ax.xaxis.set_major_locator(
        mdates.WeekdayLocator(byweekday=mdates.MO)
    )
    
    ax.xaxis.set_major_formatter(
        mdates.DateFormatter("%m-%d")
    )
    
    # ---------------------------------
    # 격자
    # ---------------------------------
    ax.grid(True)
    
    # ---------------------------------
    # 현재 가격 표시
    # ---------------------------------
    last_date = df.iloc[-1]["date"]
    last_price = df.iloc[-1]["close"]
    
    ax.scatter(last_date, last_price, s=80)
    
    ax.text(
        last_date,
        last_price,
        f"{last_price:,}",
        fontsize=10,
        ha="left",
        va="bottom"
    )
    
    # ---------------------------------
    # 여백 자동 조절
    # ---------------------------------
    plt.tight_layout()
    
    # ---------------------------------
    # 화면 출력
    # ---------------------------------
    plt.show()

    # 저장
    plt.tight_layout()
    name = "시험용 금 이미지"
    
    title = f"data/image/{name}.png"
    
    plt.savefig(
        title,
        dpi=300,
        bbox_inches="tight"
    )
