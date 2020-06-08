import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_table

from algo_script2 import get_dataframe, select_category, user_input, jw



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css',
'https://cdnjs.cloudflare.com/ajax/libs/meyer-reset/2.0/reset.min.css',
'https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css',
'https://codepen.io/jessicapmouras/pen/yLeNPzY.css',]

app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets
    )

df = get_dataframe()

app.layout = html.Div(className='col-md-8 offset-2',children=[
    html.Div(className='jumbotron tropic-goth shadow',
        children=[html.H1('SkinFit'
    ),
    html.H2('Fitting Skincare to your Lifestyle'),

    html.Ol([
        html.Li('Discover new products...'),
        html.Li('With research done for you...'),
        html.Li('So you can be on the go.'),
        
        ]),
        ]),
    
    
    html.Label('Select Product Category'),
    dcc.Dropdown(
        id='category_drop',
        className='shadow',
        options=[
            {'label': 'Moisturizer', 'value': 'More Moisturizer'},
            {'label': 'Cleansers', 'value': 'More Cleanser'},
            {'label': 'Anti-Aging', 'value': 'More Anti-Aging'},
            {'label': 'Eye Treatments', 'value': 'More Eye Treatments'},
            {'label': 'Acne Control', 'value': 'More Blemish + Acne Control'},
            {'label': 'Toners', 'value': 'More Toners, Astringents'},
            {'label': 'Night-time', 'value': 'More Night Cream'},
            {'label': 'Sun Protection', 'value': 'More Sun Protection'}
        ],
        value=''
    ),

    html.Div(id='output1', style={'color': 'pink'}),

    html.Label('Select Your Profile'),
    dcc.Dropdown(
        id='profile_drop',
        className='shadow',
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
    html.Div(className='row row-spacer',
        children=[
            html.Button(
                id='submit', className='btn btn-dark', n_clicks=0, children='Submit'
                )
                ]),
    # html.Button(id='submit', className='btn btn-primary', n_clicks=0, children='Submit'),
    html.Div(
        id='output2', style={'color': 'purple'}),

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
    return html.Div(
        dash_table.DataTable
            (style_cell={
            'height': 'auto',
            # all three widths are needed
            'minWidth': '100px', 'width': '100px', 'maxWidth': '100px',
            'whiteSpace': 'normal',
            'textAlign': 'left',
            'fontFamily': 'sans-serif',
            'padding': '2px;'
            },data=data, columns=columns)
    ,className='table shadow')


if __name__ == '__main__':
    app.run_server(debug=True, host= '0.0.0.0', port=8803)