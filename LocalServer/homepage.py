import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from navbar import dash_navbar
from page1 import tallies, title_authors, bubble_animation_col, global_line_graph, footer_row


nav = dash_navbar()
titleauthors = title_authors()
tallycards = tallies()
bubble_animation_col = bubble_animation_col()
global_line_graph = global_line_graph()
footer = footer_row()

def Homepage():
    layout = html.Div([
    nav,
    titleauthors,
    tallycards, 
    bubble_animation_col, 
    global_line_graph,
    footer
    ])
    return layout 
#to test if running uncomment below: 
app = dash.Dash(__name__, external_stylesheets = [dbc.themes.JOURNAL])
app.layout = Homepage()
if __name__ == "__main__":
    app.run_server(debug=True)



