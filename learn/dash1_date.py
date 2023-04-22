from dash import Dash, dcc, html ,Input, Output
import dash_bootstrap_components as dbc
from datetime import datetime
import pytz 

app = Dash(__name__, 
           external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME])

app.layout = html.Div([html.Div(id="date"),
                     dcc.Interval(id="clock", interval=1000),])

@app.callback(Output("date", "children"), 
            Input("clock", "n_intervals"))
def update_time(n):
    tz = pytz.timezone('Asia/Bangkok')
    current_date = datetime.now(tz).strftime("%a %d %B %Y")
    return current_date

if __name__ == "__main__":
    app.run_server(debug=True)