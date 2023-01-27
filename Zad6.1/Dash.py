import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px

app = dash.Dash()
df = pd.read_csv("winequelity.csv")
df = df.drop(columns=['Unnamed: 0'])


@app.callback(Output('chart-regression', 'figure'),
              Input(component_id='dropdown', component_property='value'),
              Input(component_id='feature_name', component_property='value'),
              )
def update_figure(prediction_type, feature_name):
    if prediction_type == "Regresja":
        fig = px.scatter(x=df[feature_name],
                         y=df["pH"],)
        fig.update_yaxes(title="pH",)
        fig.update_xaxes(title=feature_name, )

    elif prediction_type == "Klasyfikacja":
        fig = px.histogram(y=df[feature_name],
                     x=df["target"],)
        fig.update_xaxes(title="target",)
        fig.update_yaxes(title=feature_name, )

    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')
    return fig


style = {'textAlign': 'center', 'marginTop': 40, 'marginBottom': 40}
app.layout = html.Div(id='parent', children=[
    html.H1(id='H1', children='Zad6 – Dash', style=style),

    html.H2(id='H2-table', children='Dane', style=style),
    dbc.Table.from_dataframe(df.head(10), striped=True, bordered=True, hover=True, id='table', style=style),
    html.H2(id='H2-prediction', children='Rodzaj predykcji', style=style),
    dcc.Dropdown(['Klasyfikacja', 'Regresja'], "Klasyfikacja", id='dropdown', style=style),
    html.H2(id='H2-feature', children='Zmienna', style=style),
    dcc.Dropdown(
                df.columns.tolist(),
                'fixed acidity',
                id='feature_name',
                style=style
            ),
    dcc.Graph(id='chart-regression', style=style),

])

if __name__ == '__main__':
    app.run_server(debug=True)