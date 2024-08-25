
import robin_stocks.robinhood.options as roptions
import robin_stocks.robinhood as r
import pandas as pd
from plotly import express as px
from plotly.subplots import make_subplots

# Get the current options holdings for the user's account
email = input("Please enter your Robinhood email address: ")
login = r.login(email)


account_info = r.profiles.load_account_profile()

# Print your account information
print(account_info)

options = r.get_open_option_positions()

# Create a Pandas DataFrame to store the options data
df = pd.DataFrame(options)

# Display all stats for each option in the DataFrame
print(df)

# Create a Plotly graph with a slider to adjust the date and current price
fig = make_subplots(rows=1, cols=2, subplot_titles=("Option Value Over Time", "Current Option Value"))
fig.update_layout(height=600, width=800)

# Add a slider to adjust the date and current price in the graph
fig.add_trace(
    dict(
        type="scatter",
        x=df["expirationDate"],
        y=df["bid_price"] / 100,
        name="Bid Price",
        line=dict(color="#3f68b2"),
    ),
    secondary_y=True,
)
fig.add_trace(
    dict(
        type="scatter",
        x=df["expirationDate"],
        y=df["option_value"] / 100,
        name="Option Value",
        line=dict(color="#ffa634"),
    ),
)
fig.add_trace(
    dict(
        type="scatter",
        x=df["expirationDate"],
        y=df["adjusted_mark_price"] / 100,
        name="Mark Price",
        line=dict(color="#3f68b2"),
    ),
    secondary_y=True,
)
fig.add_slider(
    dict(
        steps=[
            dict(
                label="2023-01-01",
                value={"x": df["expiration_date"], "y": [df["bid_price"] / 100, df["option_value"] / 100, df["current_price"] / 100]},
            ),
            dict(label="2023-02-01", value={"x": df["expiration_date"], "y": [df["bid_price"] / 100, df["option_value"] / 100, df["current_price"] / 100]}),
            dict(label="2023-03-01", value={"x": df["expiration_date"], "y": [df["bid_price"] / 100, df["option_value"] / 100, df["current_price"] / 100]}),
        ],
    ),
)
fig.show()