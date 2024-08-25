
"""
This script is used to fetch and process option orders from Robinhood.

It prompts the user for their Robinhood username and password, and uses these credentials to log in to Robinhood.

After logging in, it fetches all option orders and converts the list of orders (which are represented as dictionaries) to a pandas DataFrame.

It then filters out any cancelled orders from the DataFrame.

The resulting DataFrame contains the details of all non-cancelled option orders.

Dependencies:
- robin_stocks: a Python library that interacts with the Robinhood API
- pandas: a Python library for data manipulation and analysis
- getpass: a Python library for securely entering passwords
"""
import os
import robin_stocks.robinhood as r
import pandas as pd
import datetime
import getpass

# username = input("Enter your username: ")
# password = getpass.getpass("Enter your password: ")
# login = r.login(username, password)


try:
    # Try to login with the username
    login = r.login()
except:
    # If login fails, prompt for password
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    login = r.login(username, password)

# Rest of your code...
# Get all option orders
all_orders = r.orders.get_all_option_orders()

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(all_orders)

df = df[df['state'] != 'cancelled']

legs_data = df['legs'].apply(pd.Series)

# Extract the 'expiration_date', 'strike_price', and 'option_type' from the 'legs' list
df['expiration_date'] = df['legs'].apply(lambda x: x[0]['expiration_date'] if x else None)
df['strike_price'] = df['legs'].apply(lambda x: '/'.join([f"{float(leg['strike_price']):.2f}" for leg in x]) if x else None)
df['option_type'] = df['legs'].apply(lambda x: '/'.join([leg['option_type'] for leg in x]) if x else None)
df['position_effect'] = df['legs'].apply(lambda x: x[0]['position_effect'] if x else None)
df['option'] = df['legs'].apply(lambda x: x[0]['option'][-13:][:-1] if x else None)


#Specify the columns to drop
columns_to_drop = ['net_amount','estimated_total_net_amount','premium','regulatory_fees',
            'time_in_force','form_source','client_bid_at_submission','client_ask_at_submission',
            'client_time_at_submission','trigger','type','updated_at','chain_id','quantity',
            'pending_quantity','response_category','stop_price','account_number',
            'cancel_url', 'canceled_quantity', 'ref_id', 'legs', 'state', 'id',
            'estimated_total_net_amount_direction']

# Drop the specified columns
df = df.drop(columns=columns_to_drop)

df = df[['chain_symbol'] + [col for col in df.columns if col != 'chain_symbol']]

# Convert 'created_at' to datetime format
df['created_at'] = pd.to_datetime(df['created_at'])


df = df[df['created_at'] > '2024-03-25']

df['created_at'] = df['created_at'].dt.date


#Specify the new column order
new_order = ['chain_symbol', 'created_at', 'option', 'position_effect', 'expiration_date', 'strike_price', 'price', 'processed_quantity', 'opening_strategy', 
            'direction', 'processed_premium', 'option_type', 'closing_strategy', 'net_amount_direction', 'average_net_premium_paid']
#Reorder the columns
df = df.reindex(columns=new_order)


# Specify the column abbreviations
column_abbreviations = {
    'chain_symbol': 'symbol',
    'average_net_premium_paid': 'avg_net_premium',
    'processed_premium': 'premium',
    'processed_quantity': 'quantity',
    # Add more abbreviations as needed
}


# Rename the columns
df = df.rename(columns=column_abbreviations)


# Display the DataFrame
df = df.sort_values(['option'])

# Iterate over each column in the DataFrame

for col in df.columns:
    if df[col].apply(lambda x: isinstance(x, datetime.date)).any():
        continue
    try:
        df[col] = df[col].astype(float).round(2)
    except ValueError:
        pass
# Save the DataFrame to a CSV file

# Count the occurrences of each 'option' value
option_counts = df['option'].value_counts()

# Get the 'option' values that appear only once
open_options = option_counts[option_counts == 1].index

# Filter the DataFrame to only include rows with 'option' values that appear only once
df = df[df['option'].isin(open_options)]
# Filter the DataFrame to only include rows where 'position_effect' is not 'close'
df = df[df['position_effect'] != 'close']

df.to_csv('recent_option_orders.csv', index=False)
