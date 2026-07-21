from data_ver2.domestic_stock.reader import domestic_stock_data_reader
from data_ver2.market_index.reader import market_index_reader
from data_ver2.make_market_chart import make_market_index_chart

#make_market_chart(gold_reader(20250721, 20260721, "M04020000", "KRX Gold"))
#market_index_reader(start, end, category, ticker, name):

#------------------------------
# Metals
#------------------------------
make_market_index_chart(market_index_reader(20250721, 20260721, "metals", "M04020000", "KRX Gold"))
make_market_index_chart(market_index_reader(20250721, 20260721, "metals", "GCcv1", "International Gold"))
make_market_index_chart(market_index_reader(20250721, 20260721, "metals", "SIcv1", "International Silver"))

#------------------------------
# Exchange
#------------------------------
make_market_index_chart(market_index_reader(20250721, 20260721, "exchange", "FX_USDKRW", "Dollar Won Exchange"))
make_market_index_chart(market_index_reader(20250721, 20260721, "exchange", ".DXY", "Dollar Index"))

#------------------------------
# Energy
#------------------------------
make_market_index_chart(market_index_reader(20250721, 20260721, "energy", "CLcv1", "West Texas Intermediate"))
make_market_index_chart(market_index_reader(20250721, 20260721, "energy", "LCOcv1", "Brent Crude"))

#------------------------------
# Bond
#------------------------------
make_market_index_chart(market_index_reader(20250721, 20260721, "bond", "US30YT%3DRR", "USA Bond 30y"))
make_market_index_chart(market_index_reader(20250721, 20260721, "bond", "US10YT%3DRR", "USA Bond 10y"))
make_market_index_chart(market_index_reader(20250721, 20260721, "bond", "US3YT%3DRR", "USA Bond 3y"))

make_market_index_chart(market_index_reader(20250721, 20260721, "bond", "KR30YT%3DRR", "Korea Bond 30y"))
make_market_index_chart(market_index_reader(20250721, 20260721, "bond", "KR10YT%3DRR", "Korea Bond 10y"))
make_market_index_chart(market_index_reader(20250721, 20260721, "bond", "KR3YT%3DRR", "Korea Bond 3y"))
