from dash import Dash, dcc, html ,Input, Output
import dash_bootstrap_components as dbc
from datetime import datetime
import pytz 

app = Dash(__name__, 
           external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME])

background_style = {
            "background-color": "rgba(100, 149, 237, 1)",
            "background-size":"cover",
            "background-position":"center",
            "background-attachment":"fixed",
      }

head_style = {
    "font-size":"3em",
    "font-weight":"bold",
    "color":"rgba(255, 255, 255, 1)",
    "text-shadow": "2px 2px #000000",
}

head_template = {
    "textAlign":"center",
    "padding":"2em"
}

date_and_time = {
    "textAlign":"center",
    "margin-top":"2em",
}

time_style = {
    "font-size":"3em",
    "font-weight":"bold",
    "color":"rgba(255, 255, 255, 1)",
    "text-shadow": "2px 2px #000000"
}

date_style = {
    "font-size":"1.5em",
    "font-weight":"bold",
    "color":"rgba(255, 255, 255,1)",
    "text-shadow": "2px 2px #000000"
}

app.layout = html.Div(
                children=[
                    html.Div([
                        html.H2("Weather Dashboard",style=head_style)
                    ],style=head_template),
                    html.Div([
                        html.Div(id="time",style=time_style),
                        html.Div(id="date",style=date_style),
                        dcc.Interval(id="clock", interval=1000),
                    ],style=date_and_time),
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