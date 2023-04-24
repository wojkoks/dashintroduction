from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px
#pip install dash
#pip install dash-core-components

d = pd.read_csv("mydata.csv")

analysis = d.groupby("category")

df = px.data.iris()

f = px.scatter(df,x="sepal_width",y="sepal_length")

app =  Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1("Sekcja AI = wprowadzenie do dash",style={"color":"yellow"}),
        dcc.Dropdown(id="input",
            options=[
                {"label": "Category A", "value": "A"},
                {"label": "Category B", "value": "B"},
                {"label": "Category C", "value": "C"}
            ],
            value="cokolwiek",
        ),
        dcc.Graph(figure=f),
        html.Div(id="output", children="") 
    ]
)
@app.callback(
    Output('output','children'),
[Input('input','value')]
)
def update_layout(value):
    ## filtrujemy dane
    if d["category"]==value:
        return value
        # return html.Div(f"{df}")


if __name__ == '__main__':
    app.run_server(debug="True")
