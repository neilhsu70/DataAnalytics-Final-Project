import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

def dash_navbar():
    navbar = dbc.NavbarSimple(  
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/home")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("US Analysis", href="/US"),
                dbc.DropdownMenuItem("Case Study", href="/Case"),   
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
                
    ],
    brand="COVID-19 Pandemic Dashboard",
    brand_href="/home",
    color="black",
    dark=True,
    sticky="top"
    )
    return navbar


