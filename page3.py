import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from plots import case_features 
from ml_icu import case_features_icu

#global confirmed, recovered and deaths row
title =dbc.Card([dbc.CardBody([dbc.Container([ 
            html.H1(children='Case study: predicting 1) confirmed COVID-19 cases from suspected cases and 2) admission to ICU among confirmed COVID-19 cases based off patient data from Hospital Israelita Albert Einstein', className='mt-5 py-4 pb-3 text-center'),
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
                            html.P("Testing all SARS-CoV-2 cases would be impractical and could lead to test result delays especially when considering an overwhelmed health system."),  
                ])])),
                dbc.Col(
                    dbc.Container([
                        html.Div([
                            html.H4('Dataset: ', className='mt-5 py-4 pb-3 text-center'),
                            html.P("Anonymized data from patients seen at the Hospital Israelita Albert Einstein, Sao Paulo, Brazil. Patients had samples collected to test for the SARS-CoV-2 RT-PCR (bloodwork). The dataset consists of 5644 records and 101 variables."),
                            html.H4("Question:", style = {'font-weight': 'bold'}, className='mt-3 py-2 pb-1 text-center'),
                            html.P("Would it be possible to predict the test result for SARS-Cov-2 (positive/negative) based on the results of laboratory tests commonly collected for a suspected COVID-19 case during a visit to the emergency room?"),    
                    ])]))])])])
case_container2 = dbc.Card([
    dbc.CardBody([
        dbc.Row([
            
            dbc.Col(
                html.Div([
                html.H4("Predicting confirmed COVID-19 cases among suspected cases", style = {'font-weight': 'bold'}, className='mt-3 py-2 pb-1 text-center'),
                html.P("EDA: looked at distribution of dataset; handled missing values; identified correlations; encoded variables to deal with catergorical variables; removed collinear variables and identified most important features from dataset."),
                html.P("ML: ran split and train validation, ran model selector (KNeighborsClassifier, SVC, DecisionTreeClassifier, RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier), ran hyperparameter optimization (find best parameters for algorithm), created a base model and trained the model with GridSearch."),

                ])
            ),
            dbc.Col(
                dbc.Container([
                    html.Div([
                        dcc.Graph(
                            id = "case-fig", 
                            figure = case_features()
                    
                        )
                        
                    ])
                ])
            ),
        ])
    ])
])

case_container3 = dbc.Card([
    dbc.CardBody([
        dbc.Row([
            
            dbc.Col(
                html.Div([
                html.H4("Predicting admission to ICU among confirmed COVID-19 cases", style = {'font-weight': 'bold'}, className='mt-3 py-2 pb-1 text-center'),
                html.P("EDA: Data is imbalanced: 558 patients tested positive/8 needed ICU care. Many features are included in the datasheets but not all are usable due to small sample sizes: patient age, bloodwork(cell counts, potassium, sodium etc), other viruses test result (influenza a, b, h1n1 etc) and urine analysis."),
                html.P("ML: A Random Forest Classifier model was chosen: SMOTE oversampling for minority group, feature selection, hyperparameter tuning for overfitting issue and improving specificity and sensitivity scores"),
                

                ])
            ),
            dbc.Col(
                dbc.Container([
                    html.Div([
                        dcc.Graph(
                            id = "case-figicu", 
                            figure = case_features_icu()
                    
                        )
                        
                    ])
                ])
            ),
        ])
    ])
])

#footer
case_footer = dbc.Container([
        html.P('Data Source: Patients seen at Hospital Israelita Albert Einstein, at Sao Paulo, Brazil, https://www.kaggle.com/einsteindata4u/covid19', style = {'font-weight': 'bold'}, className='mt-3 py-2 pb-1 text-center'),
    ])

def case_title():
    value = title
    return value
def case_container():
    value = case_container1
    return value
def case_2():
    value = case_container2
    return value 
def case_3():
    value = case_container3
    return value 
def cas_study_footer():
    value = case_footer
    return value 