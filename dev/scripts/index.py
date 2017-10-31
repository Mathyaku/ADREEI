import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
from statistics import median

# mean and standard deviation
mu_lat, sigma_lat = -4.17, 3
mu_long, sigma_long = -62, 3

app = dash.Dash('Hello World')

   
app.layout = html.Div(
    [
        html.Div([
                dcc.Dropdown(
                        id='my-dropdown',
                        options=[
                {'label': 'Dados 1', 'value': 'data1'},
                {'label': 'Dados 2', 'value': 'data2'},
                {'label': 'Dados 3', 'value': 'data3'}
            ],
            value='COKE'
        )],style={'width': '25%', 'display': 'inline-block'}),
        html.Div([
            dcc.Graph(
                id='my-graph'
                )],style={'width': '100%', 'display': 'inline-block'}
        )
    ]
, style={'width': '100%'})


@app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown_value):
    print(selected_dropdown_value)
    if(selected_dropdown_value == 'data1'):
        s_lat = np.random.normal(mu_lat, sigma_lat, 222)
        s_long = np.random.normal(mu_long, sigma_long, 222)
    elif(selected_dropdown_value == 'data1'):
        s_lat = np.random.normal(mu_lat, sigma_lat, 222)
        s_long = np.random.normal(mu_long, sigma_long, 222)
    else:
        s_lat = np.random.normal(mu_lat, sigma_lat, 222)
        s_long = np.random.normal(mu_long, sigma_long, 222)
    
    print(s_lat)
    print(s_long)
    return {
            'data': [{
                'name': 'Invasora',
                'lat': s_lat[1:122], 
                'lon': s_long[1:122], 
                'type': 'scattermapbox',
                'marker': dict( size=5, color='rgb(255, 0, 0)')
            },
            {
                'name': 'Não Invasora',
                'lat': s_lat[122:], 
                'lon': s_long[122:],
                'type': 'scattermapbox',
                'marker': dict( size=5, color='rgb(0, 0, 255)')
            }],
        'layout': {
            'mapbox': {
                    'accesstoken': (
                        'pk.eyJ1IjoiY2hyaWRkeXAiLCJhIjoiY2ozcGI1MTZ3M' +
                        'DBpcTJ3cXR4b3owdDQwaCJ9.8jpMunbKjdq1anXwU5gxIw'
                    ),
                    'center': {'lat': median(s_lat), 'lon': median(s_long)},
                    'zoom': 3.5
            },
            'margin': {
                    'l': 0, 'r': 0, 'b': 0, 't': 0
            }
        }
    }

app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

if __name__ == '__main__':
    app.run_server()




