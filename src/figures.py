from pathlib import Path
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px

event_data = Path(__file__).parent.parent.joinpath("data", "prepared6.csv")

def bar_chart(num_charts):
    """
    Creates a stacked bar chart showing change in the number of sports in the summer and winter paralympics
    over time
    An example for exercise 2.

    :param event_type: str Winter or Summer
    :return: Plotly Express bar chart
    """
    cols = ['HE provider', 'cycle_spaces', 'car_spaces']
    df_events = pd.read_csv(event_data, usecols=cols)
    """fig = px.bar(df_events,
                 x='HE provider',
                 y=['cycle_spaces', 'car_spaces'],
                 title='How has the ratio of female:male participants changed?',
                 labels={'xlabel': '', 'value': '', 'variable': ''},
                 color_discrete_map={'M%': 'blue', 'F%': 'green'},
                 template="simple_white",
                 barmode= 'group'
                 ).update_layout(height= 800)
    fig.update_traces(marker_line_width=0.01)
    fig.update_xaxes(ticklen=0)
    #return fig"""

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df_events['HE provider'][:num_charts],
        y=df_events['cycle_spaces'][:num_charts],
        name='cycle_spaces'
    ))
    fig.add_trace(go.Bar(
        x=df_events['HE provider'][:num_charts],
        y=df_events['car_spaces'][:num_charts],
        name='car_spaces'
    ))
    fig.update_layout(title='How has the ratio of female:male participants changed?',
        template="simple_white",
        barmode= 'group',height = 800)
    fig.update_traces(marker_line_width=0.01)
    fig.update_xaxes(ticklen=0)
    return fig

def pie_chart(selected_provider):
    cols = ['HE provider', 'cycle_spaces', 'car_spaces']
    df = pd.read_csv(event_data,usecols=cols)  
        
    filtered_data = df[df['HE provider'] == selected_provider]
    cycle_spaces = filtered_data['cycle_spaces'].values[0]
    car_spaces = filtered_data['car_spaces'].values[0]  
    #cycle_spaces_total = filtered_data['cycle_spaces']
    #car_spaces_total = filtered_data['car_spaces']
    labels = ['Cycle Spaces', 'Car Spaces']
    cols = ['cycle_spaces', 'car_spaces']
    values = [cycle_spaces,car_spaces]
    colors = ['gold', 'lightgreen']
  
    figure = go.Figure(data=[go.Pie(labels=labels, values=values,title=f'Pie Chart for {selected_provider}')]).update_layout(height= 800)
    figure.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                  marker=dict(colors=colors, line=dict(color='#000000', width=2)))
    #figure.show()
    """figure = px.pie(df, values=values, names=labels, title=f'Pie Chart for {selected_provider}').update_layout(height= 800)
    figure.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                  marker=dict(colors=colors, line=dict(color='#000000', width=0.01)))"""
    return figure
