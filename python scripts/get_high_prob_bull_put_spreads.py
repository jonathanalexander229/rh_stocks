"""
This script is designed to find bull put spread option strategies that have a high probability of profit. 
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

def try_login():
    
    try:
        # Try to login with the username
        login = r.login()
    except:
        # If login fails, prompt for password
        username = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ")
        login = r.login(username, password)
    return login

def createSpreads(df, spread_widths):
    spreads = []
    
    # If df has 1 or fewer rows, return an empty DataFrame
    if len(df) <= 1:
        return spreads
    
    # Loop through the DataFrame
    for i in range(len(df)):
        # Get the current option
        option1 = df.iloc[i]

        # Loop through all other options
        for j in range(i + 1, len(df)):
            # Get the next option
            option2 = df.iloc[j]

            # Check if the strike price of option1 is higher than the strike price of option2
            # and if the symbols are the same
            if option1['strike'] > option2['strike'] and option1['symbol'] == option2['symbol']:
                # Calculate the spread width
                current_spread_width = abs(option1['strike'] - option2['strike'])
                # Check if the spread width is in the list of given spread widths
                if current_spread_width in spread_widths:
                    # If it is, create a new row that combines the data from both options
                    spread = {
                        column: round((float(option1[column]) + float(option2[column])) / 2, 2) if column in ['PoP buy', 'PoP sell', 'impl vol', 'delta', 'rho', 'theta', 'vega']
                        else round(option1[column] - option2[column], 2) if column in ['mark', 'ask', 'bid', 'volume'] 
                        else f"-{option1[column]} / +{option2[column]}" if option1[column] != option2[column] 
                        else option1[column] 
                        for column in df.columns
                    }
                    # Add the spread width to the spread
                    spread['width'] = current_spread_width
                    # Add the new row to the list of spreads
                    spreads.append(spread)
    return spreads

def main():
    login = try_login()

    inputSymbols = input("Enter a stock symbol, separated by commas: ").split(',')
    expirationDate = input("Enter the option expiration date (YYYY-MM-DD): ")

    #Define the profitability criteria
    typeProfit = 'chance_of_profit_short'
    profitFloor = 0.65
    profitCeiling = 0.85

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
    df = pd.DataFrame(options)
    # df.to_csv('option_data_raw.csv', index=False)

    # df = pd.read_csv('option_data_raw.csv')
    # Convert the list of options to a DataFrame and select only the specified columns
    df = pd.DataFrame(options)[[
        'symbol', 
        'strike_price', 
        'expiration_date', 
        'ask_price', 
        'bid_price', 
        "adjusted_mark_price",
        'volume', 
        #'break_even_price', 
        'chance_of_profit_long', 
        'chance_of_profit_short', 
        'implied_volatility', 
        'delta', 
        'rho', 
        'theta', 
        'vega'
    ]]

    # Limit the decimal places of some columns to 2
    df[['ask_price', 'bid_price', 'adjusted_mark_price', 'strike_price']] = df[['ask_price', 'bid_price', 'adjusted_mark_price', 'strike_price']].astype(float).round(2)

    # Limit the decimal places of some columns to 4
    df[['chance_of_profit_long', 'chance_of_profit_short', 'implied_volatility']] = df[['chance_of_profit_long', 'chance_of_profit_short', 'implied_volatility']].astype(float).round(4)

    # Rename the columns
    df = df.rename(columns={ 
        'strike_price': 'strike', 
        'expiration_date': 'exp date', 
        'ask_price': 'ask', 
        'bid_price': 'bid',
        'adjusted_mark_price': 'mark', 
        'break_even_price': 'break even', 
        'chance_of_profit_long': 'PoP buy', 
        'chance_of_profit_short': 'PoP sell', 
        'implied_volatility': 'impl vol'
    })

    # Omit rows with Volume equal to 0
    df = df.loc[df['volume'] != 0]

    # Write the DataFrame to a CSV file
    df.to_csv('option_data.csv', index=False)

    # Sort the DataFrame by Strike price
    df = df.sort_values(['symbol','PoP sell'], ascending=False)

    print(df)

    df = df.sort_values('strike', ascending=False)
    # Initialize an empty list to store the spreads

    # Sort the DataFrame by strike price in descending order

    # df = df.drop(['impl vol', 'delta', 
    #     'rho', 'theta','vega','volume'], axis=1 )

    df = df.sort_values('strike', ascending=False)
    # Initialize an empty list to store the spreads
    spreads = createSpreads(df, [2.5, 5, 10])
    
    if(len(spreads) == 0):
        print("No spreads found")
        return
    
    # # Convert the list of spreads to a DataFrame
    spreads_df = pd.DataFrame(spreads)

    spreads_df[['mark', 'ask', 'bid']] = spreads_df[['mark', 'ask', 'bid']].astype(float).round(2)
    spreads_df = spreads_df.rename(columns={'mark': 'credit'})

    # # Calculate the max cost and max profit for buying and selling options
    spreads_df['max_cost'] = ((spreads_df['width'] - spreads_df['credit']) * 100).astype(float).round(2)
    spreads_df['max_profit'] = (spreads_df['credit'] * 100).astype(float).round(2)

    # Define the new order of the columns
    columns_order = ['symbol', 'strike', 'exp date', 'credit', 'max_cost', 'max_profit', 'width', 'ask', 'bid', 'volume', 'PoP buy', 'PoP sell', 'impl vol', 'delta',	'rho',	'theta', 'vega']

    # Reorder the DataFrame columns
    spreads_df = spreads_df.reindex(columns=columns_order)

    # Get the symbols from the user input and join them with an underscore
    symbols = '_'.join(inputSymbols)

    # Get the expiration date from the user input
    exp_date = expirationDate

    # Format the expiration date to remove any characters that are not allowed in file names
    exp_date = exp_date.replace('-', '_')

    # Create the CSV file name
    csv_file_name = f'{symbols}_{exp_date}_put_credit_spreads.csv'

    # Save the DataFrame to a CSV file
    spreads_df.to_csv(csv_file_name, index=False)

    # Save the DataFrame to a CSV file
    #spreads_df.to_csv('put_credit_spreads.csv', index=False)

    print(spreads_df)

if __name__ == "__main__":
    main()