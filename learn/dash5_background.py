from dash import Dash, dcc, html ,Input, Output
import dash_bootstrap_components as dbc
from datetime import datetime
import pytz 

app = Dash(__name__, 
           external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME])

background_style = {
            # "background-color": "rgba(___, ___, ___, 1)",
            "background-size":"cover",
            "background-position":"center",
            "background-attachment":"fixed",
      }

app.layout = html.Div(
                children=[
                    html.Div([
                        html.H2("Weather Dashboard")
                    ],),
                    html.Div([
                        html.Div(id="time",),
                        html.Div(id="date",),
                        dcc.Interval(id="clock", interval=1000),
                    ],),
                ],style=background_style)
        
@app.callback(Output("time", "children"), 
            Input("clock", "n_intervals"))
def update_time(n):
    tz = pytz.timezone('Asia/Bangkok')
    current_time = datetime.now(tz).strftime("%I:%M:%S %p")
    return current_time

@app.callback(Output("date", "children"), 
            Input("clock", "n_intervals"))
def update_time(n):
    tz = pytz.timezone('Asia/Bangkok')
    current_date = datetime.now(tz).strftime("%a %d %B %Y")
    return current_date

if __name__ == "__main__":
    app.run_server(debug=True)