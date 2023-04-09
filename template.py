from dash import Dash, dcc, html ,Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME])


# background_templates = {"background-image":"url('static/day.jpg')",
#                         "background-position":"center bottom",
#                         "background-repeat":"no-repeat",
#                         "background-size":"cover",
#                         "height":"100vh",
#                         "width":"100vw",
#                         "position":"static",}

upper = {"height":"40vh",
         "width":"100vw",}

lower = {"grid-template-columns":"auto auto auto auto auto",
        "height":"50vh",
        "width":"90vw",
        "margin":"5vh 5vw",
        "display":"grid",
        "column-gap":"5vw"
        }
item = {"background-color":"rgba(179, 218, 255,.5)",
        "grid-template-columns":"auto",
        "display":"grid",
        "row-gap":"3vw",
        "padding":"3vh 0 3vh 0",
        "border-radius":"25px",
        "text-align":"center",
        "align-items": "center",
        "justify-content": "center",
        "color":"rgba(255, 255, 255,1)",
        'text-shadow': '2px 1px #000000' }

time_templates = {"background-color":"rgba(179, 218, 255,.5)",
                  "top":"5vh",
                  "margin-left":"5vw",
                  "height":"30vh",
                  "width":"40vw",
                  "position":"relative",
                  "font-size":"7vw",
                  "font-weight":"bold",
                  "color":"rgba(255, 255, 255,1)",
                  "text-align":"center",
                  "align-items": "center",
                  "display":"flex",
                  "justify-content": "center",
                  "border-radius":"25px",
                  "float":"left",
                  'text-shadow': '2px 2px #000000' }

date_templates = {"background-color":"rgba(179, 218, 255,.5)",
                  "top":"5vh",
                  "margin-left":"5vw",
                  "height":"18vh",
                  "width":"24vw",
                  "position":"relative",
                  "font-size":"3vw",
                  "font-weight":"bold",
                  "color":"rgba(255, 255, 255,1)",
                  "text-align":"center",
                  "align-items": "center",
                  "display":"flex",
                  "justify-content": "center",
                  "border-radius":"25px",
                  "float":"left",
                  'text-shadow': '2px 2px #000000'}


app.layout = html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(id="date-time-title",style=time_templates),
                    dcc.Interval(id="clock", interval=1000),
                    html.Div(id="date-title",style=date_templates)
                ],style=upper
            ),
            html.Div(
                children=[
                    html.Div(
                        children=[
                        html.Div("time"),
                        html.Div("icon"),
                        html.Div("temperature"),
                        html.Div("rain")],style=item
                    ),
                    html.Div(
                        children=[
                        html.Div("time"),
                        html.Div("icon"),
                        html.Div("temperature"),
                        html.Div("rain")],style=item
                    ),
                    html.Div(
                        children=[
                        html.Div("time"),
                        html.Div("icon"),
                        html.Div("temperature"),
                        html.Div("rain")],style=item
                    ),
                    html.Div(
                        children=[
                        html.Div("time"),
                        html.Div("icon"),
                        html.Div("temperature"),
                        html.Div("rain")],style=item
                    ),
                    html.Div(
                        children=[
                        html.Div("time"),
                        html.Div("icon"),
                        html.Div("temperature"),
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
    Output('date-time-title', 'children'),
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


if __name__ == "__main__":
    app.run_server(debug=True)