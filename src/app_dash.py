# This version is after the final activity in week 7
from dash import Dash, html, dcc,Output, Input
import dash_bootstrap_components as dbc
from layout_elements import row_one,row_four,row_five,row_six,row_two
from figures import pie_chart,bar_chart
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
    row_one,row_four,row_five,row_two,
    row_six
])

data = Path(__file__).parent.parent.joinpath("data", "prepared6.csv")
df = pd.read_csv(data)

@app.callback(
    Output(component_id = 'pie',component_property='figure'),
    Input(component_id = 'dropdown',component_property='value')
)

def update_pie_chart(provider):
    #df = pd.read_csv('your_data.csv')
    figure = pie_chart(provider)
    return figure

@app.callback(
    Output(component_id = 'bar',component_property='figure'),
    Input(component_id = 'bar-slider',component_property='value'),
    Input(component_id = 'search-input',component_property='value')
    
)

def update_bar_chart(selected_value,search_term):
    #df = pd.read_csv('your_data.csv')
    #filtered_df = df[df['HE provider'].str.contains(search_term, case=False)] if search_term else df
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
    return figure"""
    # Filter data based on search term (if provided)
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

    return fig, selected_value  # Return both figure and slider value



# Run the Dash app
if __name__ == '__main__':
    app.run(debug=True)
    # Runs on port 8050 by default. If you have a port conflict, add the parameter port=   e.g. port=8051