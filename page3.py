import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

#global confirmed, recovered and deaths row
title =dbc.Card([dbc.CardBody([dbc.Container([ 
            html.H1(children='Case study: predicting confirmed COVID-19 cases from commonly collected laboratory tests at Hospital Israelita Albert Einstein', className='mt-5 py-4 pb-3 text-center'),
            html.P("Dashboard contributors: Bianca A. Hernandez, Ningning Du, Neil Hsu, Youngjung Choi", style = {'font-weight': 'bold'}, className='mt-3 py-2 pb-1 text-center'),
            ])])])
case_container1 = dbc.Card([
        dbc.CardBody([
            dbc.Row([
                dbc.Col(
                    dbc.Container([
                        html.Div([
                            html.H4('Background:', className='mt-5 py-4 pb-3 text-center'),
                            html.P("The World Health Organization (WHO) characterized COVID-19, caused by the SARS-CoV-2, as a pandemic on March 11. On March 20, the Brazilian federal government declared a nationwide community transmission."), 
                            html.H4("Motivation:", style = {'font-weight': 'bold'}, className='mt-3 py-2 pb-1 text-center'),
                            html.P("When considering an overwhelmed health system and possible limitataions to prerform SARS-CoV-2 tests, testing every case would be impractical and could lead to test result delays."),  
                ])])),
                dbc.Col(
                    dbc.Container([
                        html.Div([
                            html.H4('Dataset: ', className='mt-5 py-4 pb-3 text-center'),
                            html.P("Anonymized data from patients seen at the Hospital Israelita Albert Einstein, Sao Paulo, Brazil. Patients had samples collected to test for the SARS-CoV-2 RT-PCR (bloodwork). The dataset consists of 5644 records and 101 variables."),
                            html.H4("Question:", style = {'font-weight': 'bold'}, className='mt-3 py-2 pb-1 text-center'),
                            html.P("Would it be possible to predict the test result for SARS-Cov-2 (positive/negative) based on the results of laboratory tests commonly collected for a suspected COVID-19 case during a visit to the emergency room?"),    
                    ])]))])])])

def case_title():
    value = title
    return value
def case_container():
    value = case_container1
    return value
