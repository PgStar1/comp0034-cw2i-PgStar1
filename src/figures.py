from pathlib import Path
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px

data = Path(__file__).parent.parent.joinpath("data", "prepared.csv")
dataset_2016 = pd.read_csv(data)
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



def bar_chart(num_charts,selected_year):
    """
    Creates a stacked bar chart showing change in the number of sports in the summer and winter paralympics
    over time
    An example for exercise 2.

    :param event_type: str Winter or Summer
    :return: Plotly Express bar chart
    """
    #cols = ['HE provider', 'cycle_spaces', 'car_spaces']
    #df_events = pd.read_csv(data6, usecols=cols)
    if isinstance(selected_year, list):
        selected_year = selected_year[0]
    
    filtered_data = year_datasets[selected_year]
    

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=filtered_data['HE provider'][num_charts[0]:num_charts[1]],
        y=filtered_data['Total number of cycle spaces'][num_charts[0]:num_charts[1]],
        name='cycle_spaces'
    ))
    fig.add_trace(go.Bar(
        x=filtered_data['HE provider'][num_charts[0]:num_charts[1]],
        y=filtered_data['Total number of car parking spaces'][num_charts[0]:num_charts[1]],
        name='car_spaces'
    ))
    fig.update_layout(title='How has the ratio of female:male participants changed?',
        template="simple_white",
        barmode= 'group',height = 800)
    fig.update_traces(marker_line_width=0.01)
    fig.update_xaxes(ticklen=0)
    return fig

def pie_chart(selected_provider,selected_year):
    
    #filtered_data = year_datasets[selected_year[0]]
    if isinstance(selected_year, list):
        selected_year = selected_year[0]
    filtered_data = year_datasets[selected_year]
    #print(filtered_data)
    if selected_provider:
        filtered_data = filtered_data[filtered_data['HE provider'] == selected_provider]
    cycle_spaces = filtered_data['Total number of cycle spaces'].values[0]
    car_spaces = filtered_data['Total number of car parking spaces'].values[0]
    #values = filtered_data[['cycle_spaces', 'car_spaces', 'energy']]
    print(cycle_spaces, car_spaces)
    labels = ['Cycle Spaces', 'Car Spaces']
    colors = ['gold', 'lightgreen']
    values = [cycle_spaces,car_spaces]
    figure = go.Figure(data=[go.Pie(labels=labels, values=values,title=dict(text = f'Pie Chart for {selected_provider} ({selected_year})',font=dict(size=16,color="red")))]).update_layout(height= 600,margin=dict(b=1,t=5,r=4,l=40),
    paper_bgcolor='rgba(0,0,0,0)',  # Set plot background color to transparent paper_bgcolor='powderblue'
    legend=dict(x=0.8,y=0.84,font=dict(size=16,color='red'),# Show legend box
        bgcolor='rgba(0,0,0,0)',  # Set background transparent
        bordercolor="gray",  # Add border for visual separation
        borderwidth=1)                                            )
    figure.update_traces(textinfo='percent+label', textfont_size=20,
                  marker=dict(colors=colors, line=dict(color='#000000', width=2)))
    #figure.show()
    """figure = px.pie(df, values=values, names=labels, title=f'Pie Chart for {selected_provider}').update_layout(height= 800)
    figure.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                  marker=dict(colors=colors, line=dict(color='#000000', width=0.01)))"""
    return figure

def table_stats(selected_provider):
    filtered_data = year_datasets[selected_provider]
    
def line_chart(selected_providers):
    """filtered_data = all_data[all_data['HE provider'] == selected_provider]
    print(filtered_data['HE provider'])
    # Create line chart
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=filtered_data['Year'], y=filtered_data['Total renewable energy generated onsite or offsite (kWh)'], mode='lines', name='Energy'))
    fig.update_layout(title=f'Energy Over Years for {selected_provider}',
                      xaxis_title='Year',
                      yaxis_title='Energy')
    return fig"""
    
    filtered_data = all_data[all_data['HE provider'].isin(selected_providers)]
    
    # Create line chart
    fig = go.Figure()
    for provider in selected_providers:
        provider_data = filtered_data[filtered_data['HE provider'] == provider]
        fig.add_trace(go.Scatter(x=provider_data['Year'], y=provider_data['Total renewable energy generated onsite or offsite (kWh)'], mode='lines', name=provider))
    fig.update_layout(title='Energy Over Years for Selected Providers',
                      xaxis_title='Year',
                      yaxis_title='Energy')
    return fig

"""def heatmap(selected_providers):
    
    filtered_data = all_data[all_data['HE provider'].isin(selected_providers)]
    for provider in selected_providers:
        provider_data = filtered_data[filtered_data['HE provider'] == provider]
    heatmap_trace = go.Heatmap(
    x=provider_data['Year'],
    y=provider_data['HE provider'],
    z=provider_data['Total renewable energy generated onsite or offsite (kWh)'],
    #colorscale='Viridis',  # Change colorscale as needed
    #colorbar=dict(title='Energy Consumption')
)
    return heatmap_trace"""

def heatmap(selected_providers):

    #if not selected_providers:
     #   return {}
    #filtered_data = all_data[all_data["HE provider"] == selected_provider]
    filtered_data = all_data[all_data['HE provider'].isin(selected_providers)]
    filtered_data  = filtered_data.pivot(index='HE provider',columns='Year',values='Total renewable energy generated onsite or offsite (kWh)') 
    # Check if data is empty for the selected provider
    fig = px.imshow(filtered_data,color_continuous_scale=px.colors.sequential.OrRd)
    """heatmap_trace = go.Heatmap(
            x=filtered_data["Year"],
            #y=filtered_data["HE provider"],  # This value is likely not useful for a single provider
            y=filtered_data["Total renewable energy generated onsite or offsite (kWh)"],
            # colorscale='Viridis',  # Optional color scale customization
            # colorbar=dict(title='Energy Consumption')  # Optional color bar customization
        )"""
    return fig
    # Return None if no data is found for the selected provider




    