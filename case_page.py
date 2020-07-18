import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from navbar import dash_navbar
from page1 import tallies, title_authors, footer_row
from page3 import case_title, case_container, case_2, case_3


nav = dash_navbar()
case_study_title = case_title()
case_study_container = case_container()
case_study_container2 = case_2()
case_study_container3 = case_3()
footer = footer_row()

def case_covid():
    layout = html.Div([
        nav,
        case_study_title,
        case_study_container,
        case_study_container2,
        case_study_container3,
        footer
    ])
    return layout
#to test if running uncomment below: 
app = dash.Dash(__name__, external_stylesheets = [dbc.themes.JOURNAL])
app.layout = case_covid()
if __name__ == "__main__":
    app.run_server(debug=True)