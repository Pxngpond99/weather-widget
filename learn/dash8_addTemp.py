from dash import Dash, dcc, html ,Input, Output
import dash_bootstrap_components as dbc
from datetime import datetime
import pytz 
import plotly.graph_objects as go
import random

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

# ________ = {
#     "background-color":"rgba(179, 218, 255,.5)",
#     "border-radius":"25px",
#     "textAlign":"center",
#     "display":"inline-block",
#     "margin":"2em",
#     "width": "32vw", 
#     "height": "38vh",
#     "text-shadow":"2px 2px 2px #000000",
# }

app.layout = html.Div(
                children=[
                    html.Div([
                        html.H2("Weather Dashboard",style=head_style)
                    ], style=head_template),

                    html.Div([
                        dbc.Row([
                            dbc.Col([
                                html.Div([
                                    html.Div(id="time",style=time_style),
                                    html.Div(id="date",style=date_style),
                                    dcc.Interval(id="clock", interval=1000),
                                ],style=date_and_time)
                            ],md=3),

                            dbc.Col([
                                html.Div([
                                    # dcc.Graph(id="________",style=gauge_style),
                                    # dcc.Interval(id="_________", interval=______, n_intervals=0),
                                ]),
                            ],md=9),
                        ]),
                    ]),
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

# @app.callback(
#     Output('gauge-temp', 'figure'),
#     Input("interval", "n_intervals")
# )
# def update_output(value):
#     value = random.randrange(0, 60)
#     fig_temp = go.Figure(go.Indicator(
#     domain = {'x': [0, 1], 'y': [0, 1]},
#     value = value,
#     mode = "gauge+number+delta",
#     title = {'text': "_____________"},
#     delta = {'reference': 40,'increasing': {'color': "#7FFF00"}},
#     gauge = {'axis': {'range': [0, 60], 'tickwidth': 1,'tickcolor': "rgba(___,___,___,1)","dtick":___},
#              'bar': {'color': "#7CFC00", "line" : {"width":0}} ,
#              'bgcolor': "white",
#              'steps' : [
#                  {'range': [0, 20], 'color': "#F0FFFF"},
#                  {'range': [20, 40], 'color': "#87CEFA"},
#                  {'range': [40, 60], 'color': "#FFA07A"}],
#              'threshold' : {'line': {'color': "rgba(0,0,0,0)", 'width': 4}, 'thickness': 0.75, 'value': 60}},
#     ))
#     fig_temp.update_layout(paper_bgcolor = "rgba(___,___,___,1)",font = {'color': "rgba(___,___,___,1)"})
#     return fig_temp

if __name__ == "__main__":
    app.run_server(debug=True)