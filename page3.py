import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

#global confirmed, recovered and deaths row
title =dbc.Card([dbc.CardBody([dbc.Container([ 
            html.H1(children='Case study: determining factors for intensive care need at Hospital Israelita Albert Einstein, Sao Paulo, Brazil ', className='mt-5 py-4 pb-3 text-center'),
            html.P("Dashboard contributors: Bianca A. Hernandez, Ningning Du, Neil Hsu, Youngjung Choi", style = {'font-weight': 'bold'}, className='mt-3 py-2 pb-1 text-center'),
            ])])])
case_container1 = dbc.Card([dbc.CardBody([dbc.Container([ 
            html.H1(children='This is where we can have case study', className='mt-5 py-4 pb-3 text-center')
            ])])])
def case_title():
    value = title
    return value
def case_container():
    value = case_container1
    return value
