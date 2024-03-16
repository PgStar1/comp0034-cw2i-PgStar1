# This version is after the final activity in week 7
from dash import Dash, html, dcc,Output, Input
import dash_bootstrap_components as dbc
from layout_elements import row_eleven,row_one,row_ten,row_four,row_nine,row_five,row_six,row_two,row_three,row_seven,row_eight
from figures import pie_chart,bar_chart,table_stats,line_chart,heatmap
import pandas as pd
import plotly.graph_objs as go
from pathlib import Path

# Variable that contains the external_stylesheet to use, in this case Bootstrap styling from dash bootstrap
# components (dbc)
external_stylesheets = [dbc.themes.BOOTSTRAP]

# Define a variable that contains the meta tags
meta_tags = [
    {"name": "viewport", "content": "width=device-width, initial-scale=1"},
]


# Pass the stylesheet variable to the Dash app constructor
app = Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)

# Variables that define the three rows of the layout

# Add an HTML layout to the Dash app.
# The layout is wrapped in a DBC Container()
app.layout = dbc.Container([
    row_ten,row_one,row_ten,row_nine,row_seven,row_ten,row_eight,row_ten,row_eleven,row_ten,row_four,row_ten,row_five,row_ten,row_two,row_ten,row_three,
    row_six
])


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

year_datasets = {
    '2015/16': dataset_2016,
    '2016/17': dataset_2017,
    '2017/18': dataset_2018,
    '2018/19': dataset_2019,
    '2019/20': dataset_2020,
    '2020/21': dataset_2021,
    '2021/22': dataset_2022
}

@app.callback(
    Output('dropdown', 'options'),
    [Input('checklist', 'value')]
)
def update_provider_dropdown(selected_years):
    providers = set()
    #for year in selected_years:
    if isinstance(selected_years, list):
        selected_years = selected_years[0]
    providers.update(year_datasets[selected_years]['HE provider'].unique())
    options = [{'label': provider, 'value': provider} for provider in sorted(providers)]#sorted(providers)]
    return options


@app.callback(
    Output(component_id = 'pie',component_property='figure'),
    [Input(component_id = 'dropdown',component_property='value'),
    Input(component_id = 'checklist',component_property = 'value')]
)

def update_pie_chart(provider,num):
    #years = ['2016','2017','2018','2019','2020','2021']
    #if num in years:
    #df = pd.read_csv('your_data.csv')
    
    figure = pie_chart(provider,num)
    return figure

@app.callback(
    Output(component_id = 'bar',component_property='figure'),
    [Input(component_id = 'he-provider-slider',component_property='value'),
    Input(component_id = 'search-input',component_property='value'),
    Input(component_id = 'checklist',component_property = 'value')]
    
)

def update_bar_chart(selected_value,search_term,selected_year):
    #df = pd.read_csv('your_data.csv')
    #filtered_df = df[df['HE provider'].str.contains(search_term, case=False)] if search_term else df
    figure = bar_chart(selected_value,selected_year)
    return figure
    
    """figure = bar_chart(num_bars)
    filtered_df = df[df['HE provider'].str.contains(search_term, case=False)] if search_term else df
    if not filtered_df.empty:
        for col in filtered_df.columns[1:3]:  # Skip the 'HE provider' column
            figure.add_trace(go.Bar(
                x=filtered_df['HE provider'],
                y=filtered_df[col],
                name=col
            ))
    figure.update_layout(barmode='group', title=f'Bar Chart for {search_term}')
    return figure
    # Filter data based on search term (if provided)
    
    df = year_datasets[selected_year]
    
    if not search_term:
        return bar_chart(selected_value)  # Include all data if no search term
    else:
        filtered_df = df[df['HE provider'].str.contains(search_term, case=False)]
        # Disable slider when searching (optional)
        selected_value = 'disabled'

    # Create an empty figure (clear existing traces)
    fig = go.Figure()

    # Check if any data remains after filtering
    if len(filtered_df) > 0:
        # Add trace for the filtered data (only if results exist)
        fig.add_trace(go.Bar(x=filtered_df['HE provider'], y=filtered_df['cycle_spaces']))
        fig.add_trace(go.Bar(x=filtered_df['HE provider'], y=filtered_df['car_spaces']))

    # Update layout (optional)
    fig.update_layout(title='Bar Chart - HE Provider Search')

    return fig, selected_value  # Return both figure and slider value"""

@app.callback(
    Output(component_id = 'table',component_property='figure'),
    [Input(component_id = 'checklist',component_property = 'value')]
    
)

def update_table(selected_value,selected_year):
    #df = pd.read_csv('your_data.csv')
    #filtered_df = df[df['HE provider'].str.contains(search_term, case=False)] if search_term else df
    figure = table_stats(selected_value,selected_year)
    return figure

@app.callback(
    Output(component_id='line', component_property='figure'),
    Output(component_id='heat', component_property='figure'),
    [Input(component_id='provider-dropdown', component_property='value')]
)
def update_line_chart(selected_provider):
    figure = line_chart(selected_provider)
    figure1 = heatmap(selected_provider)#,selected_provider)
    return figure,figure1

"""@app.callback(
    Output(component_id='heat', component_property='figure'),
    [Input(component_id='provider-dropdown', component_property='value')]
     #Input(component_id='provider-dropdown', component_property='value')]
)
def update_heat_chart(selected_provider):#,selected_provider):
    figure = heatmap(selected_provider)#,selected_provider)
    return figure"""

# Run the Dash app
if __name__ == '__main__':
    app.run(debug=True)
    # Runs on port 8050 by default. If you have a port conflict, add the parameter port=   e.g. port=8051