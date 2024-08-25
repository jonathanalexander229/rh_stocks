"""
Options Spread Analysis Script

This script analyzes options spread trades from a CSV file containing Robinhood options data.
It performs the following tasks:

1. Loads and preprocesses options trade data from a CSV file.
2. Aggregates multi-leg orders into single spread orders.
3. Analyzes each unique stock symbol in the dataset:
   - Identifies and pairs opening and closing spread orders.
   - Handles partial closings of spread orders.
   - Finds unpaired (open) spread orders.
   - Searches for potential individual leg closings for unpaired spread orders.
4. Generates a detailed report for each symbol, including:
   - Paired spread orders with their closing details.
   - Unpaired spread orders with potential individual leg closings.
   - Summary statistics (total opened, closed, and remaining open quantities).

The script provides insights into the status of options spread trades, helping to identify
open positions, partial closings, and potential leg-by-leg closings of spread orders.

Usage:
Ensure the input CSV file path is correctly specified before running the script.
The script will output the analysis results to the console.

Note: This script is designed for use with Robinhood options data and may require
modifications for use with data from other sources.
"""

import robin_stocks.robinhood as r
import pandas as pd

# Load your spreadsheet
df = pd.read_csv('../output/options_output.csv')

# Convert 'order_created_at' to datetime
df['order_created_at'] = pd.to_datetime(df['order_created_at'])
df['order_created_at'] = df['order_created_at'].dt.strftime('%Y-%m-%d %H:%M:%S.%f').str[:-4]

# Select only the columns we want
df = df[['order_created_at', 'chain_symbol', 'expiration_date', 
         'strike_price', 'option_type', 'direction', 'order_quantity', 
         'order_type', 'opening_strategy', 'closing_strategy', 'price', 'processed_quantity']]

# Group by 'order_created_at' and aggregate
aggregated_df = df.groupby('order_created_at').agg({
    'chain_symbol': 'first',
    'expiration_date': 'first',
    'strike_price': lambda x: '/'.join(map(str, sorted(x, key=abs, reverse=True))),
    'option_type': 'first',
    'direction': 'first',
    'order_quantity': 'first',
    'order_type': 'first',
    'opening_strategy': 'first',
    'closing_strategy': 'first',
    'price': 'first',
    'processed_quantity': 'first'
}).reset_index()

# Function to extract strike prices from the strike_price string
def extract_strikes(strike_string):
    return [float(s.strip('+-')) for s in strike_string.split('/')]

# Get all unique chain symbols
unique_symbols = aggregated_df['chain_symbol'].unique()

# Analyze each symbol
for symbol in unique_symbols:
    print(f"\n--- Analysis for {symbol} ---")
    
    # Filter for the current symbol's spread orders
    symbol_spreads = aggregated_df[
        (aggregated_df['chain_symbol'] == symbol) & 
        (aggregated_df['opening_strategy'].str.contains('spread|iron', case=False, na=False))
    ]
    
    # Find paired and unpaired opening orders
    paired_orders = []
    unpaired_opens = []
    for _, order in symbol_spreads.iterrows():
        remaining_quantity = order['processed_quantity']
        closing_orders = aggregated_df[
            (aggregated_df['chain_symbol'] == symbol) &
            (aggregated_df['closing_strategy'].str.contains('spread|iron', case=False, na=False)) &
            (aggregated_df['expiration_date'] == order['expiration_date']) &
            (aggregated_df['strike_price'] == order['strike_price'])
        ]
        
        matching_closes = []
        for _, close in closing_orders.iterrows():
            if remaining_quantity > 0:
                matched_quantity = min(remaining_quantity, close['processed_quantity'])
                matching_closes.append((close, matched_quantity))
                remaining_quantity -= matched_quantity
        
        if matching_closes:
            paired_orders.append((order, matching_closes, remaining_quantity))
        if remaining_quantity > 0:
            unpaired_opens.append((order, remaining_quantity))

    # Process paired orders
    print(f"\nPaired orders: {len(paired_orders)}")
    for i, (open_order, close_orders, remaining) in enumerate(paired_orders):
        print(f"\nPair {i+1}:")
        print(f"Open: {open_order['order_created_at']} - {open_order['strike_price']} - {open_order['opening_strategy']} - Quantity: {open_order['processed_quantity']}")
        total_closed = sum(close_order[1] for close_order in close_orders)
        print(f"Closed: {total_closed} out of {open_order['processed_quantity']}")
        for j, (close_order, matched_quantity) in enumerate(close_orders):
            print(f"  Close {j+1}: {close_order['order_created_at']} - {close_order['strike_price']} - {close_order['closing_strategy']} - Matched Quantity: {matched_quantity}")
        if remaining > 0:
            print(f"Remaining open quantity: {remaining}")

    # Process unpaired opening orders
    print(f"\nUnpaired opening orders: {len(unpaired_opens)}")
    for i, (order, remaining_quantity) in enumerate(unpaired_opens):
        print(f"{i+1}: {order['order_created_at']} - Exp: {order['expiration_date']} - {order['strike_price']} - {order['opening_strategy']} - Remaining Quantity: {remaining_quantity}")

    # Calculate total opened and closed quantities
    total_opened = sum(order['processed_quantity'] for order, _, _ in paired_orders) + sum(remaining_quantity for _, remaining_quantity in unpaired_opens)
    total_closed = sum(sum(close_order[1] for close_order in close_orders) for _, close_orders, _ in paired_orders)

    print(f"\nTotal opened quantity: {total_opened}")
    print(f"Total closed quantity: {total_closed}")
    print(f"Remaining open quantity: {total_opened - total_closed}")