# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/jjpal/kx-project/main/forecasting.csv')

# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.Div(children='Time Series App'),
    html.Hr(),
    dcc.RadioItems(options=['MAE', 'RMSE'], value='MAE', id='radio-item-example'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=6),
    dcc.Graph(figure={}, id='graph-example')
])


# Add controls to build the interaction
@callback(
    Output(component_id='graph-example', component_property='figure'),
    Input(component_id='radio-item-example', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='Model', y=col_chosen, histfunc='avg')
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)