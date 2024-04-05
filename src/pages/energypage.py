
from dash import Dash, html, dcc,register_page, get_asset_url,callback, Input, Output
import dash_bootstrap_components as dbc
from figures import line_chart,heatmap
from pathlib import Path
import pandas as pd

#UPLOADED ALL MY DATASETS AND CONCATENATED THEM
try:
    
    data = Path(__file__).parent.parent.joinpath("data", "prepared.csv")
    dataset_2016 = pd.read_csv(data)
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("Error:", e)
dataset_2016['Year'] = 2016
data1 = Path(__file__).parent.parent.joinpath("data", "prepared1.csv")
dataset_2017 = pd.read_csv(data1)
dataset_2017['Year'] = 2017
data2 = Path(__file__).parent.parent.joinpath("data", "prepared2.csv")
dataset_2018 = pd.read_csv(data2)
dataset_2018['Year'] = 2018
data3 = Path(__file__).parent.parent.joinpath("data", "prepared3.csv")
dataset_2019 = pd.read_csv(data3)
dataset_2019['Year'] = 2019
data4 = Path(__file__).parent.parent.joinpath("data", "prepared4.csv")
dataset_2020 = pd.read_csv(data4)
dataset_2020['Year'] = 2020
data5 = Path(__file__).parent.parent.joinpath("data", "prepared5.csv")
dataset_2021 = pd.read_csv(data5)
dataset_2021['Year'] = 2021
data6 = Path(__file__).parent.parent.joinpath("data", "prepared6.csv")
dataset_2022 = pd.read_csv(data6)
dataset_2022['Year'] = 2022

all_data = pd.concat([dataset_2016,dataset_2017,dataset_2018,dataset_2019,dataset_2020, dataset_2021,dataset_2022], ignore_index=True)


year_datasets = {
    '2015/16': dataset_2016,
    '2016/17': dataset_2017,
    '2017/18': dataset_2018,
    '2018/19': dataset_2019,
    '2019/20': dataset_2020,
    '2020/21': dataset_2021,
    '2021/22': dataset_2022
}
first_value = dataset_2022.iloc[8]['HE provider']
line = line_chart(['The University of Greenwich'])
heat = heatmap(['The University of Greenwich'])
column_values = dataset_2022['HE provider'].unique()

# CREATED DIFFERENT FUNCTIONALITIES FOR THIS PAGE TO ALLOW INTERACTION WITH THE USER

dropdown2 = dcc.Dropdown(
        id='provider-dropdown',
        options=[{'label': provider, 'value': provider} for provider in list(all_data['HE provider'].unique())],
        value=['The University of Greenwich'],  # Default selected provider
        multi= True
    )

navbar2 = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Go to home page", href = '/home'))],
                color="dark",
                dark=True,
                style={'position': 'absolute', 'top': 0, 'left': 0, 'right': 0, 'z-index': 1000}
)

#CREATED DIFFERENT LAYOUTS FOR THE PAGE

row_ten = html.Br()

row_20 = html.Div(
    dbc.Row([dbc.Col(children=[navbar2],width=1)])
    )

row_seven = html.Div(
    dbc.Row([dbc.Col(children=[dcc.Graph(id='line', figure = line)
        ], width=12)])) 
row_eleven = html.Div(dbc.Row([dbc.Col(children=[dcc.Graph(id='heat', figure = heat)
        ], width=12)]))

row_eight = html.Div(
    dbc.Row([dbc.Col(children=[dropdown2
        ], width=12)]))

row_21 = html.Div(
    dbc.Row([dbc.Col(html.H1("Renewable Energy Page"), width=12),])
    ) 

row_22 = html.Div(
    dbc.Row([dbc.Col(html.P("Welcome to the Renewable Energy page!This Page contains two charts, one is the heat map the other is the line chart.Explore!"), width=12)])
    )
row_24 = html.Div(
    dbc.Row([dbc.Col(html.P("This Page contains two charts, one is the heat map and the other is the line chart. Explore!"), width=12)])
    ) 
row_23 = html.Div(
    dbc.Row([dbc.Col(html.Div("Select universities to display the heat map and line chart below:", style={'font-weight': 'bold'}))])
)

#LAYOUT FOR THE APP SO THAT IT IS RESPONSIVE BASED ON THE DEVICE
layout = dbc.Container([
    row_ten,
    row_ten,
    row_ten,
    row_21,
    row_ten,
    row_22,row_24,row_ten,row_23,
    row_eight,
    row_seven,
    row_ten,
    row_ten,
    row_eleven,
    row_20
])

@callback(
    Output(component_id='line', component_property='figure'),
    Output(component_id='heat', component_property='figure'),
    [Input(component_id='provider-dropdown', component_property='value')],allow_duplicate=True
)
def update_line_chart(selected_provider):
    figure = line_chart(selected_provider)
    figure1 = heatmap(selected_provider)
    return figure,figure1