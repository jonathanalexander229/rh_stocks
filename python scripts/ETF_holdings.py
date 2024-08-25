import robin_stocks.robinhood as r

# Login to Robinhood
r.login('joncrissey@gmail.com')

# Get the holdings of an ETF
holdings = r.account.get_holdings('QQQ')

# Check if NVDA is in the holdings
if 'NVDA' in holdings:
    print('NVDA is in the holdings of this ETF.')
else:
    print('NVDA is not in the holdings of this ETF.')