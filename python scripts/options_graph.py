import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

# Create a DataFrame from your data
data = {
    'Stock': ['JPM'],
    'Spread': ['+197.5 / -195.0'],
    'Date': ['2024-04-12'],
    'Price': [0.87],
    'Stock Price': [163.0]
}
df = pd.DataFrame(data)

# Create a Dash application
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div(children=[
    html.H1(children='Option Spread'),

    dcc.Graph(
        id='option-spread',
        figure={
            'data': [
                go.Scatter(
                    x=df['Date'],
                    y=df['Price'],
                    mode='lines+markers',
                    name='Option Price'
                ),
                go.Scatter(
                    x=df['Date'],
                    y=df['Stock Price'],
                    mode='lines+markers',
                    name='Stock Price'
                )
            ],
            'layout': go.Layout(
                xaxis={'title': 'Date'},
                yaxis={'title': 'Price'},
                title='Option Spread for JPM'
            )
        }
    )
])

# Run the application
if __name__ == '__main__':
    app.run_server(debug=True)