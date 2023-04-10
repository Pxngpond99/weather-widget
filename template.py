from dash import Dash, dcc, html ,Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from datetime import datetime
import plotly.graph_objects as go

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME])


upper = {"height":"45vh",
         "width":"100vw",
         "top":"5vh",
         "grid-template-columns": "19vw 19vw 19vw 20vw",
         "display":"grid",
         "padding":"5vh 5vw 0 5vw",
         "column-gap":"4vw"}                  

lower = {"grid-template-columns":"auto auto auto auto auto",
        "height":"20vh",
        "width":"90vw",
        "margin":"5vh 5vw 0 5vw",
        "display":"grid",
        "column-gap":"5vw"
        }
item = {"background-color":"rgba(179, 218, 255,.5)",
        "grid-template-columns":"auto",
        "display":"grid",
        "row-gap":"2vw",
        "padding":"3vh 0 3vh 0",
        "border-radius":"25px",
        "text-align":"center",
        "align-items": "center",
        "justify-content": "center",
        "color":"rgba(255, 255, 255,1)",
        'text-shadow': '2px 1px #000000' }

date_time = {     "text-align":"center",
                  "align-items": "center",
                  "display":"flex",
                  "justify-content": "center",
                  "grid-template-columns":"auto",
                  "display":"grid",
                  'height': '40vh'
                  }

time_templates = {"background-color":"rgba(179, 218, 255,.5)",
                  "height":"13vh",
                  "width":"20vw",
                  "position":"relative",
                  "font-size":"3vw",
                  "font-weight":"bold",
                  "color":"rgba(255, 255, 255,1)",
                  "text-align":"center",
                  "align-items": "center",
                  "display":"flex",
                  "justify-content": "center",
                  "border-radius":"25px",
                  'text-shadow': '2px 2px #000000',
                  }

date_templates = {"background-color":"rgba(179, 218, 255,.5)",
                  "height":"13vh",
                  "width":"20vw",
                  "position":"relative",
                  "font-size":"3vw",
                  "font-weight":"bold",
                  "color":"rgba(255, 255, 255,1)",
                  "text-align":"center",
                  "align-items": "center",
                  "display":"flex",
                  "justify-content": "center",
                  "border-radius":"25px",
                  'text-shadow': '2px 2px #000000'}

gauge = {"background-color":"rgba(179, 218, 255,.5)",
         "border-radius":"25px",
         "text-align":"center",
        "align-items": "center",
        "display":"flex",
        "justify-content": "center",
        'width': '21vw', 
        'height': '40vh'}

gauge_templates = {'height': '37vh'}

app.layout = html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(dcc.Graph(id="gauge-temp",style=gauge_templates),style=gauge),
                    html.Div(dcc.Graph(id="gauge-humidity",style=gauge_templates),style=gauge),
                    html.Div(dcc.Graph(id="gauge-light",style=gauge_templates),style=gauge),
                    dcc.Interval(id="clock", interval=1000),
                    html.Div(children=[
                        html.Div(id="time-title",style=time_templates),
                        html.Div(id="date-title",style=date_templates),
                        ],style=date_time),
                ],style=upper
            ),
            html.Div(
                children=[
                    html.Div(
                        children=[
                        html.Div(id="time-now"),
                        html.Div("icon"),
                        html.Div("light"),
                        html.Div("temperature"),
                        html.Div("humidity"),
                        html.Div("rain")],style=item
                    ),
                    html.Div(
                        children=[
                        html.Div(id="time-next-1"),
                        html.Div("icon"),
                        html.Div("light"),
                        html.Div("temperature"),
                        html.Div("humidity"),
                        html.Div("rain")],style=item
                    ),
                    html.Div(
                        children=[
                        html.Div(id="time-next-2"),
                        html.Div("icon"),
                        html.Div("light"),
                        html.Div("temperature"),
                        html.Div("humidity"),
                        html.Div("rain")],style=item
                    ),
                    html.Div(
                        children=[
                        html.Div(id="time-next-3"),
                        html.Div("icon"),
                        html.Div("light"),
                        html.Div("temperature"),
                        html.Div("humidity"),
                        html.Div("rain")],style=item
                    ),
                    html.Div(
                        children=[
                        html.Div(id="time-next-4"),
                        html.Div("icon"),
                        html.Div("light"),
                        html.Div("temperature"),
                        html.Div("humidity"),
                        html.Div("rain")],style=item  
                    ),
                ],style=lower
            )
    ],id="image-title")




app.clientside_callback(
    """
    function(n) {          
        const local_time_str = new Date().toLocaleTimeString();                   
        return local_time_str
    }
    """,
    Output('time-title', 'children'),
    Input('clock', 'n_intervals'),
)

