Data Visualization - Final Project

Members:

Young Jung Choi

Ning Ning Du

Bianca Hernandez

Neil Hsu

We plan on building on our previous Covid-19 project by adding machine learning algorithms. We hope to develop a predictive model that will give us insight into how the virus will continues to affect our world.

Data sources:

Johns Hopkins Covid dataset

https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv

Texas Health & Human Services / Texas Department of State Health Services - specific data on Texas infection and fatalities

https://txdshs.maps.arcgis.com/apps/opsdashboard/index.html#/ed483ecd702b4298ab01e8b9cafc8b83

Technologies used:

Dash

Postgres Database server on AWS

Plotly

How we'll integrate Machine Learning algorithms

Regression algorithem:

Projections on infections and fatalities and possibly recoveries

Classification algorithms: 

To determine wether social distancing / mandatory mask policies have been effective. We'll have to take into account the 2 week incubation time. Also to compare state data.


End User interaction

We plan on making our model interactive by allowing the end user select the location of the visualizations so the end user can see how covid is progressing in certain locations and predict how covid will progress in the future. We'll use MLFlow to make our model portable.

