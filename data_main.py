from data_ver2.domestic_stock.reader import domestic_stock_data_reader
from data_ver2.metal.gold_reader import gold_reader
from data_ver2.make_market_chart import make_market_chart
from data_ver2.exchange.exchange_reader import exchange_reader


make_market_chart(gold_reader())

make_market_chart(exchange_reader())
