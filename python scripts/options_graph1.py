import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

# Create a Dash application
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1('Option P/L Chart'),
    dcc.Slider(
        id='date-slider',
        min=0,
        max=365,  # Set the maximum value to 365 days
        value=0,
        marks={i: str(i) for i in range(0, 366, 30)},
        step=1
    ),
    dcc.Slider(
        id='stock-price-slider',
        min=100,  # Set the minimum stock price
        max=200,  # Set the maximum stock price
        value=150,  # Set the initial stock price
        step=1
    ),
    dcc.Graph(id='pl-chart')
])
# Define the callback
@app.callback(
    Output('pl-chart', 'figure'),
    [Input('date-slider', 'value'), Input('stock-price-slider', 'value')]
)
def update_graph(selected_date, selected_stock_price):
    # Manually enter the values
    original_price = 0.87
    theta_effect = -0.14
    delta_effect = -0.32
    original_stock_price = 163.0

    # Calculate the new option price and P/L
    option_price = original_price + theta_effect * selected_date + delta_effect * (selected_stock_price - original_stock_price)
    pl = option_price - original_price

    return {
        'data': [go.Scatter(
            x=[selected_stock_price],
            y=[pl],
            mode='markers',
            name='P/L'
        )],
        'layout': go.Layout(
            xaxis={'title': 'Stock Price'},
            yaxis={'title': 'P/L'},
            title='Option P/L Chart'
        )
    }
# Run the application
if __name__ == '__main__':
    app.run_server(debug=True, port=8051)