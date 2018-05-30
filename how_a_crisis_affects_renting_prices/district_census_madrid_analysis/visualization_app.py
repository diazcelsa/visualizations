import pickle

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output

file = open("./data/df_census_visualizations.pkl", 'rb')
sd = pickle.load(file)


def shit_for_levin(data, column, name, group, color):
    # Create and style traces
    trace = go.Scatter(
        x=data.index.tolist(),
        y=data[column].tolist(),
        legendgroup=group,
        name=name,
        line=dict(
            color=(color),
            width=4, )
    )
    return trace


age_range = {'Age range 0-24': 0,
             'Age range 25-39': 1,
             'Age range 40-64': 2,
             'Age range 65-84': 3,
             'Age range 85-100': 4}

app = dash.Dash('drop_down_line_suplot')

app.layout = html.Div([
    dcc.Tabs(
        tabs=[
            {'label': k, 'value': v} for k, v in age_range.items()
        ],
        value=0,
        id='tabs'
    ),
    dcc.Graph(id='my-graph')
], style={
    'width': '80%',
    'fontFamily': 'Sans-Serif',
    'margin-left': 'auto',
    'margin-right': 'auto'
})


@app.callback(Output('my-graph', 'figure'), [Input('tabs', 'value')])
def update_graph(age_range):
    trace0 = shit_for_levin(sd[age_range], 'worker class', 'Worker Class', 'group', 'rgb(22, 96, 167)')
    trace1 = shit_for_levin(sd[age_range], 'middle class', 'middle Class', 'group', 'rgb(169,169,169)')
    trace2 = shit_for_levin(sd[age_range], 'upper class', 'upper Class', 'group', 'rgb(205, 12, 24)')

    data = [trace0, trace1, trace2]
    return {
        'data': data,
        'layout': {'margin': {'l': 40, 'r': 0, 't': 20, 'b': 30},
                   'legend': {'x': 0, 'y': 1}}
    }


app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

if __name__ == '__main__':
    app.run_server()
