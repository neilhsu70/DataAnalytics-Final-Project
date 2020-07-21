import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

#global confirmed, recovered and deaths row
case_container1 = dbc.Card([dbc.CardBody([dbc.Container([ 
            html.H1(children='This is where we can have case study', className='mt-5 py-4 pb-3 text-center')
            ])])])

def case_container():
    value = case_container1
    return value
