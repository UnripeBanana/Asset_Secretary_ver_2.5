from data_ver2.domestic_stock.reader import domestic_stock_data_reader
from data_ver2.market_index.reader import market_index_reader

#make_market_chart(gold_reader(20250721, 20260721, "M04020000", "KRX Gold"))
#market_index_reader(start, end, category, ticker, name):

make_market_chart(market_index_reader(20250721, 20260721, category, "M04020000", "KRX Gold"))
