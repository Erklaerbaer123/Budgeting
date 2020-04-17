
import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.graph_objs as go

labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
values = [4500, 2500, 1053, 500]

app = dash.Dash()
app.layout = html.Div(children=[
    dcc.Graph(
        figure=go.Figure(
            data=[
                go.Pie(labels=labels, values=values)
            ],
            layout=go.Layout(
                title='US Export of Plastic Scrap',
            )
        ),
        style={'height': 300},
        id='my-graph'
    )  
])

if __name__ == '__main__':
    app.run_server(debug=True)