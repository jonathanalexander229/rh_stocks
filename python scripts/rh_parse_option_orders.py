import robin_stocks.robinhood as r
import pandas as pd

def load_and_process_data(file_path):
    """Load the CSV file and process the data."""
    # Load your spreadsheet
    df = pd.read_csv(file_path)

    # Convert 'order_created_at' to datetime
    df['order_created_at'] = pd.to_datetime(df['order_created_at'])
    df['order_created_at'] = df['order_created_at'].dt.strftime('%Y-%m-%d %H:%M:%S.%f').str[:-4]

    # Select only the columns we want
    df = df[['order_created_at', 'chain_symbol', 'expiration_date', 
             'strike_price', 'option_type', 'direction', 'order_quantity', 
             'order_type', 'opening_strategy', 'closing_strategy', 'price', 'processed_quantity']]
    
    return df

def aggregate_and_calculate_cost(df):
    """Aggregate the DataFrame and calculate the total option cost."""
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

    # Sort the DataFrame
    aggregated_df = aggregated_df.sort_values(by=['chain_symbol', 'expiration_date', 'strike_price'])

    # Calculate cost
    aggregated_df['cost'] = aggregated_df['price'] * aggregated_df['processed_quantity'] * 100

    # Adjust the cost based on the direction
    aggregated_df['cost'] = aggregated_df.apply(
        lambda x: -x['cost'] if x['direction'] == 'debit' else x['cost'],
        axis=1
    )      

    return aggregated_df

def fetch_events_for_symbols(aggregated_df):
    """Fetch events for each unique chain symbol and calculate total cash amount."""
    unique_symbols = aggregated_df['chain_symbol'].unique()
    total_cash_amount = 0  # Initialize total cash amount

    for symbol in unique_symbols:
        events = r.get_events(symbol)  # Fetch events for the symbol
        for event in events:
            if event['direction'] == 'credit':
                total_cash_amount += float(event['total_cash_amount'])  # Add for exercise
            elif event['direction'] == 'debit':
                total_cash_amount -= float(event['total_cash_amount'])  # Subtract for assignment

    return total_cash_amount  # Return the total cash amount

def main():
    """Main function to orchestrate the workflow."""
    email = input("Please enter your Robinhood email address: ")
    login = r.login(email)  # Uncomment this line to perform login

    file_path = '../output/options_output.csv'
    df = load_and_process_data(file_path)
    
    aggregated_df = aggregate_and_calculate_cost(df)
    
    # Fetch events for each unique chain symbol and calculate total cash amount
    option_event_total = fetch_events_for_symbols(aggregated_df)

    total_option_cost = aggregated_df['cost'].sum() + option_event_total
    print(f"Total option cost: ${total_option_cost:.2f}")

    # Save the results
    aggregated_df.to_csv('../output/options_orders_parsed.csv', index=False)

if __name__ == "__main__":
    main()