import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
from pandas import DataFrame
from statistics import median

import loadModel


# mean and standard deviation
mu_lat, sigma_lat = -4.17, 3
mu_long, sigma_long = -62, 3

df = pd.read_pickle("positions.pkl")
df = df.loc[1:689,:]

app = dash.Dash('Hello World')

   
app.layout = html.Div([
    html.H2('ADREEI', style={'text-align': 'center'}),
    html.Div([
        html.Div([
            html.Div([
            dcc.Dropdown(
                id='my-dropdown',
                options=[
                    {'label': 'Treinar', 'value': 'train'},
                    {'label': 'Gerar Rotas', 'value': 'route'},
                    {'label': 'Limpar', 'value': 'clean'}
                ],
                value='COKE'
            )], style={'width': '80%', 'display':'inline-block','vertical-align': 'middle'})
        ], style={'width': '20%', 'float': 'left', 'text-align':'center', 'height':'388px'}),
        html.Div([
            dcc.Graph(
                id='my-graph'
                )], style={'width': '80%', 'float': 'right', 'margin-top':'-12px'}
    )], style={'width': '100%', 'height':'388px'}),
    html.H2('Resultados', style={'text-align': 'center'})
], style={'width': '100%'})




@app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown_value):
    if(selected_dropdown_value == 'train'):
        scores = loadModel.predict()
        print(scores)
    elif(selected_dropdown_value == 'route'):
        s_lat=df.loc[:,1]
        s_long=df.loc[:,0]
    else:
        s_lat=df.loc[:,1]
        s_long=df.loc[:,0]
        rgb = [0,0,200]
    
    return {
            'data': [{
                'name': 'Invasora',
                'lat': s_lat[1:122], 
                'lon': s_long[1:122], 
                'type': 'scattermapbox',
                'marker': dict( size=5, color='rgb('+str(rgb[0])+',' +str(rgb[1])+',' +str(rgb[2])+')')
            },
            {
                'name': 'Não Invasora',
                'lat': s_lat[122:], 
                'lon': s_long[122:],
                'type': 'scattermapbox',
                'marker': dict( size=5, color='rgb('+str(rgb[0])+',' +str(rgb[1])+',' +str(rgb[2])+')')
            }],
        'layout': {
            'mapbox': {
                'accesstoken': (
                    'pk.eyJ1IjoiY2hyaWRkeXAiLCJhIjoiY2ozcGI1MTZ3M' +
                    'DBpcTJ3cXR4b3owdDQwaCJ9.8jpMunbKjdq1anXwU5gxIw'
                ),
                'center': {'lat': median(s_lat), 'lon': median(s_long)},
                'zoom': 3.5,
                'top': 0,
                'margin-top': 0
            },
            'margin': { 'l': 0, 'r': 0, 'b': 0, 't': 0 },
            'height': 400
        }
    }

app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

if __name__ == '__main__':
    app.run_server()




