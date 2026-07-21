from data_ver2.domestic_stock.reader import domestic_stock_data_reader
from data_ver2.market_index.reader import market_index_reader

make_market_chart(gold_reader(20250721, 20260721, "M04020000", "KRX Gold"))
market_index_reader(start, end, category, ticker, name):

    #start = pd.to_datetime(start, format="%Y%m%d")
    #end = pd.to_datetime(end, format="%Y%m%d")
    #ticker = "M04020000"
    #name = "KRX Gold"

#make_market_chart(exchange_reader())
