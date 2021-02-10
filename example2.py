
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(children = [
  html.H1("Using callbacks"),
  dcc.Dropdown(
      id="dropdown",
      options= [
          {"value": "whatever2", "label": "one"},
          {"value": "whatever", "label": "two"}
      ]),
  html.H2(id="id-changes")
])

@app.callback(
  Output(component_id="id-changes",component_property="children"),
  [Input(component_id="dropdown", component_property="value")]
)
def change_h2_on_input_change(potato):
    return "the value of the input is: " + potato

app.run_server(debug=True)
