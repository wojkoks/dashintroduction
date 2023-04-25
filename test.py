from dash import Dash, dcc, html,dash_table
from dash.dependencies import Input, Output
from dash.development.base_component import Component
import pandas as pd
import plotly.express as px
#pip install dash
#pip install dash-core-components

#csv data
df = pd.read_csv("mydata.csv")

#graph data
iris_df = px.data.iris()
f = px.scatter(iris_df,x="sepal_width",y="sepal_length",height=350,width=700)

#initialize empty app
app =  Dash(__name__)

#create a layout
app.layout = html.Div(
    children=[
        html.Div(children=[
            html.Title("Dash Introduction"),
            html.Link(
                rel="stylesheet",
                href="style.css"
            ),
            html.Div(children=[
                html.H1("Introduction to dash - Wojciech Kuś",id="mainHeader"),
                ],
                style={"height":"150px"}),
            dcc.Dropdown(id="input",
                options=[
                    {"label": "Category A", "value": "A"},
                    {"label": "Category B", "value": "B"},
                    {"label": "Category C", "value": "C"}
                ],
                value=None, style={"color":"black","width":"300px"}),
            html.Div(children=[
                html.Div(children=[
                    dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns])],
                    style={"color":"black","width":"300px"},id="output2"
                ),
                html.Div(id="output", children=["jello"],style={"width":"700px"}),
                ],style={"display":"flex","flex-direction":"row"}),
            html.Div(id="graph",children=[
                dcc.Graph(figure=f),
                html.Br(),
                "Iris graph example (dubleclick to zoom out)",
                ],style={"display":"flex","flex-direction":"column"})
                ],className="mainPage")
        ],
        className="test-1")


@app.callback(
    Output(component_id='output',component_property='children'),
    [Input(component_id='input',component_property='value')])
def update_layout(value):

    if value != "" and value !=None:
        filtered_df = df[df["category"]==value] ## Filtering data
        filtered_df = filtered_df.groupby("category").mean()
    else:
        filtered_df = df                        ## Category is All so we dont need to filter data

  
    a = round(filtered_df['value1'][0],2)       ## Extracting mean value
    b = round(filtered_df['value2'][0],2)

    # print(type(filtered_df))                  panda DataFrame
    # print(type(filtered_df['value1']))        panda Series
    # print(type(filtered_df['value1'][0]))     float64 
    # that's why the syntax
    result = ("Between every category",f"For category {value} its mean for")[value!=None]
    return html.P(f"{result} its value1 mean evaluates to: {a} and its value2 meanevaluates to:{b}",style={"padding":"40px","background-color":"#0512265e"})


@app.callback(
    Output(component_id='output2',component_property='children'),
    [Input(component_id='input',component_property='value')])
def update_table(category):                     #argument can be named whatever   
    if category == '' or category == None:      
        return dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns])
    
    filtered_df = df[df["category"]==category]
    return dash_table.DataTable(filtered_df.to_dict('records'), [{"name": i, "id": i} for i in filtered_df.columns])

if __name__ == '__main__':
    app.run_server(debug="True")
