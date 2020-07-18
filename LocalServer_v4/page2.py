import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import plotly

import pandas as pd
import numpy as np
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime


#Data
US_country_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_country.csv')

US_country_df=US_country_df.loc[US_country_df['Country_Region'] == 'US']
US_country_df['Deaths'] = US_country_df['Deaths'].astype(int).apply(lambda x: "{:,}".format(x))
US_country_df['Recovered'] = US_country_df['Recovered'].astype(int).apply(lambda x: "{:,}".format(x))
US_country_df['Active'] = US_country_df['Active'].astype(int).apply(lambda x: "{:,}".format(x))
US_country_df['Confirmed'] = US_country_df['Confirmed'].astype(np.int64).apply(lambda x: "{:,}".format(x))

#title and contributors
US_title_contributors =dbc.Card([dbc.CardBody([dbc.Container([ 
            html.H1(children='Remotely monitoring the COVID-19 pandemic: US', className='mt-5 py-4 pb-3 text-center'),
            html.P("Dashboard contributors: Bianca A. Hernandez, Ningning Du, Neil Hsu, Youngjung Choi", style = {'font-weight': 'bold'}, className='mt-3 py-2 pb-1 text-center'),
            ])])])

#cards for tally us
US_first_card=dbc.Card([
    dbc.CardBody(children=[html.H4('Confirmed', style = {'padding-top': '5px','font-weight':'bold', 'color':'#5e4fa2'}),
        html.Div([dbc.Button(US_country_df['Confirmed'].sum(), color="#5e4fa2", size = "lg")])],
        className='text-center')
                    ]),
US_second_card=dbc.Card([
    dbc.CardBody(children = [html.H4('Recovered', style = {'padding-top': '5px', 'font-weight':'bold', 'color':'#66c2a5'}),
        html.Div([dbc.Button(US_country_df['Recovered'].sum(), color="#66c2a5", size = "lg")])],
        className='text-center'),
                    ]),
US_third_card=dbc.Card([
    dbc.CardBody(children = [html.H4('Deaths', style = {'padding-top': '5px', 'font-weight':'bold', 'color':'#d53e50'}),
        html.Div([dbc.Button(US_country_df['Deaths'].sum(), color="#d53e50", size = "lg")])],
        className='text-center'),
                    ]),
US_fourth_card=dbc.Card([
    dbc.CardBody(children = [html.H4('Active', style = {'padding-top': '5px', 'font-weight':'bold', 'color':'#f46d43',}),
        html.Div([dbc.Button(US_country_df['Active'].sum(), color="#f46d43", size = "lg")])],
        className='text-center'),
])


container1 = dbc.Card([dbc.CardBody([dbc.Container([ 
            html.H1(children='US Map Analysis', className='mt-3 py-2 pb-1 text-center'),
            ])])])

container2 = html.Div([
        html.Iframe(src="https://public.tableau.com/views/USmapsdeathscases/Dashboard1?:embed=yes&:showVizHome=no", width = "100%", height = "1000")
])

US_first_row = html.Div([
    html.Br(),
        html.Iframe(src="https://public.tableau.com/views/Top_10_states_ACD/Dashboard2?:embed=yes&:showVizHome=no", width = "100%", height = "1000")
])

def US_title_authors():
    heading = US_title_contributors
    return heading

def us_tallies():
    layout = dbc.Row([dbc.Col(US_first_card), dbc.Col(US_second_card), dbc.Col(US_third_card), dbc.Col(US_fourth_card)], className='justify-content-center',)
    return layout

def container_box():
    value = container1
    return value
def container_box2():
    value = container2
    return value

def US_main():
    value = US_first_row
    return value






