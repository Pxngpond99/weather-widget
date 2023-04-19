from dash import Dash, dash, dcc, html ,Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from datetime import datetime
import pytz #time zone
import plotly.graph_objects as go
import random
import dash

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME])
df = px.data.gapminder()
# style

dashboard_template = {
    "textAlign":"center",
    "padding":"1em 0 1em 0"
}

dashboard_name = {
    "font-size":"3em",
    "font-weight":"bold",
    "color":"rgba(255, 255, 255, 1)",
    "text-shadow": "2px 2px #000000",
}

date_and_time = {
    "textAlign":"center",
    "margin-top":"2em",
}

time_template = {
    "font-size":"3em",
    "font-weight":"bold",
    "color":"rgba(255, 255, 255, 1)",
    "text-shadow": "2px 2px #000000"
}

date_template = {
    "font-size":"1.5em",
    "font-weight":"bold",
    "color":"rgba(255, 255, 255,1)",
    "text-shadow": "2px 2px #000000"
}

gauge = {
    "background-color":"rgba(179, 218, 255,.5)",
    "border-radius":"25px",
    "textAlign":"center",
    "display":"inline-block",
    "margin":"2em",
    "width": "32vw", 
    "height": "38vh",
    "text-shadow":"2px 2px 2px #000000",
}

item = {
    "background-color":"rgba(179, 218, 255,.5)",
    "grid-template-columns":"auto",
    "display":"grid",
    "row-gap":"2.7vw",
    "padding":"0 0 3vh 0",
    "border-radius":"25px",
    "textAlign":"center",
    "color":"rgba(255, 255, 255,1)",
    'text-shadow': '2px 1px #000000',
    "font-size":"17px"
}

items = {
    "grid-template-columns":"auto auto auto auto auto",
    "height":"20vh",
    "width":"90vw",
    "padding":"5vh 5vw 0 5vw",
    "display":"grid",
    "column-gap":"5vw",
}

graph = {
    "margin-top":"20em",
    "padding":"1em 3em 3em 3em",
}

change_graph = {
}

change_graph_template = {
    "display": "flex",
    "justify-content": "space-around",
    "margin-bottom":"1em"
}

app.layout = html.Div(
    children=[
        html.Div([
            html.H2("Weather Dashboard",style=dashboard_name)
        ], style=dashboard_template),

        html.Div([
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.Div(id="time",style=time_template),
                        html.Div(id="date",style=date_template),
                        html.Div(className="fa-sharp fa-light fa-hourglass-clock"),
                        dcc.Interval(id="clock", interval=1000),
                    ],style=date_and_time)
                ],md=3),

                dbc.Col([
                    html.Div([
                        dcc.Graph(id="gauge-temp",style=gauge),
                        dcc.Graph(id="gauge-humidity",style=gauge),
                        dcc.Graph(id="gauge-light",style=gauge),
                        dcc.Graph(id="gauge-rain",style=gauge),
                        dcc.Interval(id="interval", interval=30 * 1000, n_intervals=0),
                    ])
                ],md=9)
            ]),
        ]),
        
        html.Div([
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.Div(id="time-now"),
                        html.Div("icon"),
                        html.Div("light"),
                        html.Div("temperature"),
                        html.Div("humidity"),
                        html.Div("rain")
                    ],style=item),
                    html.Div([
                        html.Div(id="time-next-1"),
                        html.Div("icon"),
                        html.Div("light"),
                        html.Div("temperature"),
                        html.Div("humidity"),
                        html.Div("rain")
                    ],style=item)
                ],style=items)
            ]),
        ]),

        html.Div([
            dbc.Row(
                dbc.CardBody(
                    [
                        html.Div([
                            html.Div(
                                dbc.Button("Temperature",id="temperature_graph",n_clicks=0),
                            style=change_graph),
                            html.Div(
                                dbc.Button("Humidity",id="humidity_graph",n_clicks=0),
                            style=change_graph),
                            html.Div(
                                dbc.Button("Light",id="light_graph",n_clicks=0),
                            style=change_graph)
                        ],style=change_graph_template),
                        
                        html.Div([
                            dcc.Graph(id='live-graph')
                        ]),
                    ]
                ),
            style=graph)
        ])

    ],id="image-title"
)

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


app.clientside_callback(
    """
    function(n) {          
    const now = new Date();
    const hour = now.getHours();
    let message = "";

    if (hour >= 8 && hour <= 16) {
        message = "url('static/day.jpg')";
    } else if (hour >= 6 && hour <= 8) {
        message = "url('static/morning.jpg')";
    } else if (hour >= 16 && hour <= 18) {
        message = "url('static/morning.jpg')";
    } else {
        message = "url('static/night.jpg')"
    }

     return {
            "background-image": message,
            "background-size":"cover",
            "background-position":"center",
            "background-attachment":"fixed",
      };
    }
    """,
    Output('image-title', 'style'),
    Input('clock', 'n_intervals'),
)


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
                 {'range': [0, 20], 'color': "#4682B4"},
                 {'range': [20, 35], 'color': "#87CEFA"},
                 {'range': [35, 60], 'color': "#FF7F50"}],
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
    title = {'text': "Humidity"},
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
    title = {'text': "Light"},
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
    title = {'text': "Rain"},
    delta = {'reference': 80,'increasing': {'color': "#7FFF00"}},
    gauge = {'axis': {'range': [0, 100], 'tickwidth': 1,'tickcolor': "rgba(255, 255, 255,1)","dtick":10},
             'bar': {'color': "#FFD700"},
             'bgcolor': "white",
             'steps' : [
                 {'range': [0, 25], 'color': "#696969"},
                 {'range': [25, 60], 'color': "#F0FFFF"},],
             'threshold' : {'line': {'color': "rgba(0,0,0,0)", 'width': 4}, 'thickness': 0.75, 'value': 100}},
    ))
    fig_rain.update_layout(paper_bgcolor = "rgba(0,0,0,0)",font = {'color': "rgba(255, 255, 255,1)",})
    return fig_rain


@app.callback(Output('live-graph', 'figure'),
              [Input('temperature_graph', 'n_clicks'), 
               Input('humidity_graph', 'n_clicks'),
               Input('light_graph', 'n_clicks')])

def update_graph(button1_clicks, button2_clicks, button3_clicks):
    ctx = dash.callback_context
    if not ctx.triggered:
        graph_id = 'temperature_graph'
    else:
        graph_id = ctx.triggered[0]['prop_id'].split('.')[0]
        print(ctx.triggered)

    if graph_id == 'temperature_graph':
        fig = px.scatter(df, x="gdpPercap", y="lifeExp", size="pop",
                         color="continent", log_x=True, hover_name="country",
                         size_max=60)
        
    elif graph_id == 'humidity_graph':
        fig = px.scatter(df, x="gdpPercap", y="lifeExp",
                        color="continent", log_x=True, hover_name="country",
                        size_max=60)
    else:
        fig = px.scatter(df, x="lifeExp", y="gdpPercap", size="pop",
                         color="continent", log_y=True, hover_name="country",
                         size_max=60)
        
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)