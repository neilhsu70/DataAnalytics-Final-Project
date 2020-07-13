import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

#global confirmed, recovered and deaths row
container1 = dbc.Card([dbc.CardBody([dbc.Container([ 
            html.H1(children='This is where we can link tableau, or create a plotly visualization?', className='mt-5 py-4 pb-3 text-center')
            ])])])
container2 = dbc.Card([dbc.CardBody([dbc.Container([ 
            html.H1(children='This is where we can put an ML simulator', className='mt-5 py-4 pb-3 text-center')
            ])])])
def container_box():
    value = container1
    return value
def container_box2():
    value = container2
    return value






