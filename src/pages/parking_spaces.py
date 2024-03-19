
from dash import Dash, html, dcc,register_page, get_asset_url,callback, Input, Output
import dash_bootstrap_components as dbc
from figures import bar_chart,pie_chart,line_chart,heatmap
from pathlib import Path
import pandas as pd
from dash import dash_table
#data = Path(__file__).parent.parent.joinpath("data", "prepared6.csv")
#df = pd.read_csv(data)
try:
    data = Path(__file__).parent.parent.joinpath("data", "prepared.csv")
    dataset_2016 = pd.read_csv(data)
    print("File successfully loadedee.")
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

#register_page(__name__, name="Parking", title="parking", path="/c")

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
                          style={#'background-color': '#2ecc71',
                             'color': 'teal',
                             'border-radius':'5px',
                             'padding':'10px 40px',
                             'border':'none',
                             'cursor':'pointer'}
                          #type= 'radio'
)

range_slider = dcc.RangeSlider(
            id="he-provider-slider",
            min=1,
            max=len(all_data['HE provider'].unique()),
            value=[89, 97],  # Default to show all providers
            #marks={str(i): i for i in range(min, max + 1)},
            tooltip={"placement": "bottom"},
        )

dropdown = dcc.Dropdown(id = 'dropdown',
                      #options = dropdown_options,
                      value='',
                      placeholder='Select HE provider',
                      #search=True, 
                      #clearable=True
)

row_five = html.Div(
    dbc.Row([dbc.Col(children=[
            dcc.Graph(id='bar', figure = bar)
            #html.Img(src=app.get_asset_url('line-chart-placeholder.png'), className="img-fluid"),
        ], width=12),
             ])
    )

row_two = html.Div(
    dbc.Row([dbc.Col(children=[range_slider
            #html.Img(src=app.get_asset_url('line-chart-placeholder.png'), className="img-fluid"),
        ], width=12),])
    ) 

row_three = html.Div(
    dbc.Row([dbc.Col(children=[dropdown
            #html.Img(src=app.get_asset_url('line-chart-placeholder.png'), className="img-fluid"),
        ], width=6),
             dbc.Col(children=[
                 checklist,
    ], width =5)]))

row_ten = html.Br()

row_six = html.Div(
    dbc.Row([dbc.Col(children=[],width=1),dbc.Col(children=[
        dcc.Graph(id='pie', figure = pie)], width=10
        ),#{"size": 4, "offset": 4}),
             #dbc.Col(children=[Table], width=5)
        dbc.Col(children=[],width=1)])
    )

layout = dbc.Container([
    row_ten,
    row_five,
    row_ten,
    row_two,
    row_ten,
    row_three,
    row_six
])

@callback(
    Output('dropdown', 'options'),
    [Input('checklist', 'value')],allow_duplicate=True
)
def update_provider_dropdown(selected_years):
    providers = set()
    #for year in selected_years:
    if isinstance(selected_years, list):
        selected_years = selected_years[0]
    providers.update(year_datasets[selected_years]['HE provider'].unique())
    options = [{'label': provider, 'value': provider} for provider in sorted(providers)]#sorted(providers)]
    return options

@callback(
    Output(component_id = 'pie',component_property='figure'),
    [Input(component_id = 'dropdown',component_property='value'),
    Input(component_id = 'checklist',component_property = 'value')],allow_duplicate=True
)

def update_pie_chart(provider,num):
    #years = ['2016','2017','2018','2019','2020','2021']
    #if num in years:
    #df = pd.read_csv('your_data.csv')
    
    figure = pie_chart(provider,num)
    return figure

@callback(
    Output(component_id = 'bar',component_property='figure'),
    [Input(component_id = 'he-provider-slider',component_property='value'),
    #Input(component_id = 'search-input',component_property='value'),
    Input(component_id = 'checklist',component_property = 'value')],allow_duplicate=True
    
)

def update_bar_chart(selected_value,selected_year):
    #df = pd.read_csv('your_data.csv')
    #filtered_df = df[df['HE provider'].str.contains(search_term, case=False)] if search_term else df
    figure = bar_chart(selected_value,selected_year)
    return figure