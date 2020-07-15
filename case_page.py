import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from navbar import dash_navbar
from page1 import tallies, title_authors, footer_row
from page3 import case_container

nav = dash_navbar()
titleauthors = title_authors()
tallycards = tallies()
case_study_container = case_container()

footer = footer_row()

def case_covid():
    layout = html.Div([
        nav,
        titleauthors,
        tallycards,
        case_study_container,
        footer
    ])
    return layout
#to test if running uncomment below: 
app = dash.Dash(__name__, external_stylesheets = [dbc.themes.JOURNAL])
app.layout = case_covid()
if __name__ == "__main__":
    app.run_server(debug=True)