from dash import Dash, dcc, html ,Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import dash
from datetime import datetime
import pytz #time zone
import plotly.graph_objects as go
import random
from pycaret.classification import *

from data import value_temperature
from data import value_humidity
from data import value_light
from data import value_raindrop

from data_graph import value_temperature_graph
from data_graph import value_humidity_graph
from data_graph import value_light_graph



app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME])

df_tem = value_temperature_graph()
df_hum = value_humidity_graph()
df_light = value_light_graph()


model = load_model("ada_model")
# style

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

prediction_item = {
    "background-color":"rgba(179, 218, 255,.5)",
    "grid-template-columns":"auto",
    "display":"grid",
    "row-gap":"2.7vw",
    "padding":"5vh 0 3vh 0",
    "border-radius":"25px",
    "textAlign":"center",
    "color":"rgba(255, 255, 255,1)",
    'text-shadow': '2px 1px #000000',
    "font-size":"2em",
    "font-weight":"bold",
}

item_template = {
    "grid-template-columns":"auto auto",
    "height":"70vh",
    "width":"70vw",
    "padding":"8vh 5vw 0 5vw",
    "display":"grid",
    "column-gap":"8vw",
}

item_center = {
    "display":"flex",
    "justify-content": "center",
}

item_image = {
    "width": "15vw", 
    "height": "auto",
}

item_button = {
    "background-image": "linear-gradient(to bottom, #80EBD9, #08C8A8)",
    "color": "white",
    "border-radius": "20px",
    "border": "1px solid #08C8A8",
    "padding": "12px 24px",
    "font-size": "1.2rem",
    "font-weight": "600",
    "box-shadow": "0px 4px 4px rgba(0, 0, 0, 0.25)",
    "transition": "all 0.3s ease",
    "width": "15vw",
}

item_input = {
    "textAlign": "center",
    "border-radius": "15px",
    "align-items": "center",
    "display": "inline",
    "fontSize": 22,
    "width": "15vw",
}

change_graph_template = {
    "display": "flex",
    "flex-wrap":"wrap",
    "justify-content": "space-around",
    "margin-bottom":"1em"
}

icon_button = {
    "margin":"0.2em", 
    "font-size":"1.5rem"
}
    
graph_button = {
    "background-image": "linear-gradient(to bottom, #B7E3FF, #08A2BD)",
    "color": "white",
    "border-radius": "20px",
    "border": "1px solid #08A2BD",
    "padding": "12px 24px",
    "font-size": "1.2rem",
    "font-weight": "600",
    "box-shadow": "0px 4px 4px rgba(0, 0, 0, 0.25)",
    "transition": "all 0.3s ease",
    "justify-content": "center",
    "textAlign":"center",
}

