import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from navbar import dash_navbar
from page1 import tallies, title_authors, footer_row
from page2 import container_box, container_box2

nav = dash_navbar()
titleauthors = title_authors()
tallycards = tallies()
tempbox1 = container_box()
tempbox2 = container_box2()
footer = footer_row()

def app_covid():
    layout = html.Div([
        nav,
        titleauthors,
        tallycards,
        tempbox1,
        tempbox2,
        footer
    ])
    return layout
#to test if running uncomment below: 
app = dash.Dash(__name__, external_stylesheets = [dbc.themes.JOURNAL])
app.layout = app_covid()
if __name__ == "__main__":
    app.run_server(debug=True)