from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from figures import bar_chart,pie_chart
from pathlib import Path
import pandas as pd
from dash import dash_table
data = Path(__file__).parent.parent.joinpath("data", "prepared6.csv")
df = pd.read_csv(data)
first_value = df.iloc[0]['HE provider']
bar = bar_chart(len(df),'2015/16')
pie = pie_chart(first_value,'2015/16')

column_values = df['HE provider'].unique()

dropdown_options = [{'label': value, 'value': value} for value in column_values]

checklist = dbc.RadioItems(id = 'checklist',
                          options = [{"label": "2015/16", "value": "2015/16"},
                                    {"label": "2016/17", "value": "2016/17"},
                                    {"label": "2017/18", "value": "2017/18"},
                                    {"label": "2018/19", "value": "2018/19"},
                                    {"label": "2019/20", "value": "2019/20"},
                                    {"label": "2020/21", "value": "2020/21"},
                                    {"label": "2021/22", "value": "2021/22"}],
                          value = ["2015/16"],
                          inline = True,
                          #type= 'radio'
)
Stats = {'Max_cycle_spaces': df["cycle_spaces"].max(),
         'Max_car_spaces': df["car_spaces"].max(),
         'Max_energy': df["energy"].max()}

Table  = dash_table.DataTable(
        id='table',
        columns=[{'name': col, 'id': col} for col in Stats.keys()],
        data=[Stats],
        style_table={'overflowX': 'auto'},
        style_header={
            'writing-mode': 'vertical-rl',  # Rotate text vertically
            'text-orientation': 'mixed',  # Ensure text orientation is applied in all browsers
            'white-space': 'nowrap'  # Prevent text wrapping
        }
    )

dropdown = dbc.Select(id = 'dropdown',
                      #options = dropdown_options,
                      value='',
                      placeholder='Select HE provider'
                      #search=True, 
                      #clearable=True
)

slider = dcc.Slider(
        id='bar-slider',
        min=1,
        max=len(df),  # Set the maximum value of the slider to the number of bars
        #step=1,
        value=5,  # Default value is the total number of bars
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
row_three = html.Div(
    dbc.Row([dbc.Col(children=[dropdown
            #html.Img(src=app.get_asset_url('line-chart-placeholder.png'), className="img-fluid"),
        ], width=4)])) 

row_six = html.Div(
    dbc.Row([dbc.Col(children=[
        checklist,
    ], width={"size": 4, "offset": 4}),
             dbc.Col(children=[
                 dcc.Graph(id='pie', figure = pie)], width=7),
             dbc.Col(children=[Table], width=5)
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