graph = {
    "padding":"28em 3em 3em 3em",
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
                    ])
                ],md=9)
            ]),
        ]),
        
        html.Div([
            dbc.Row(
                html.Div([
                    html.Div([
                        html.Div(id="time-next-1"),
                        dcc.Input(id='input_tem_1', value='', type='text', placeholder='Enter Temperature',style=item_input, className="mx-auto"),
                        dcc.Input(id='input_hum_1', value='', type='text', placeholder='Enter Humidity',style=item_input, className="mx-auto"),
                        dcc.Input(id='input_light_1', value='', type='text', placeholder='Enter Light',style=item_input, className="mx-auto"),
                        html.Div(id="rain_icon_next-1"),
                        dbc.Button([
                            html.Div(className="fa-solid fa-cloud",
                                        style=icon_button),
                            "Submit"],
                            className="mx-auto",
                            id="submit-next-1",
                            n_clicks=0,
                            style=item_button
                        ),
                    ],style=prediction_item),
                    html.Div([
                        html.Div(id="time-next-2"),
                        dcc.Input(id='input_tem_2', value='', type='text', placeholder='Enter Temperature',style=item_input, className="mx-auto"),
                        dcc.Input(id='input_hum_2', value='', type='text', placeholder='Enter Humidity',style=item_input, className="mx-auto"),
                        dcc.Input(id='input_light_2', value='', type='text', placeholder='Enter Light',style=item_input, className="mx-auto"),
                        html.Div(id="rain_icon_next-2"),
                        dbc.Button([
                            html.Div(className="fa-solid fa-umbrella",
                                        style=icon_button),
                            "Submit"],
                            className="mx-auto",
                            id="submit-next-2",
                            n_clicks=0,
                            style=item_button
                        ),
                    ],style=prediction_item)
                ],style=item_template),
            style=item_center)
        ]),

        html.Div([
            dbc.Row(
                dbc.CardBody(
                    [
                        html.Div([
                            html.Div(
                                dbc.Button([
                                    html.Div(className="fa-solid fa-temperature-quarter fa-bounce",
                                                style=icon_button),
                                    "Temperature"],
                                    id="temperature_graph",
                                    n_clicks=0,
                                    style=graph_button),
                            ),
                            html.Div(
                                dbc.Button([
                                    html.Div(className="fa-solid fa-droplet fa-bounce",
                                                style=icon_button),
                                    "Humidity"],
                                    id="humidity_graph",
                                    n_clicks=0,
                                    style=graph_button),
                            ),
                            html.Div(
                                dbc.Button([
                                    html.Div(className="fa-solid fa-sun fa-bounce",
                                                style=icon_button),
                                    "Light"],             
                                    id="light_graph",
                                    n_clicks=0,
                                    style=graph_button)
                            )
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


@app.callback(Output('image-title', 'style'),
            Input('clock', 'n_intervals'))
def update_time(n):
    tz = pytz.timezone('Asia/Bangkok')
    hour = int(datetime.now(tz).strftime("%H"))
    if (hour >= 8 and hour <= 16) :
        message = "url('static/background/day.jpg')"
    elif (hour >= 6 and hour <= 8) :
        message = "url('static/background/mornin.jpg')"
    elif (hour >= 16 and hour <= 18) :
        message = "url('static/background/morning.jpg')"
    else :
        message = "url('static/background/night.jpg')"
    return {
            "background-image": message,
            "background-size":"cover",
            "background-position":"center",
            "background-attachment":"fixed"
      }


@app.callback(
    Output('gauge-temp', 'figure'),
    Input("interval", "n_intervals")
)
def update_output(value):
    fig_temp = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = value_temperature(),
    mode = "gauge+number+delta",
    title = {'text': "Temperature (°C)"},
    delta = {'reference': 40,'increasing': {'color': "#7FFF00"}},
    gauge = {'axis': {'range': [0, 40], 'tickwidth': 1,'tickcolor': "rgba(255, 255, 255,1)","dtick":10},
             'bar': {'color': "#F56161", "line" : {"width":0}} ,
             'bgcolor': "white",
             'steps' : [
                 {'range': [0, 15], 'color': "#61D4FF"},
                 {'range': [15, 25], 'color': "#68FF61"},
                 {'range': [25, 35], 'color': "#FFFA61"},
                 {'range': [35, 45], 'color': "#FF6161"},],
             'threshold' : {'line': {'color': "rgba(0,0,0,0)", 'width': 4}, 'thickness': 0.75, 'value': 60}},
    ))
    fig_temp.update_layout(paper_bgcolor = "rgba(0,0,0,0)",font = {'color': "rgba(255, 255, 255,1)"})
    return fig_temp

@app.callback(
    Output('gauge-humidity', 'figure'),
    Input("interval", "n_intervals")
)
def update_output(value):
    fig_humidity = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = value_humidity(),
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
    Input("interval", "n_intervals"),
)
def update_output(value):
    fig_light = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = value_light(),
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
    Input("clock", "n_intervals")
)
def update_output(value):
    fig_rain = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = value_raindrop(),
    mode = "gauge+number+delta",
    title = {'text': "Raindrop (%)"},
    delta = {'reference': 80,'increasing': {'color': "#7FFF00"}},
    gauge = {'axis': {'range': [0, 100], 'tickwidth': 1,'tickcolor': "rgba(255, 255, 255,1)","dtick":10},
             'bar': {'color': "#29D6E4"},
             'bgcolor': "white",
             'steps' : [
                 {'range': [0, 35], 'color': "#F1F1F1"},
                 {'range': [35, 70], 'color': "#3687DE"},
                 {'range': [70, 100], 'color': "#44698E"}],
             'threshold' : {'line': {'color': "rgba(0,0,0,0)", 'width': 4}, 'thickness': 0.75, 'value': 100}},
    ))
    fig_rain.update_layout(paper_bgcolor = "rgba(0,0,0,0)",font = {'color': "rgba(255, 255, 255,1)",})
    return fig_rain


@app.callback(Output("time-next-1", "children"), 
            Input("clock", "n_intervals"))
def update_time(n):
    tz = pytz.timezone('Asia/Singapore')
    current_time = datetime.now(tz).strftime("%I:00 %p")
    return current_time

@app.callback(Output("time-next-2", "children"), 
            Input("clock", "n_intervals"))
def update_time(n):
    tz = pytz.timezone('Asia/Tokyo')
    current_time = datetime.now(tz).strftime("%I:00 %p")
    return current_time

@app.callback(Output('rain_icon_next-1', 'children'),
            [Input('input_tem_1', 'value'),
            Input('input_hum_1', 'value'),
            Input('input_light_1', 'value'),
            Input("submit-next-1","n_clicks")]
)
def update_time(input1_value, input2_value, input3_value,n_click):
    ctx = dash.callback_context
    tz = pytz.timezone('Asia/Singapore')
    current_time = datetime.now(tz).strftime("%H")
    score = 0
    if "submit-next-1" == ctx.triggered_id:
        data = pd.DataFrame({'Temp9am': float(input1_value),
                            'Humidity9am': float(input2_value),
                            'Sunshine': float(input3_value)}, index=[1])
        value = predict_model(model, data)

        label = value["prediction_label"].item()
        score = value["prediction_score"].item() * 100
        if label == "No":
            score = 100 - score
    if (score < 20):
        if int(current_time) >= 6 and int(current_time) <= 18:
            message = "static/icon/sun.png"
        else :
            message = "static/icon/moon.png"
    elif (score < 40):
        if int(current_time) >= 6 and int(current_time) <= 18:
            message = "static/icon/day_cloudy.png"
        else :
            message = "static/icon/night_cloudy.png"
    elif (score < 60):
        if int(current_time) >= 6 and int(current_time) <= 18:
            message = "static/icon/day_rain.png"
        else :
            message = "static/icon/night_rain.png"
    elif (score < 80):
        message = "static/icon/rainy.png"
    elif (score <= 100):
        message = "static/icon/storm.png"

    return html.Div([html.Img(src=message, style=item_image), html.H4(f"Raindrop {score:.2f} %",style={"padding":"2em 0 0 0"})])

@app.callback(Output('rain_icon_next-2', 'children'),
            [Input('input_tem_2', 'value'),
            Input('input_hum_2', 'value'),
            Input('input_light_2', 'value'),
            Input("submit-next-2","n_clicks")])
def update_time(input1_value, input2_value, input3_value,n_click):
    ctx = dash.callback_context
    tz = pytz.timezone('Asia/Tokyo')
    current_time = datetime.now(tz).strftime("%H")
    score = 0
    if "submit-next-2" == ctx.triggered_id:
        data = pd.DataFrame({'Temp9am': float(input1_value),
                            'Humidity9am': float(input2_value),
                            'Sunshine': float(input3_value)}, index=[1])
        value = predict_model(model, data)
        label = value["prediction_label"].item()
        score = value["prediction_score"].item() * 100
        if label == "No":
            score = 100 - score
    if (score < 20):
        if int(current_time) >= 6 and int(current_time) <= 18:
            message = "static/icon/sun.png"
        else :
            message = "static/icon/moon.png"
    elif (score < 40):
        if int(current_time) >= 6 and int(current_time) <= 18:
            message = "static/icon/day_cloudy.png"
        else :
            message = "static/icon/night_cloudy.png"
    elif (score < 60):
        if int(current_time) >= 6 and int(current_time) <= 18:
            message = "static/icon/day_rain.png"
        else :
            message = "static/icon/night_rain.png"
    elif (score < 80):
        message = "static/icon/rainy.png"
    elif (score <= 100):
        message = "static/icon/storm.png"

    return html.Div([html.Img(src=message, style=item_image), html.H4(f"Raindrop {score:.2f} %",style={"padding":"2em 0 0 0"})])

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

    if graph_id == 'temperature_graph':
        fig = px.bar(df_tem, x="time", y="value", color="time", title="Temperature",
                    labels={'value':'Temperature (°C)', 'time':'Time'})
        
    elif graph_id == 'humidity_graph':
        fig = px.line(df_hum, x='time', y='value', color='time', symbol="time", markers=True, 
                      title="Humidity", labels={'value':'Humidity (%)', 'time':'Time'})

    else:
        fig = px.scatter(df_light, x="time", y="value", color="time", title="Light",
                    size='value', size_max=25, labels={'value':'Light (%)', 'time':'Time'})
        
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)