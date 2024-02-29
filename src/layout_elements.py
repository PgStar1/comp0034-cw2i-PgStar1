from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from figures import bar_chart,pie_chart
from pathlib import Path
import pandas as pd

data = Path(__file__).parent.parent.joinpath("data", "prepared6.csv")
df = pd.read_csv(data)
first_value = df.iloc[0]['HE provider']
bar = bar_chart(len(df))
pie = pie_chart(first_value)

column_values = df['HE provider'].unique()

dropdown_options = [{'label': value, 'value': value} for value in column_values]


dropdown = dbc.Select(id = 'dropdown',
                      options = dropdown_options,
                      value='',
                      #search=True, 
                      #clearable=True
)

slider = dcc.Slider(
        id='bar-slider',
        min=1,
        max=len(df),  # Set the maximum value of the slider to the number of bars
        #step=1,
        value=len(df),  # Default value is the total number of bars
        #marks={i: str(i) for i in range(1, len(df) + 1)}  # Mark every integer from 1 to the number of bars
        #marks = {} # Dictionary
    )
row_one = html.Div(
    dbc.Row([
        dbc.Col([html.H1("Paralympics Dashboard"), html.P(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent congue luctus elit nec gravida. Fusce "
            "efficitur posuere metus posuere malesuada. ")
                 ], width=12),
    ]),
)
row_four = html.Div(
    dbc.Row([
        dbc.Col(children=[
            dbc.Input(id='search-input', type='text', placeholder='Enter search term'),
            html.Div(id='search-output')
        ], width=3),
    ])
)

row_five = html.Div(
    dbc.Row([dbc.Col(children=[
            dcc.Graph(id='bar', figure = bar)
            #html.Img(src=app.get_asset_url('line-chart-placeholder.png'), className="img-fluid"),
        ], width=12),
             ])
    )
row_two = html.Div(
    dbc.Row([dbc.Col(children=[slider
            #html.Img(src=app.get_asset_url('line-chart-placeholder.png'), className="img-fluid"),
        ], width=12),
             ])
    )
row_six = html.Div(
    dbc.Row([dbc.Col(children=[dropdown
            #html.Img(src=app.get_asset_url('line-chart-placeholder.png'), className="img-fluid"),
        ], width=4),
             dbc.Col(children=[
                 dcc.Graph(id='pie', figure = pie)], width=8),
             ])
    )
"""row_six = html.Div([
    dcc.Dropdown(
        id='category-filter',
        options=[],
        value='',  # Default value
        searchable=True,  # Enable search functionality
        clearable=True
    ),
    dcc.Graph(id='pie',figure = pie)
])"""
