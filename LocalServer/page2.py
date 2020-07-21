import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import numpy as np
#data

US_country_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_country.csv')

US_country_df=US_country_df.loc[US_country_df['Country_Region'] == 'US']
US_country_df['Deaths'] = US_country_df['Deaths'].astype(int).apply(lambda x: "{:,}".format(x))
US_country_df['Recovered'] = US_country_df['Recovered'].astype(int).apply(lambda x: "{:,}".format(x))
US_country_df['Active'] = US_country_df['Active'].astype(int).apply(lambda x: "{:,}".format(x))
US_country_df['Confirmed'] = US_country_df['Confirmed'].astype(np.int64).apply(lambda x: "{:,}".format(x))



#tally
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

#global confirmed, recovered and deaths row
container1 = dbc.Card([dbc.CardBody([dbc.Container([ 
            html.H1(children='Just example tableau', className='mt-5 py-4 pb-3 text-center'),
            html.Iframe(src="https://public.tableau.com/views/USmapsdeathscases/Story1?:language=en&:display_count=y&publish=yes&:origin=viz_share_link:showVizHome=no&:embed=true", width="1000", height="827")
            ])])])
container2 = dbc.Card([dbc.CardBody([dbc.Container([ 
            html.H1(children='This is where we can put an ML simulator', className='mt-5 py-4 pb-3 text-center')
            ])])])

def tallies():
    layout = dbc.Row([dbc.Col(US_first_card), dbc.Col(US_second_card), dbc.Col(US_third_card), dbc.Col(US_fourth_card)], className='justify-content-center',)
    return layout            
def container_box():
    value = container1
    return value
def container_box2():
    value = container2
    return value






