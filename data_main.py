from data_ver2.domestic_stock.reader import domestic_stock_data_reader
from data_ver2.market_index.reader import market_index_reader
from data_ver2.make_market_chart import make_market_index_chart
from data_ver2.base_interest_rate.reader import base_interest_rate_reader

def domestic_stock_data_reader(start, end, ticker):

#------------------------------
# Domestic Stock
#------------------------------


#------------------------------
# Metals
#------------------------------
make_market_index_chart(market_index_reader(20250721, 20260721, "metals", "M04020000", "KRX Gold", "KRW"))
make_market_index_chart(market_index_reader(20250721, 20260721, "metals", "GCcv1", "International Gold", "USD"))
make_market_index_chart(market_index_reader(20250721, 20260721, "metals", "SIcv1", "International Silver", "USD"))

#------------------------------
# Exchange
#------------------------------
make_market_index_chart(market_index_reader(20250721, 20260721, "exchange", "FX_USDKRW", "Dollar Won Exchange", "USD/KRW"))
make_market_index_chart(market_index_reader(20250721, 20260721, "exchange", ".DXY", "Dollar Index", "Point"))

#------------------------------
# Energy
#------------------------------
make_market_index_chart(market_index_reader(20250721, 20260721, "energy", "CLcv1", "West Texas Intermediate", "USD"))
make_market_index_chart(market_index_reader(20250721, 20260721, "energy", "LCOcv1", "Brent Crude", "USD"))

#------------------------------
# Bond
#------------------------------
make_market_index_chart(market_index_reader(20250721, 20260721, "bond", "US30YT%3DRR", "USA Bond 30y", "USD"))
make_market_index_chart(market_index_reader(20250721, 20260721, "bond", "US10YT%3DRR", "USA Bond 10y", "USD"))
make_market_index_chart(market_index_reader(20250721, 20260721, "bond", "US3YT%3DRR", "USA Bond 3y", "USD"))

make_market_index_chart(market_index_reader(20250721, 20260721, "bond", "KR30YT%3DRR", "Korea Bond 30y", "KRW"))
make_market_index_chart(market_index_reader(20250721, 20260721, "bond", "KR10YT%3DRR", "Korea Bond 10y", "KRW"))
make_market_index_chart(market_index_reader(20250721, 20260721, "bond", "KR3YT%3DRR", "Korea Bond 3y", "KRW"))

#------------------------------
# Base Interest Rate
#------------------------------
make_market_index_chart(base_interest_rate_reader(20250721, 20260721, "standardInterest", "USA", "USA Base Interest Rate", "%"))

make_market_index_chart(base_interest_rate_reader(20250721, 20260721, "standardInterest", "KOR", "Korea Base Interest Rate", "%"))
