
from dash import Dash, html, dcc,register_page, get_asset_url
import dash_bootstrap_components as dbc
from figures import bar_chart,pie_chart,line_chart,heatmap
from pathlib import Path
import pandas as pd
from dash import dash_table
#data = Path(__file__).parent.parent.joinpath("data", "prepared6.csv")
#df = pd.read_csv(data)
data = Path(__file__).parent.parent.joinpath("data", "prepared.csv")
dataset_2016 = pd.read_csv(data)
data1 = Path(__file__).parent.parent.joinpath("data", "prepared1.csv")
dataset_2017 = pd.read_csv(data1)
data2 = Path(__file__).parent.parent.joinpath("data", "prepared2.csv")
dataset_2018 = pd.read_csv(data2)
data3 = Path(__file__).parent.parent.joinpath("data", "prepared3.csv")
dataset_2019 = pd.read_csv(data3)
data4 = Path(__file__).parent.parent.joinpath("data", "prepared4.csv")
dataset_2020 = pd.read_csv(data4)
data5 = Path(__file__).parent.parent.joinpath("data", "prepared5.csv")
dataset_2021 = pd.read_csv(data5)
data6 = Path(__file__).parent.parent.joinpath("data", "prepared6.csv")
dataset_2022 = pd.read_csv(data6)

all_data = pd.concat([dataset_2016,dataset_2017,dataset_2018,dataset_2019,dataset_2020, dataset_2021], ignore_index=True)


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
bar = bar_chart([1,9],'2015/16')
pie = pie_chart(first_value,'2015/16')
line = line_chart(['University College London'])
heat = heatmap(['The University of Greenwich'])
column_values = dataset_2022['HE provider'].unique()

# register the page in the app
register_page(__name__, name="Charts", title="Charts")

dropdown2 = dcc.Dropdown(
        id='provider-dropdown',
        options=[{'label': provider, 'value': provider} for provider in list(all_data['HE provider'].unique())],
        value=list(all_data['HE provider'].unique()[8]),  # Default selected provider
        multi= True
    )

row_ten = html.Br()

row_seven = html.Div(
    dbc.Row([dbc.Col(children=[dcc.Graph(id='line', figure = line)
            #html.Img(src=app.get_asset_url('line-chart-placeholder.png'), className="img-fluid"),
        ], width=12)])) 
row_eleven = html.Div(dbc.Row([dbc.Col(children=[dcc.Graph(id='heat', figure = heat)
            #html.Img(src=app.get_asset_url('line-chart-placeholder.png'), className="img-fluid"),
        ], width=12)]))

row_eight = html.Div(
    dbc.Row([dbc.Col(children=[dropdown2
            #html.Img(src=app.get_asset_url('line-chart-placeholder.png'), className="img-fluid"),
        ], width=12)]))

layout = dbc.Container([
    row_ten,
    row_seven,
    row_ten,
    row_eight,
    row_ten,
    row_eleven
])