app.clientside_callback(
    """
    function(n) {          
        const local_date_str = new Date().toLocaleDateString();                   
        return  local_date_str
    }
    """,
    Output('date-title', 'children'),
    Input('clock', 'n_intervals'),
)

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
            "background-position":"center bottom",
            "background-repeat":"no-repeat",
            "background-size":"cover",
            "height":"100vh",
            "width":"100vw",
            "position":"static",
      };
    }
    """,
    Output('image-title', 'style'),
    Input('clock', 'n_intervals'),
)


app.clientside_callback(
    """
    function(n) {
        const now = new Date();
        const hour = now.getHours();
        const minutes = '00';
        const am_pm = hour >= 12 ? 'PM' : 'AM';
        const hour12 = hour % 12 || 12; 
        return hour12 + ':' + minutes + ' ' + am_pm;
    }
    """,
    Output('time-now', 'children'),
    Input('clock', 'n_intervals'),
)

app.clientside_callback(
    """
    function(n) {
        const now = new Date();
        const hour = now.getHours() + 1;
        const minutes = '00';
        const am_pm = hour >= 12 ? 'PM' : 'AM';
        const hour12 = hour % 12 || 12; 
        return hour12 + ':' + minutes + ' ' + am_pm;
    }
    """,
    Output('time-next-1', 'children'),
    Input('clock', 'n_intervals'),
)

app.clientside_callback(
    """
    function(n) {
        const now = new Date();
        const hour = now.getHours() + 2;
        const minutes = '00';
        const am_pm = hour >= 12 ? 'PM' : 'AM';
        const hour12 = hour % 12 || 12; 
        return hour12 + ':' + minutes + ' ' + am_pm;
    }
    """,
    Output('time-next-2', 'children'),
    Input('clock', 'n_intervals'),
)

app.clientside_callback(
    """
    function(n) {
        const now = new Date();
        const hour = now.getHours() + 3;
        const minutes = '00';
        const am_pm = hour >= 12 ? 'PM' : 'AM';
        const hour12 = hour % 12 || 12; 
        return hour12 + ':' + minutes + ' ' + am_pm;
    }
    """,
    Output('time-next-3', 'children'),
    Input('clock', 'n_intervals'),
)

app.clientside_callback(
    """
    function(n) {
        const now = new Date();
        const hour = now.getHours() + 4;
        const minutes = '00';
        const am_pm = hour >= 12 ? 'PM' : 'AM';
        const hour12 = hour % 12 || 12;
        return hour12 + ':' + minutes + ' ' + am_pm;
    }
    """,
    Output('time-next-4', 'children'),
    Input('clock', 'n_intervals'),
)

@app.callback(
    Output('gauge-temp', 'figure'),
    Input('clock', 'n_intervals')
)
def update_output(value):
    fig_temp = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = 38,
    mode = "gauge+number+delta",
    title = {'text': "Temperature"},
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
    fig_temp.update_layout(paper_bgcolor = "rgba(0,0,0,0)",font = {'color': "rgba(255, 255, 255,1)"},)
    return fig_temp

@app.callback(
    Output('gauge-humidity', 'figure'),
    Input('clock', 'n_intervals')
)
def update_output(value):
    fig_humidity = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = 80,
    mode = "gauge+number+delta",
    title = {'text': "Humidity"},
    delta = {'reference': 40,'increasing': {'color': "#7FFF00"}},
    gauge = {'axis': {'range': [0, 100], 'tickwidth': 1,'tickcolor': "rgba(255, 255, 255,1)","dtick":20},
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
    Input('clock', 'n_intervals')
)
def update_output(value):
    fig_light = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = 15,
    mode = "gauge+number+delta",
    title = {'text': "Light"},
    delta = {'reference': 80,'increasing': {'color': "#7FFF00"}},
    gauge = {'axis': {'range': [0, 100], 'tickwidth': 1,'tickcolor': "rgba(255, 255, 255,1)","dtick":20},
             'bar': {'color': "#FFD700"},
             'bgcolor': "white",
             'steps' : [
                 {'range': [0, 25], 'color': "#696969"},
                 {'range': [25, 60], 'color': "#F0FFFF"},],
             'threshold' : {'line': {'color': "rgba(0,0,0,0)", 'width': 4}, 'thickness': 0.75, 'value': 100}},
    ))
    fig_light.update_layout(paper_bgcolor = "rgba(0,0,0,0)",font = {'color': "rgba(255, 255, 255,1)",})
    return fig_light

if __name__ == "__main__":
    app.run_server(debug=True)