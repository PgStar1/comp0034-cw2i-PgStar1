
from dash import Dash, html, dcc,register_page, get_asset_url,callback, Input, Output
import dash_bootstrap_components as dbc
from figures import bar_chart,pie_chart,line_chart,heatmap
from pathlib import Path
import pandas as pd
from dash import dash_table

# I UPLOADED  ALL MY DATASETS AND CONCATENATED THEM.
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
bar = bar_chart([1,9],'2020/21')
pie = pie_chart(first_value,'2015/16')
line = line_chart(['University College London'])
heat = heatmap(['The University of Greenwich'])
column_values = dataset_2022['HE provider'].unique()

#CREATED THE NAVIGATION BAR TO USE IT TO RETURN TO THE HOME PAGE
navbar2 = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Go to home page", href = '/home'))],
                color="dark",
                dark=True,
                style={'position': 'absolute', 'top': 0, 'left': 0, 'right': 0, 'z-index': 1000}
)
#CREATED RADIOITEMS FOR THE APP TO ALLOW INTERACTION IN THE APP
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
                          style={
                             'color': 'teal',
                             'border-radius':'5px',
                             'padding':'10px 40px',
                             'border':'none',
                             'cursor':'pointer'}
)

checklist1 = dbc.RadioItems(id = 'checklist1',
                          options = [{"label": "2015/16", "value": "2015/16"},
                                    {"label": "2016/17", "value": "2016/17"},
                                    {"label": "2017/18", "value": "2017/18"},
                                    {"label": "2018/19", "value": "2018/19"},
                                    {"label": "2019/20", "value": "2019/20"},
                                    {"label": "2020/21", "value": "2020/21"},
                                    {"label": "2021/22", "value": "2021/22"}],
                          value = ["2020/21"],
                          inline = True,
                          style={
                             'color': 'teal',
                             'border-radius':'5px',
                             'padding':'10px 40px',
                             'border':'none',
                             'cursor':'pointer'}
)

range_slider = dcc.RangeSlider(
            id="he-provider-slider",
            min=1,
            max=len(all_data['HE provider'].unique()),
            value=[89, 97],
            tooltip={"placement": "bottom"},
        )

dropdown = dcc.Dropdown(id = 'dropdown',
                      #options = dropdown_options,
                      value='',
                      placeholder='Select University',
)

#CREATED LAYOUT FOR THE APP TO FILL DIFFERENT ROWS 

row_one = html.Div(
    dbc.Row([dbc.Col(html.Div("Adjust the range to select a number of universities to display:", style={'font-weight': 'bold'}))])
)

row_eleven = html.Div(
    dbc.Row([dbc.Col(html.Div("Select a year to display the bar charts for:", style={'font-weight': 'bold'}))])
)

row_five = html.Div(
    dbc.Row([dbc.Col(children=[
            dcc.Graph(id='bar', figure = bar)
        ], width=12),
             ])
    )

row_two = html.Div(
    dbc.Row([dbc.Col(children=[range_slider
        ], width=12),])
    ) 

row_21 = html.Div(
    dbc.Row([dbc.Col(html.H1("Parking Spaces Page"), width=12),]),
    ) 

row_22 = html.Div(
    dbc.Row([dbc.Col(html.P("Welcome to the parking spaces page!"), width=12)])
    ) 

row_24 = html.Div(
    dbc.Row([dbc.Col(html.P("This Page contains two charts, one is the bar graph and the other is the pie chart. Explore!"), width=12)])
    ) 

row_three = html.Div(
    dbc.Row([dbc.Col(children=[dropdown
        ], width=6),
             dbc.Col(children=[
                 checklist,
    ], width =6)]))

row_seven = html.Div(dbc.Row([dbc.Col(children=[checklist1
        ], width=12)]))

row_ten = html.Br()

row_twelve = html.Div(
    dbc.Row([dbc.Col(children=[],width=3),dbc.Col(html.Div("Select the university and a year to display the pie chart for:", style={'font-weight': 'bold'}))])
)

row_six = html.Div(
    dbc.Row([dbc.Col(children=[],width=1),dbc.Col(children=[
        dcc.Graph(id='pie', figure = pie)], width=10
        ),
        dbc.Col(children=[],width=1)])
    )

row_20 = html.Div(
    dbc.Row([dbc.Col(children=[navbar2],width=1)])
    )

layout = dbc.Container([
    row_ten,
    row_ten,
    row_ten,
    row_21,
    row_22,row_24,
    row_eleven,
    row_seven,
    row_ten,
    row_one,
    row_two,
    row_five,
    row_ten,
    row_ten,
    row_twelve,
    row_ten,
    row_three,
    row_six,
    row_20
],fluid=True)

@callback(
    Output('dropdown', 'options'),
    [Input('checklist', 'value')],#allow_duplicates=True
)
def update_provider_dropdown(selected_years):
    providers = set()
    if isinstance(selected_years, list):
        selected_years = selected_years[0]
    providers.update(year_datasets[selected_years]['HE provider'].unique())
    options = [{'label': provider, 'value': provider} for provider in sorted(providers)]#sorted(providers)]
    return options

@callback(
    Output(component_id = 'pie',component_property='figure'),
    [Input(component_id = 'dropdown',component_property='value'),
    Input(component_id = 'checklist',component_property = 'value')],allow_duplicates=True
)

def update_pie_chart(provider,num):
    
    figure = pie_chart(provider,num)
    return figure

@callback(
    Output(component_id = 'bar',component_property='figure'),
    [Input(component_id = 'he-provider-slider',component_property='value'),
    Input(component_id = 'checklist1',component_property = 'value')],
    allow_duplicates=True
    
)

def update_bar_chart(selected_value,selected_year):
    figure = bar_chart(selected_value,selected_year)
    return figure