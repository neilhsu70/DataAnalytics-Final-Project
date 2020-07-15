import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from USpage import app_covid
from case_page import case_covid 
from homepage import Homepage

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.JOURNAL])

app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id = 'url', refresh = False),
    html.Div(id = 'page-content')
])

@app.callback(Output('page-content', 'children'),
            [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/US':
        return app_covid()
    elif pathname == '/Case':
        return case_covid()
    else:
        return Homepage()

if __name__ == '__main__':
    app.run_server(debug=True)
    



