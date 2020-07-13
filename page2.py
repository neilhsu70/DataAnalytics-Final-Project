import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from navbar import dash_navbar
from tally_cards import tallies, title_authors

nav = dash_navbar()
titleauthors = title_authors()
tallycards = tallies()

#global confirmed, recovered and deaths row
container = dbc.Card([dbc.CardBody([dbc.Container([ 
            html.H1(children='This is where we can link tableau, maybe with an image of visualization?', className='mt-5 py-4 pb-3 text-center')
            ])])])


