import dash
from dash import html as html
from dash import dcc as dcc
import plotly.graph_objects as go
import plotly.express as px
app = dash.Dash()   #initialising dash app
df = px.data.stocks() #reading stock price dataset 

def stock_prices():
    # Function for creating line chart showing Google stock prices over time 
    fig = go.Figure([go.Scatter(x = df['date'], y = df['GOOG'],\
                     line = dict(color = 'firebrick', width = 4), name = 'Google')
                     ])
    fig.update_layout(title = 'Prices over time',
                      xaxis_title = 'Dates',
                      yaxis_title = 'Prices'
                      )
    return fig  

 
app.layout = html.Div(id = 'parent', children = [
    html.H1(id = 'H1', children = 'Styling using html components', style = {'textAlign':'center',\
                                            'marginTop':40,'marginBottom':40}),

        
        dcc.Graph(id = 'line_plot', figure = stock_prices())    
    ]
                     )