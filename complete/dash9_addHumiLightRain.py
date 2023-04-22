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

gauge_style = {
    "background-color":"rgba(179, 218, 255,.5)",
    "border-radius":"25px",
    "textAlign":"center",
    "display":"inline-block",
    "margin":"2em",
    "width": "32vw", 
    "height": "38vh",
    "text-shadow":"2px 2px 2px #000000",
}

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
                                    dcc.Graph(id="gauge-temp",style=gauge_style),
                                    dcc.Graph(id="gauge-humidity",style=gauge_style),
                                    dcc.Graph(id="gauge-light",style=gauge_style),
                                    dcc.Graph(id="gauge-rain",style=gauge_style),
                                    dcc.Interval(id="interval", interval=30 * 1000, n_intervals=0),
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

@app.callback(
    Output('gauge-temp', 'figure'),
    Input("interval", "n_intervals")
)
def update_output(value):
    value = random.randrange(0, 60)
    fig_temp = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = value,
    mode = "gauge+number+delta",
    title = {'text': "Temperature (°C)"},
    delta = {'reference': 40,'increasing': {'color': "#7FFF00"}},
    gauge = {'axis': {'range': [0, 60], 'tickwidth': 1,'tickcolor': "rgba(255, 255, 255,1)","dtick":10},
             'bar': {'color': "#7CFC00", "line" : {"width":0}} ,
             'bgcolor': "white",
             'steps' : [
                 {'range': [0, 20], 'color': "#F0FFFF"},
                 {'range': [20, 40], 'color': "#87CEFA"},
                 {'range': [40, 60], 'color': "#FFA07A"}],
             'threshold' : {'line': {'color': "rgba(0,0,0,0)", 'width': 4}, 'thickness': 0.75, 'value': 60}},
    ))
    fig_temp.update_layout(paper_bgcolor = "rgba(0,0,0,0)",font = {'color': "rgba(255, 255, 255,1)"})
    return fig_temp

@app.callback(
    Output('gauge-humidity', 'figure'),
    Input("interval", "n_intervals")
)
def update_output(value):
    value = random.randrange(0, 100)
    fig_humidity = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = value,
    mode = "gauge+number+delta",
    title = {'text': "Humidity (%)"},
    delta = {'reference': 40,'increasing': {'color': "#7FFF00"}},
    gauge = {'axis': {'range': [0, 100], 'tickwidth': 1,'tickcolor': "rgba(255, 255, 255,1)","dtick":10},
             'bar': {'color': "darkblue"},
             'bgcolor': "white",
             'steps' : [
                 {'range': [0, 20], 'color': "#F8F8FF"},
                 {'range': [20, 60], 'color': "#E0FFFF"},
                 {'range': [60, 100], 'color':" #87CEFA"},],
             'threshold' : {'line': {'color': "rgba(0,0,0,0)", 'width': 4}, 'thickness': 0.75, 'value': 100}},
    ))
    fig_humidity.update_layout(paper_bgcolor = "rgba(0,0,0,0)",font = {'color': "rgba(255, 255, 255,1)"})
    return fig_humidity

@app.callback(
    Output('gauge-light', 'figure'),
    Input("interval", "n_intervals")
)
def update_output(value):
    value = random.randrange(0, 100)
    fig_light = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = value,
    mode = "gauge+number+delta",
    title = {'text': "Light (%)"},
    delta = {'reference': 80,'increasing': {'color': "#7FFF00"}},
    gauge = {'axis': {'range': [0, 100], 'tickwidth': 1,'tickcolor': "rgba(255, 255, 255,1)","dtick":10},
             'bar': {'color': "#FFD700"},
             'bgcolor': "white",
             'steps' : [
                 {'range': [0, 25], 'color': "#696969"},
                 {'range': [25, 60], 'color': "#F0FFFF"},],
             'threshold' : {'line': {'color': "rgba(0,0,0,0)", 'width': 4}, 'thickness': 0.75, 'value': 100}},
    ))
    fig_light.update_layout(paper_bgcolor = "rgba(0,0,0,0)",font = {'color': "rgba(255, 255, 255,1)",})
    return fig_light

@app.callback(
    Output('gauge-rain', 'figure'),
    Input("interval", "n_intervals")
)
def update_output(value):
    value = random.randrange(0, 100)
    fig_rain = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = value,
    mode = "gauge+number+delta",
    title = {'text': "Raindrop (%)"},
    delta = {'reference': 80,'increasing': {'color': "#7FFF00"}},
    gauge = {'axis': {'range': [0, 100], 'tickwidth': 1,'tickcolor': "rgba(255, 255, 255,1)","dtick":10},
             'bar': {'color': "#00FFFF"},
             'bgcolor': "white",
             'steps' : [
                 {'range': [0, 50], 'color': "#F0FFFF"},
                 {'range': [50, 100], 'color': "#87CEFA"},],
             'threshold' : {'line': {'color': "rgba(0,0,0,0)", 'width': 4}, 'thickness': 0.75, 'value': 100}},
    ))
    fig_rain.update_layout(paper_bgcolor = "rgba(0,0,0,0)",font = {'color': "rgba(255, 255, 255,1)",})
    return fig_rain

if __name__ == "__main__":
    app.run_server(debug=True)