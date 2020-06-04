import dash
# from algo_script import *
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1('Brand or App Name', style= {'color': "pink", 'backgroundColor': "grey",
     'padding': '50px', 'fontSize': '70px',
    'border': '3px solid green'}),
    html.H2('put tagline or branding here'),

    html.Ol([
        html.Li('Select your product category'),
        html.Li('Now select up to 6 tags of interest or need'),
        html.Li('Click the button to receive your recommended products'),
        
        ]),
    
    html.Label('Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'Mositurizer', 'value': 'More Mositurizer'},
            {'label': 'Cleansers', 'value': 'More Cleanser'},
            {'label': 'Anti-Aging', 'value': 'More Anti-Aging'}
        ],
        value=''
    ),

    html.Label('Multi-Select Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'Vibrant Skin', 'value': 'sensitive, cleanser, night, acne, powerful, clean'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value=[],
        multi=True
    ),



    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

   
])

# @app.callback(
#     # basic callback
#     # input HAS to be LIST
#     # output ONLY list, if it has multiple values
#     Output(component_id='output1', component_property='children'),
#     [Input(component_id='input1', component_property='value')]
# )
# def my_prediction_function(input_value):
#     return "{} was entered".format(input_value)



if __name__ == '__main__':
    app.run_server(debug=True, host= '0.0.0.0', port=8899)