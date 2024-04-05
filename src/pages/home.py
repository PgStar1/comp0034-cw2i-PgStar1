import dash
from dash import Dash, html, dcc,Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go
from pathlib import Path
from pages import energypage,parking_spaces 

#CREATED NAVIGATION BARS TO ALLOW THE USER TO GO TO A SPECIFIC PAGE TO ACCESS CHARTS
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Click here for information about Parking Spaces", href = '/spaces',id='parking'))],
    
                color="dark",
                dark=True,
                style={'position': 'absolute', 'top': 0, 'left': 0, 'right': 0, 'z-index': 1000}
)

navbar1 = dbc.NavbarSimple(
    children=[dbc.NavItem(dbc.NavLink("Click here for information about Renewable Energy",href= '/energy',id='energy'))],
                color="dark",
                dark=True,
                style={'position': 'absolute', 'top': 0, 'left': 0, 'right': 0, 'z-index': 1000}
)

# Created a responsive layout for the App 

layout = dbc.Container([html.Div([
    dbc.Row([dbc.Col(children=[],width=1),
        dbc.Col(html.H1("TRANSPORT AND ENVIRONMENT METRICS AT VARIOUS HIGHER EDUCATION PROVIDERS"),
                width=8,
                style={'height': '200px', 'font': 'Lato', 'background-color': '#1a202c', 'color': '#4fd1c5'}
                ),
        dbc.Col(html.Img(src='/assets/logo.jpg', style={'top': '10px', 'right': '10px', 'height': '200px'}),
                width=3),
    ]),
    html.Br(),
    dbc.Row([dbc.Col(children=[],width=1),dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    navbar
                ]),
                style={'background-image': 'url("/assets/parking.jpg")', 'height': '400px','background-size': 'cover'}
            ),
            width=5
        ),dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    navbar1
                ]),
                style={'transition': 'filter 0.3s ease-in-out','background-image': 'url("/assets/renewable.jpg")', 'height': '400px','background-size': 'cover'}
            ),
            width=5
        )]),
])],fluid=True)