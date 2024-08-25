import robin_stocks.robinhood as r
import pandas as pd

# Load and preprocess the options data
df = pd.read_csv('../output/options_output.csv')
df['order_created_at'] = pd.to_datetime(df['order_created_at'])
df['order_created_at'] = df['order_created_at'].dt.strftime('%Y-%m-%d %H:%M:%S.%f').str[:-4]
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

# Prepare a list to collect results for CSV
results = []

# Get all unique chain symbols
unique_symbols = aggregated_df['chain_symbol'].unique()

# Analyze each symbol
for symbol in unique_symbols:
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

    # Process unpaired opening orders
    for i, (order, remaining_quantity) in enumerate(unpaired_opens):
        strikes = extract_strikes(order['strike_price'])
        
        potential_closes = aggregated_df[
            (aggregated_df['closing_strategy'].notna()) &
            (~aggregated_df['closing_strategy'].str.contains('spread|iron', case=False, na=False)) &  # Exclude spread closing orders
            (aggregated_df['expiration_date'] == order['expiration_date']) &
            (aggregated_df['chain_symbol'] == symbol) &
            (aggregated_df['strike_price'].apply(lambda x: any(s in strikes for s in extract_strikes(x))))
        ]
        
        # Mark potential closing orders in the original DataFrame
        for _, close in potential_closes.iterrows():
            close['potential_closing_order'] = 'Yes'  # Add a new column to denote potential closing orders
            results.append(close)

    # Append all spread orders to results
    for _, order in symbol_spreads.iterrows():
        order['potential_closing_order'] = 'No'  # Mark as not a potential closing order
        results.append(order)

    # Collect all other orders for the symbol
    all_other_orders = aggregated_df[
        (aggregated_df['chain_symbol'] == symbol) &
        (~aggregated_df['opening_strategy'].str.contains('spread|iron', case=False, na=False)) &
        (~aggregated_df['closing_strategy'].str.contains('spread|iron', case=False, na=False))
    ]
    
    for _, order in all_other_orders.iterrows():
        order['potential_closing_order'] = 'No'  # Mark as not a potential closing order
        results.append(order)

# Create a DataFrame from the results
results_df = pd.DataFrame(results)

# Save the results to a CSV file
results_df.to_csv('../output/options_analysis_results.csv', index=False)

print("Analysis results saved to options_analysis_results.csv")