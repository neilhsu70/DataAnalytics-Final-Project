#get_default_color
import dash
#pip install dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

#import necessary libraries
from plotly import tools
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px
import plotly.graph_objects as go #for calling graph objects from plotly library.
import pandas as pd
import numpy as np 
import requests
#!pip install wget
from datetime import datetime
from scipy.interpolate import interp1d

#loading global COVID-19 datasets
death_df =  pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
confirmed_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
recovered_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
country_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_country.csv')

dates = confirmed_df.columns[4:]
confirmed_df_long = confirmed_df.melt(
    id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], 
    value_vars=dates, 
    var_name='Date', 
    value_name='Confirmed'
)
death_df_long = death_df.melt(
    id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], 
    value_vars=dates, 
    var_name='Date', 
    value_name='Deaths'
)
recovered_df_long = recovered_df.melt(
    id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], 
    value_vars=dates, 
    var_name='Date', 
    value_name='Recovered'
)

recovered_df_long = recovered_df_long[recovered_df_long['Country/Region']!='Canada']

full_table = confirmed_df_long.merge(
  right=death_df_long, 
  how='left',
  on=['Province/State', 'Country/Region', 'Date', 'Lat', 'Long']
)
# Merging full_table and recovered_df_long
full_table = full_table.merge(
  right=recovered_df_long, 
  how='left',
  on=['Province/State', 'Country/Region', 'Date', 'Lat', 'Long']
)

full_table['Date'] = pd.to_datetime(full_table['Date'])
full_table['Recovered'] = full_table['Recovered'].fillna(0)

ship_rows = full_table['Province/State'].str.contains('Grand Princess') | full_table['Province/State'].str.contains('Diamond Princess') | full_table['Country/Region'].str.contains('Diamond Princess') | full_table['Country/Region'].str.contains('MS Zaandam')
full_ship = full_table[ship_rows]
full_table = full_table[~(ship_rows)]
full_table['Active'] = full_table['Confirmed'] - full_table['Deaths'] - full_table['Recovered']
full_grouped = full_table.groupby(['Date', 'Country/Region', 'Lat', 'Long'])['Confirmed', 'Deaths', 'Recovered', 'Active'].sum().reset_index()

temp = full_grouped.groupby(['Country/Region', 'Date', ])['Confirmed', 'Deaths', 'Recovered']
temp = temp.sum().diff().reset_index()
mask = temp['Country/Region'] != temp['Country/Region'].shift(1)
temp.loc[mask, 'Confirmed'] = np.nan
temp.loc[mask, 'Deaths'] = np.nan
temp.loc[mask, 'Recovered'] = np.nan
# renaming columns
temp.columns = ['Country/Region', 'Date', 'New cases', 'New deaths', 'New recovered']
# merging new values
full_grouped = pd.merge(full_grouped, temp, on=['Country/Region', 'Date'])
# filling na with 0
full_grouped = full_grouped.fillna(0)
# fixing data types
cols = ['New cases', 'New deaths', 'New recovered']
full_grouped[cols] = full_grouped[cols].astype('int')
# 
full_grouped['New cases'] = full_grouped['New cases'].apply(lambda x: 0 if x<0 else x)
full_grouped["Date"] = full_grouped["Date"].dt.strftime('%Y/%m/%d')


#us data and cleaning 




#plot
def global_animation():
    fig = px.scatter_mapbox(full_grouped,
                            lat="Lat", 
                            lon="Long",                       
                            color="Confirmed", 
                            size=full_grouped['Confirmed']**0.5*50,
                            template='seaborn',
                            color_continuous_scale="spectral", 
                            size_max=50, 
                            animation_frame='Date', 
                            zoom=0.7, 
                            hover_data= ['Country/Region'])
    
    fig.update_layout(
        mapbox_style="carto-positron",
        margin={"r":1,"t":1,"l":1,"b":1})
    #update frame speed
    fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 200
    #update different layouts
    fig.layout.sliders[0].currentvalue.prefix=""
    fig.layout.sliders[0].len=.9
    fig.layout.sliders[0].currentvalue.font.color="black"
    fig.layout.sliders[0].currentvalue.font.size=18
    return fig

death_df.drop('Province/State', axis=1, inplace=True)
confirmed_df.drop('Province/State', axis=1, inplace=True)
recovered_df.drop('Province/State', axis=1, inplace=True)
country_df.drop(['People_Tested', 'People_Hospitalized'], axis=1, inplace=True)

death_df.rename(columns={'Country/Region': 'Country'}, inplace=True)
confirmed_df.rename(columns={'Country/Region': 'Country'}, inplace=True)
recovered_df.rename(columns={'Country/Region': 'Country'}, inplace=True)
country_df.rename(columns={'Country_Region': 'Country', 'Long_': 'Long'}, inplace=True)
country_df.sort_values('Confirmed', ascending=False, inplace=True)

#top ten countries by case
def bubble_fig():
    fig = px.scatter(confirmed_df.head(10), 
    x = 'Country', 
    y ='Confirmed', 
    size = 'Confirmed', 
    color = 'Country', 
    hover_name = 'Country',
    size_max = 50)
    return fig 

df_list = [confirmed_df, recovered_df, death_df]

def plot_cases_for_country(ad):
    labels = ['Confirmed', 'Recoverd', 'Deaths']
    colors = ['#5e4fa2', '#66c2a5', '#d53e50']
    mode_size = [4,4,4]
    line_size = [4,4,4]

    fig = go.Figure()
    
    for i, df in enumerate (df_list):
        if ad =='world' or ad =='World':
            x_data = np.array(list (df.iloc[:,5:].columns))
            y_data = np.sum(np.asarray(df.iloc[:,5:]),axis = 0)
        
        else:
            x_data = np.array(list (df.iloc[:,5:].columns))
            y_data = np.sum(np.asarray(df[df['Country']==ad].iloc[:,5:]),axis = 0)
                        
        fig.add_trace(go.Scatter(x=x_data, y=y_data, mode='lines+markers',name=labels[i],
            line=dict(color=colors[i], width=line_size[i]),
            connectgaps=True,
            text = "Total " +str(labels[i]+ ":" +str(y_data[-1]))
         )) 
    return fig

