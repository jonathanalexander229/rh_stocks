"""
This script is designed to find options strategies that have a high probability of profit. 
It uses the robin_stocks library to interact with the Robinhood API.

The user is prompted to enter their Robinhood username and password, which are used to log in to Robinhood.

The user is also prompted to enter the stock symbols for which they want to find options. 
The input is split into a list of symbols, and leading and trailing whitespace is removed from each symbol.

The script then defines the profitability criteria. 
The 'chance_of_profit_short' is set as the type of profit, which represents the probability of making a profit if the option is shorted.

The script uses these inputs to find options strategies that have a 70% chance of profit when sold and a 30% chance of profit when bought.

Finally, the script outputs the data collected to a CSV file for further analysis.
"""

import robin_stocks.robinhood.options as roptions
import robin_stocks.robinhood as r
import getpass
import pandas as pd

username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")
login = r.login(username, password)

# Prompt the user to enter the stock symbols
inputSymbols = input("Enter a stock symbol, separated by commas: ").split(',')

orderType = input("Enter the order type (call or put): ")

# Remove leading and trailing whitespace from each symbol
inputSymbols = [symbol.strip() for symbol in inputSymbols]

# Define the symbols for which you want to find options
#inputSymbols = ['AMD','META','NFLX']

# Define the profitability criteria
typeProfit = 'chance_of_profit_short'
profitFloor = 0.70
profitCeiling = 0.78

# Define the expiration date, strike price, and option type
expirationDate = '2024-03-22'
strikePrice = None
optionType = 'put'

# Find options that meet the profitability criteria
options = roptions.find_options_by_specific_profitability(
    inputSymbols, 
    expirationDate=expirationDate, 
    strikePrice=strikePrice, 
    optionType=optionType, 
    typeProfit=typeProfit, 
    profitFloor=profitFloor, 
    profitCeiling=profitCeiling, 
    info=None
)

# Convert the list of options to a DataFrame and select only the specified columns
df = pd.DataFrame(options)[[
    'symbol', 
    'strike_price', 
    'expiration_date', 
    'ask_price', 
    'bid_price', 
    'volume', 
    'break_even_price', 
    'chance_of_profit_long', 
    'chance_of_profit_short', 
    'implied_volatility', 
    'delta', 
    'rho', 
    'theta', 
    'vega'
]]

# Limit the decimal places of some columns to 2
df[['ask_price', 'bid_price', 'strike_price', 'break_even_price']] = df[['ask_price', 'bid_price', 'strike_price', 'break_even_price']].astype(float).round(2)


# Limit the decimal places of some columns to 2
df[['chance_of_profit_long', 'chance_of_profit_short', 'implied_volatility']] = df[['chance_of_profit_long', 'chance_of_profit_short', 'implied_volatility']].astype(float).round(4)

# Rename the columns
df = df.rename(columns={ 
    'strike_price': 'strike', 
    'expiration_date': 'exp date', 
    'ask_price': 'ask', 
    'bid_price': 'bid', 
    'volume': 'volume', 
    'break_even_price': 'break even', 
    'chance_of_profit_long': 'PoP long', 
    'chance_of_profit_short': 'PoP short', 
    'implied_volatility': 'impl vol'
})

# Omit rows with Volume equal to 0
df = df.loc[df['volume'] != 0]

# Calculate the max cost and max profit for buying and selling options
df['max_cost_buy'] = (df['ask'] * 100).round(2)
df['max_profit_buy'] = ((df['strike'] - df['ask']) * 100).round(2)
df['max_loss_buy'] = df['max_cost_buy']
df['max_cost_sell'] = (df['bid'] * 100).round(2)
df['max_profit_sell'] = ((df['strike'] - df['bid']) * 100).round(2)
df['max_loss_sell'] = (df['strike'].astype(float) * 100).round(2)

# Sort the DataFrame by Strike price
df = df.sort_values(['symbol','PoP short'], ascending=False)

# Write the DataFrame to a CSV file
# df.to_csv('put_option_data.csv', index=False)

# Group the DataFrame by the 'symbol' column
groups = df.groupby('symbol')

# Loop through the groups
for name, group in groups:
    # Sort the group by 'PoP short'
    group = group.sort_values('PoP short', ascending=False)
    
    # Write the group to a CSV file
    group.to_csv(f'{name}_{orderType}_option_data.csv', index=False)
