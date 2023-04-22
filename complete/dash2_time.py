from dash import Dash, dcc, html ,Input, Output
import dash_bootstrap_components as dbc
from datetime import datetime
import pytz 

app = Dash(__name__, 
           external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME])

app.layout = html.Div([html.Div(id="time"),
                     dcc.Interval(id="clock", interval=1000),])

@app.callback(Output("time", "children"), 
            Input("clock", "n_intervals"))
def update_time(n):
    tz = pytz.timezone('Asia/Bangkok')
    current_time = datetime.now(tz).strftime("%I:%M:%S %p")
    return current_time
 
if __name__ == "__main__":
    app.run_server(debug=True)