import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

def dash_navbar():
    navbar = dbc.NavbarSimple(  
    children=[
        dbc.NavItem(dbc.NavLink("US Analysis & Projections", href="/US")),
    ],
    brand="COVID-19 Pandemic Dashboard",
    brand_href="/home",
    color="black",
    dark=True,
    sticky="top"
    )
    return navbar

