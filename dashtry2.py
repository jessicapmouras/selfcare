import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_table

from algo_script import get_dataframe, select_category, user_input, jw


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = get_dataframe()

app.layout = html.Div(children=[
    html.H1('Brand or App Name', style= {'color': "pink", 'backgroundColor': "grey",
    'padding': '50px', 'fontSize': '70px',
    'border': '3px solid green'}),
    html.H2('put tagline or branding here'),

    html.Ol([
        html.Li('Select your product category'),
        html.Li('Now select the profile that reflects your skin care lifestyle'),
        html.Li('Click the button to receive your recommended products'),
        
        ]),
    
    html.Label('Select Category'),
    dcc.Dropdown(id='category_drop',
        options=[
            {'label': 'Moisturizer', 'value': 'More Moisturizer'},
            {'label': 'Cleansers', 'value': 'More Cleanser'},
            {'label': 'Anti-Aging', 'value': 'More Anti-Aging'},
            {'label': 'Eye Treatments', 'value': 'More Eye Treatments'},
            {'label': 'Acne Control', 'value': 'More Blemish + Acne Control'},
            {'label': 'Toners', 'value': 'More Toners, Astringents'},
            {'label': 'Nightime', 'value': 'More Night Cream'},
            {'label': 'Sun Protection', 'value': 'More Sun Protection'}
        ],
        value=''
    ),

    html.Div(id='output1', style={'color': 'pink'}),

    html.Label('Select your profile'),
    dcc.Dropdown(id='profile_drop',
        options=[
            {'label': 'Vibrant You', 'value': 'happy, vibrant, fresh, thick, daily, clean'},
            {'label': 'Youthful Renew', 'value': 'regenerative, restore, renew, mature, age, help'},
            {'label': 'Sensitive Healing', 'value': 'sensitive, care, night, acne, heal, treat'},
            {'label': 'Natural Vibe', 'value': 'natural, treatment, daily, sensitive, gentle, organic'},
            {'label': 'Minimalist Clean', 'value': 'minimal, clean, night, simple, quick, effective'},
            {'label': 'Glam Glow', 'value': 'glow, glam, special, radiant, powerful, bright'},
            {'label': 'Fix-it Fresh', 'value': 'morning, dewy, bright, fresh, trouble, fix'},
            {'label': 'Maximum Sunshield', 'value': 'sun, freckle, work, apply, feel, defense'}
        ],
        value='',
        multi=False
    ),
    html.Button(id='submit', n_clicks=0, children='Submit'),
    html.Div(id='output2', style={'color': 'purple'}),

    # dash_table.DataTable(
    # id='table',
    # columns=[{"name": i, "id": i} for i in df.columns],
    # data=df.to_dict('rows'),
#   
])

@app.callback(Output('output2', 'children'),
              [Input('submit', 'n_clicks')],
              [State('category_drop', 'value'), State('profile_drop', 'value')])

def recommend(n_clicks, category, profile):
    print('clicks : {}, category : {}, profile : {}'.format(n_clicks, category, profile))
    print(df.shape)
    category_df = select_category(df, category)
    print(category_df.shape)
    user_input_df = user_input(category_df, profile)
    print(user_input_df.head())
    results_df = jw(user_input_df).round(2)
    print(results_df)
    columns = [{"name": i, "id": i,} for i in (results_df.columns)]
    data = results_df.to_dict('rows')
    return dash_table.DataTable(style_cell={
        'height': 'auto',
        # all three widths are needed
        'minWidth': '100px', 'width': '100px', 'maxWidth': '100px',
        'whiteSpace': 'normal'
    },data=data, columns=columns)


if __name__ == '__main__':
    app.run_server(debug=True, host= '0.0.0.0', port=8800)