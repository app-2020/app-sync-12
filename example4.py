import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

df = pd.read_csv("bike-accidents.csv")

app = dash.Dash(__name__)

districts = [{"label": district, "value": district} for district in  df["DISTRITO"].unique()]
kinds_of_accidents = [{"label": kind, "value": kind} for kind in  df["TIPO ACCIDENTE"].unique()]

app.layout = html.Div(children = [
    html.H1("Bicimad accidents by district"),
    html.H3("districts"),
    dcc.Dropdown(
        id="district",
        options=districts,
        multi=True,
        value=[districts[0]["value"]]
    ),
    html.H3("Kinds of accidents"),
    dcc.Dropdown(
        id="accident-kind",
        options=kinds_of_accidents,
        multi=True,
        value=[kinds_of_accidents[0]["value"]]
    ),
    dcc.Graph(
        id="accidents-graph",
        figure={
            "data": [],
            "layout": {
                "title": "accidents"
            }
        }
    )
])

xs = list(sorted(df["HORA"].unique()))

@app.callback(
    Output(component_id="accidents-graph",component_property="figure"),
    [Input(component_id="district", component_property="value"),
     Input(component_id="accident-kind", component_property="value")]
)
def update(districts, accidents):

    data = []

    filtered = df["TIPO ACCIDENTE"].isin(accidents)
    my_df = df[filtered]

    for district in districts:
        count = my_df[my_df["DISTRITO"] == district]["HORA"].count()
        row = {'x': list(range(0, 100)), 'y': [count], 'type': 'bar', 'name': district}
        data.append(row)

    return {
        "data": data,
        "layout": {
            "title": "accidents"
        }
    }

app.run_server(debug=True)
