import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import plotly

import pandas as pd
import numpy as np
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

from plots import bubble_fig, global_animation, plot_cases_for_country

#Data
death_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
confirmed_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
recovered_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
country_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_country.csv')

#Data/add comma
country_df.fillna(0,inplace=True)
country_df['Total_Confirmed']=country_df['Confirmed'].sum()
country_df['Total_Recovered']=country_df['Recovered'].sum()
country_df['Total_Deaths']=country_df['Deaths'].sum()
country_df['Total_Active']=country_df['Active'].sum()

country_df['Total_Deaths'] = country_df['Total_Deaths'].astype(int).apply(lambda x: "{:,}".format(x))
country_df['Total_Recovered'] = country_df['Total_Recovered'].astype(int).apply(lambda x: "{:,}".format(x))
country_df['Total_Active'] = country_df['Total_Active'].astype(int).apply(lambda x: "{:,}".format(x))
country_df['Total_Confirmed'] = country_df['Total_Confirmed'].astype(np.int64).apply(lambda x: "{:,}".format(x))


death_df.drop('Province/State', axis=1, inplace=True)
confirmed_df.drop('Province/State', axis=1, inplace=True)
recovered_df.drop('Province/State', axis=1, inplace=True)
country_df.drop(['People_Tested', 'People_Hospitalized'], axis=1, inplace=True)

death_df.rename(columns={'Country/Region': 'Country'}, inplace=True)
confirmed_df.rename(columns={'Country/Region': 'Country'}, inplace=True)
recovered_df.rename(columns={'Country/Region': 'Country'}, inplace=True)
country_df.rename(columns={'Country_Region': 'Country', 'Long_': 'Long'}, inplace=True)
country_df.sort_values('Confirmed', ascending=False, inplace=True)


#heading and contributors
title_contributors =dbc.Card([dbc.CardBody([dbc.Container([ 
            html.H1(children='Remotely monitoring the COVID-19 pandemic', className='mt-5 py-4 pb-3 text-center'),
            html.P("Dashboard contributors: Bianca A. Hernandez, Ningning Du, Neil Hsu, Youngjung Choi", style = {'font-weight': 'bold'}, className='mt-3 py-2 pb-1 text-center'),
            ])])])

#cards for tally

first_card=dbc.Card([
    dbc.CardBody(children=[html.H4('Confirmed', style = {'padding-top': '5px','font-weight':'bold', 'color':'#5e4fa2'}),
        html.Div([dbc.Button(country_df['Total_Confirmed'].max(), color="#5e4fa2", size = "lg")])],
        className='text-center')
                    ]),
second_card=dbc.Card([
    dbc.CardBody(children = [html.H4('Recovered', style = {'padding-top': '5px', 'font-weight':'bold', 'color':'#66c2a5'}),
        html.Div([dbc.Button(country_df['Total_Recovered'].max(), color="#66c2a5", size = "lg")])],
        className='text-center'),
                    ]),
third_card=dbc.Card([
    dbc.CardBody(children = [html.H4('Deaths', style = {'padding-top': '5px', 'font-weight':'bold', 'color':'#d53e50'}),
        html.Div([dbc.Button(country_df['Total_Deaths'].max(), color="#d53e50", size = "lg")])],
        className='text-center'),
                    ]),
fourth_card=dbc.Card([
    dbc.CardBody(children = [html.H4('Active', style = {'padding-top': '5px', 'font-weight':'bold', 'color':'#f46d43',}),
        html.Div([dbc.Button(country_df['Total_Active'].max(), color="#f46d43", size = "lg")])],
        className='text-center'),
])

#headings for bubble and global animations
tally_heading = html.H2(children='World Cases Tally', className='mt-5 py-4 pb-3 text-center')
global_map_heading = html.H2(children='World outbreaks of COVID-19 across time', className='mt-5 py-4 pb-3 text-center')
us_heading =  html.H2(children='US Cases: Confirmed, recovered and deaths', className='mt-3 py-2 pb-1 text-center')
world_heading =  html.H2(children='World Cases: Confirmed, recovered and deaths', className='mt-3 py-2 pb-1 text-center')

#bubble figure: top ten countries by case
bubble_fig = px.scatter(country_df.head(10), 
    x = 'Country', 
    y ='Confirmed', 
    size = 'Confirmed', 
    color = 'Country', 
    hover_name = 'Country',
    size_max = 50)

#bubble fig and animation row 
third_row = dbc.Card([
        dbc.CardBody([
            dbc.Row([
                dbc.Col(
                    dbc.Container([
                        html.Div([
                            html.H2('What is COVID-19?', className='mt-5 py-4 pb-3 text-center'),
                            html.P("COVID-19 is a disease caused by a new strain of coronavirus. 'CO' stands for corona, 'VI' for virus, and 'D' for disease."),
                            html.P("Symptoms can include fever, cough and shortness of breath. In more severe cases, infection can cause pneumonia or breathing difficulties. More rarely, the disease can be fatal."),
                            html.P("The virus is transmitted through direct contact with respiratory droplets of an infected person (generated through coughing and sneezing)."),
                            html.H4("Countries with most confirmed COVID-19 cases", style = {'font-weight': 'bold'}, className='mt-3 py-2 pb-1 text-center'),
                        html.Div(dcc.Graph(
                        id='top-ten',
                        figure=bubble_fig))    
                ])])),
                dbc.Col(
                    dbc.Container([global_map_heading,
                    html.Div(id='global-total'), 
                    dcc.Graph(
                        id='global-viz',
                        figure=global_animation()
                        ),
                        html.Div([
                            dbc.Container([
                                html.H4("To prevent infection and to slow transmission of COVID-19, do the following:", style = {'font-weight': 'bold'}, className='mt-3 py-2 pb-1 text-center'),
                                ]),
                    html.P("Wash your hands regularly with soap and water, or clean them with alcohol-based hand rub. Avoid touching your face. Stay home if you feel unwell."),
                    html.P("Practice physical distancing by avoiding unnecessary travel and staying away from large groups of people."),
                    html.P("Cover your mouth and nose when coughing or sneezing."),    
                    ])]))])])])

#global confirmed, recovered and deaths row
fourth_row = dbc.Card([
        dbc.CardBody([
            dbc.Container([world_heading, 
            html.Div(id='us-total'),
            dcc.Graph(
                id='us-viz',
                figure=plot_cases_for_country('World'))]),

        ])])
#footer
fifth_row = dbc.Container([
        html.P('Data Source: COVID-19 Data Repository by Johns Hopkins University (CSSE)', style = {'font-weight': 'bold'}, className='mt-3 py-2 pb-1 text-center'),
    ])

def title_authors():
    heading = title_contributors
    return heading
def tallies():
    layout = dbc.Row([dbc.Col(first_card), dbc.Col(second_card), dbc.Col(third_card), dbc.Col(fourth_card)], className='justify-content-center',)
    return layout
def bubble_animation_col():
    column = third_row
    return column 
def global_line_graph():
    column = fourth_row
    return column 
def footer_row():
    column = fifth_row
    return column 
    
    






