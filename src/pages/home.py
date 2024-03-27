# This version is after the final activity in week 7
import dash
from dash import Dash, html, dcc,Output, Input
import dash_bootstrap_components as dbc
#from layout_elements import row_eleven,row_one,row_ten,row_four,row_nine,row_five,row_six,row_two,row_three,row_seven,row_eight
from figures import pie_chart,bar_chart,table_stats,line_chart,heatmap
import pandas as pd
import plotly.graph_objs as go
from pathlib import Path
from pages import energypage,parking_spaces 
# Variable that contain
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Click here for information about Parking Spaces", href = '/spaces'))],#href=dash.page_registry['pages.parking_spaces']['path'])),
    
    #brand="Paralympics Dashboard",
    #brand_href="#",#brand="Navigation 1",
                color="dark",
                dark=True,
                #expand="md",
                style={'position': 'absolute', 'top': 0, 'left': 0, 'right': 0, 'z-index': 1000}
    #color="primary",
    #dark=True,
)

navbar1 = dbc.NavbarSimple(
    children=[dbc.NavItem(dbc.NavLink("Click here for information about Renewable Energy",href= '/energy'))],#href=dash.page_registry['pages.energypage']['path']))],
    #brand_href="#",#brand="Navigation 1",
                color="dark",
                dark=True,
                #expand="md",
                style={'position': 'absolute', 'top': 0, 'left': 0, 'right': 0, 'z-index': 1000}
)

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
                    #html.H5("Card title", className="card-title"),
                    #html.P("This is some card content"),
                    navbar
                    #dbc.Button("Button", color="primary")
                ]),
                style={'background-image': 'url("/assets/parking.jpg")', 'height': '400px','background-size': 'cover'}
            ),
            width=5
        ),dbc.Col(
            dbc.Card(
                dbc.CardBody([
                   # html.H5("Card title", className="card-title"),
                    #html.P("This is some card content"),
                    navbar1
                    #dbc.Button("Button", color="primary")
                ]),
                style={'transition': 'filter 0.3s ease-in-out','background-image': 'url("/assets/renewable.jpg")', 'height': '400px','background-size': 'cover'}
            ),
            width=5
        )]),
    #dbc.Row([dbc.Col(children=[navbar2],width=1),
    #]),
    #html.H2("Click here for information about Renewable Energy", id='energy'),
])])