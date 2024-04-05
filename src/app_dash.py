
import dash
from dash import Dash, html, dcc,Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go
from pathlib import Path
from pages import energypage,parking_spaces,home

external_stylesheets = [dbc.themes.BOOTSTRAP]
app = dash.Dash(__name__, suppress_callback_exceptions=True,external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
    html.A('Go to top', href='#top', id='top-link', style={'background-color': 'gray', 'color': 'white', 'padding': '10px'})
])

@app.callback(
    Output(component_id='page-content', component_property='children'),
    [Input(component_id='url', component_property='pathname')]
)
def display_page(pathname):
    
    if not pathname or pathname == '/':
        # If no pathname (first load), display the home page
        return home.layout
    
    elif pathname == '/home':
        return home.layout
    elif pathname == '/energy':
        return energypage.layout
    elif pathname == '/spaces':
        return parking_spaces.layout
    else:
        return html.Div("404 - Page not found")
    
    
@app.callback(
    Output('top-link', 'style'),
    [Input('url', 'pathname')]
)
def update_top_link_style(pathname):
    if pathname == '/home':
        return {'display': 'none'}  # Hide the link on the home page
    else:
        return {'background-color': 'gray', 'color': 'white', 'padding': '10px'}

if __name__ == '__main__':
    app.run(debug=True)