# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 10:51:10 2017

@author: Raissa
"""

from plotly.offline import iplot
import plotly.plotly as py
import pandas as pd
import numpy as np
import random
#df_airports = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_february_us_airport_traffic.csv')
#df_airports.head()
#
#df_flight_paths = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_february_aa_flight_paths.csv')
#df_flight_paths.head()
mu_lat, sigma_lat = -4.17, 3
mu_long, sigma_long = -62, 4 # mean and standard deviation
s_lat = [np.random.normal(mu_lat, sigma_lat, 222), np.random.normal(mu_long, sigma_long, 222)]
s_long = np.random.normal(mu_long, sigma_long, 222)

#for i in range(0, 221):
##    df_airports['lat'][i] = random.uniform(-1, -6)
##    df_airports['long'][i] = random.uniform(-55, -64)
#    df_airports['lat'][i] = s_lat[i]
#    df_airports['long'][i] = s_long[i]

airports = [ dict(
        type = 'scattergeo',
        locationmode = 'ISO-3',
        lon = s_long,
        lat = s_lat,
        hoverinfo = 'text',
        text = str(s_long) + "_" + str(s_lat),
        mode = 'markers',
        marker = dict( 
            size=3, 
            color='rgb(255, 0, 0)',
            line = dict(
                width=3,
                color='rgba(68, 68, 68, 0)'
            )
        ))]
        
flight_paths = []
for i in range( len( df_flight_paths ) ):
    flight_paths.append(
        dict(
            type = 'scattergeo',
            locationmode = 'ISO-3',
            lon = [ df_flight_paths['start_lon'][i], df_flight_paths['end_lon'][i] ],
            lat = [ df_flight_paths['start_lat'][i], df_flight_paths['end_lat'][i] ],
            mode = 'lines',
            line = dict(
                width = 1,
                color = 'red',
            ),
            opacity = float(df_flight_paths['cnt'][i])/float(df_flight_paths['cnt'].max()),
        )
    )
    
layout = dict(
        title = 'Feb. 2011 American Airline flight paths<br>(Hover for airport names)',
        showlegend = False, 
        geo = dict(
            projection=dict( type='azimuthal equal area' ),
            showland = True,
            landcolor = 'rgb(243, 243, 243)',
            countrycolor = 'rgb(204, 204, 204)',
        ),
    )
    
fig = dict( data= airports, layout=layout )
import plotly
plotly.tools.set_credentials_file(username='raissb', api_key='n6WrafYM07brhRy8dEYW')
py.iplot( fig, filename='d3-flight-brazil_1')

index = [random.randint(0,221) for x in range(1,round(0.3*221))]
airports = [ dict(
        type = 'scattergeo',
        locationmode = 'ISO-3',
        lon = s_long[index],
        lat = s_lat[index],
        hoverinfo = 'text',
        text = str(s_long) + "_" + str(s_lat),
        mode = 'markers',
        marker = dict( 
            size=3, 
            color='rgb(255, 0, 0)',
            line = dict(
                width=3,
                color='rgba(68, 68, 68, 0)'
            )
        ))]
        
    
fig = dict( data= airports, layout=layout )
fig = dict( data=drone_paths , layout=layout )
py.iplot( fig, filename='d3-path-brazil_1')