import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np

import plotly.express as px
from dash.dependencies import Input, Output

df = pd.read_csv('finals.csv')


app = dash.Dash(__name__)
server = app.server

fig = px.scatter_mapbox(df, lat="latitude", lon="longitude", hover_name="location", hover_data=["Severity Type"],
                        color_discrete_sequence=["red"], zoom=3, height=500)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

#all_options = {
#    'One Location': [
#        dcc.Input(id='my-id', value='initial value', type='text'),
#        html.Div(id='my-div')],
#    'Many Locations': [
#        dcc.Input(id='my-id', value='initial value', type='text'),
#        html.Div(id='my-div')]
#}

app.layout =html.Div([
        html.H1('Project:Telsra Network Disruption'),
        html.Div([
            html.P('We tried to predict a network disruption in Australia based on its location'),
            html.P('Created by: Edward S, Hans R, and Timothius H'),
            html.P('----------------------------------------------'),
            html.P('Divided into 3 categories :'),
            html.P('0 = No Fault'),
            html.P('1 = A Few Faults'),
            html.P('2 = Many Faults'),
            html.P('----------------------------------------------'),
    #----------------------------------------------------------
            html.Label('Choose your location code : '),
            #dcc.RadioItems(
            #options=[
            #    {'label': 'One Location', 'value': 'oneloc'},
            #    {'label': 'Many Locations', 'value': 'manyloc'}
            #],
        #value=''
        #),
                 
            dcc.Input(id='input-loc', value='0', type='number'),
            html.Div(id='my-div'),
            html.P('   '),
            html.P('   '),
            html.P('   '),
            html.P('   '),
            html.P('   '),
            html.P('   '),
            html.P('----------------------------------------------'),
            html.P('Base Station Map'),
    #----------------------------------------------------------
            html.Div([
    dcc.Graph(id='graph', figure=fig)
])
])
])


@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='input-loc', component_property='value')]
)
            
def update_output_div(input_value):
    nofault = df[df['location']==input_value]['No Fault'].values[0]
    afewfaults = df[df['location']==input_value]['A Few Faults'].values[0]
    manyfaults = df[df['location']==input_value]['Many Faults'].values[0]
    highest = df[df['location']==input_value]['Severity Type'].values[0]
    return """
        Probability of network disruption at location : {} || 
        No fault = {}  || 
        A Few Faults = {}  || 
        Many Faults = {}  || 
        Highest Possibilities = {}
        """.format(input_value, nofault, afewfaults, manyfaults, highest)


if __name__ == '__main__':
    app.run_server(debug=True)