#us animation
def us_animation():
    fig = px.scatter_mapbox(cumulative_df_us, 
                        lat="Lat", 
                        lon="Long_", 
                        size=cumulative_df_us["Confirmed"]**.5*50,
                        template = "seaborn",
                        color = "Confirmed",  
                        color_continuous_scale="spectral",
                        zoom=2, 
                        size_max=10, 
                        animation_frame="Date",
                        hover_name="Province_State", 
                        hover_data= ["Province_State","Confirmed"])
                        
                            

    fig.update_layout(margin=dict(l=1, r=1, t=1, b=1),
                  autosize=True,
                  mapbox_style="carto-positron")
    #update different layouts
    fig.layout.sliders[0].currentvalue.prefix=""
    fig.layout.sliders[0].len=.9
    fig.layout.sliders[0].currentvalue.font.color="black"
    fig.layout.sliders[0].currentvalue.font.size=18
    fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 200
    return fig 

import lightgbm as lgb
import lightgbm as LGBMRegressor
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

df = pd.read_csv("diagnosis-of-covid-19-and-its-clinical-spectrum.csv")

#number of unique classes in each object column
df.columns = [x.lower().strip().replace(' ','_') for x in df.columns]
df.select_dtypes('object').apply(pd.Series.nunique, axis = 0)

#first ten correlations between the features in dataset
features = df.columns.values[2:112]
corrs_ = df[features].corr().abs().unstack().sort_values(kind="quicksort").reset_index()
corrs_ = corrs_[corrs_['level_0'] != corrs_['level_1']]

#Encoding variables: find a way to encode (represent) these variables as numbers before handing them off to the model

#fill in mean for floats
for c in df.columns:
    if df[c].dtype=='float16' or  df[c].dtype=='float32' or  df[c].dtype=='float64':
        df[c].fillna(df[c].mean())

#fill in -999 for categoricals
df = df.fillna(-999)

#label Encoding
for f in df.columns:
    if df[f].dtype=='object': 
        lbl = preprocessing.LabelEncoder()
        lbl.fit(list(df[f].values))
        df[f] = lbl.transform(list(df[f].values))

#threshold for removing correlated variables
threshold = 0.92

#absolute value correlation matrix
corr_matrix = df.corr().abs()
corr_matrix.head()

#upper triangle of correlations
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool))

#select columns with correlations above threshold
to_drop = [column for column in upper.columns if any(upper[column] > threshold)]
dataset = df.drop(columns = to_drop)

#remove missing values
#dataset missing values (in percent)
dataset_missing = (dataset.isnull().sum() / len(dataset)).sort_values(ascending = False)

#identify missing values above threshold
dataset_missing_ = dataset_missing.index[dataset_missing > 0.85]
all_missing = list(set(dataset_missing_))
dataset = dataset.drop(columns = all_missing)

#feature selection through feature importance
cat_features = [i for i in dataset.columns if str(dataset[i].dtype) in ['object', 'category']]

if len(cat_features) > 0:
    dataset[cat_features] = dataset[cat_features].astype('category')


df_lgb = dataset.copy()
for i in cat_features:
    df_lgb[i] = dataset[i].cat.codes

df_lgb.columns = ["".join (c if c.isalnum() else "_" for c in str(x)) for x in df_lgb.columns]

dataset_labels = df_lgb['sars_cov_2_exam_result']
df_lgb_ = df_lgb.copy()
df_lgb = df_lgb.drop(['patient_id', 
                      'sars_cov_2_exam_result', 
                      'patient_addmited_to_regular_ward_1_yes_0_no',
                      'patient_addmited_to_semi_intensive_unit_1_yes_0_no',
                      'patient_addmited_to_intensive_care_unit_1_yes_0_no'
                ], axis=1)
x = df_lgb.copy()

# Initialize an empty array to hold feature importances
feature_importances = np.zeros(df_lgb.shape[1])

# Create the model with several hyperparameters
model = lgb.LGBMClassifier(objective='binary', boosting_type = 'goss', n_estimators = 5000, class_weight = 'balanced')

# Fit the model twice to avoid overfitting
for i in range(2):
    # Split into training and validation set
    dataset_features, valid_features, dataset_features_y, valid_y = train_test_split(x, dataset_labels, test_size = 0.20, random_state = i)
    
    # Train using early stopping
    model.fit(dataset_features, dataset_features_y, early_stopping_rounds=100, eval_set = [(valid_features, valid_y)], 
              eval_metric = 'auc', verbose = 200)
    
    # Record the feature importances
    feature_importances += model.feature_importances_
#average feature importances! 
feature_importances = feature_importances / 2
feature_importances = pd.DataFrame({'feature': list(df_lgb.columns), 'importance': feature_importances}).sort_values('importance', ascending = False)

#for dash app figure 
fig_feature_importances = feature_importances[:18]

#log transform 
fig_feature_importances['log10_value'] = np.log10(fig_feature_importances.loc[:,'importance']) 
log_features = fig_feature_importances



def case_features():
    fig = go.Figure(go.Bar(
            x=log_features["log10_value"],
            y=log_features["feature"],
            orientation='h'))
    fig.update_layout(yaxis=dict(autorange="reversed"))
    return fig 

