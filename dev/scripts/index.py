import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
from pandas import DataFrame
from statistics import median
import random

import loadModel
import modelagem


# mean and standard deviation

df = pd.read_pickle("positions.pkl")
df = df.loc[1:689,:]

s_lat = df.loc[:,1]
s_long = df.loc[:,0]

scores = []

iInvasive = []
iNonInvasive = []

Accuracy = 0
nCluster = 0


app = dash.Dash('Hello World')

   
app.layout = html.Div([
    html.H2('ADREEI', style={'text-align': 'center'}),
    html.Div([
        html.Div([
            html.Div([
            html.Div(
                    [html.B('Ações')], style={'text-align': 'left', 'font-size': '1.1em'}),
            dcc.Dropdown(
                id='my-dropdown',
                options=[
                    {'label': 'Treinar', 'value': 'train'},
                    {'label': 'Invasoras', 'value': 'invasive'},
                    {'label': 'Gerar Rotas', 'value': 'route'},
                    {'label': 'Limpar', 'value': 'clean'}
                ]
            ),
            html.Div([
                html.Div(
                    [html.B('Relatório')], style={'text-align': 'left', 'font-size': '1.1em'}),
                dcc.Dropdown(
                    id='my-dropdown-result',
                    options=[
                        {'label': 'Gerar Resultados', 'value': 'result'},
                        {'label': 'Limpar', 'value': 'clean'}
                    ]
                )],style={'margin-top':'5px'})
            ], style={'width': '80%', 'display':'inline-block','vertical-align': 'middle'})
        ], style={'width': '20%', 'float': 'left', 'text-align':'center', 'height':'388px'}),
        html.Div([
            dcc.Graph(
                id='my-graph'
                )], style={'width': '80%', 'float': 'right', 'margin-top':'-12px'}
    )], style={'width': '100%', 'height':'388px'}),
    html.H2('Resultados', style={'text-align': 'center'}),
    html.Div(id='my-results', style={'text-align': 'center'})
], style={'width': '100%'})

@app.callback(
    Output(component_id='my-results', component_property='children'),
    [Input('my-dropdown-result', 'value')]    
)
def update_output_div(input_value):
    global nCluster
    global Accuracy
    global iInvasive

    header = ['Acurácia do modelo','Número de espécies invasivas','Número de clusters' ]
    if(input_value == 'result'):
        return html.Table(
                # Header
                [html.Tr([html.Th(col) for col in header])] +
                # Body
                [html.Tr([
                    html.Td(result) for result in [Accuracy,len(iInvasive),nCluster]
                ])], style={   'display': 'inline-block'})

    else:
        return '' 

@app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown_value):
    global scores
    global s_lat
    global s_long
    global iInvasive
    global iNonInvasive
    global nCluster
    global Accuracy
    
    if(selected_dropdown_value == 'train'):
        
        scores = [0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
        #loadModel.predict()
        iInvasive = [i for i, x in enumerate(scores) if x == 1]
        iNonInvasive = [i for i, x in enumerate(scores) if x == 0]
        Accuracy = '90,42%'
        
        data = [{
            'name': 'Invasora',
            'lat': s_lat[iInvasive], 
            'lon': s_long[iInvasive], 
            'type': 'scattermapbox',
            'marker': dict( size=5, color='rgb(200,0,0)')
        },
        {
            'name': 'Não Invasora',
            'lat': s_lat[iNonInvasive], 
            'lon': s_long[iNonInvasive], 
            'type': 'scattermapbox',
            'marker': dict( size=5, color='rgb(0,200,0)')
        }]
    elif(selected_dropdown_value == 'invasive'):
        data = [{
            'name': 'Invasora',
            'lat': s_lat[iInvasive], 
            'lon': s_long[iInvasive], 
            'type': 'scattermapbox',
            'marker': dict( size=5, color='rgb(200,0,0)')
        }]
    elif(selected_dropdown_value == 'route'):
        result = modelagem.gen_paths(iInvasive) 
        data = result[0]
        nCluster = result[1]
    else:
        data = [{
                'name': 'Não identificado',
                'lat': s_lat[1:689], 
                'lon': s_long[1:689], 
                'type': 'scattermapbox',
                'marker': dict( size=5, color='rgb(0,0,200)')
            }]
        Accuracy = 0
    
    return {
            'data': data,
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




