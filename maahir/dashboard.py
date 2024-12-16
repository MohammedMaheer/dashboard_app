import dash
from dash import dcc, html, Input, Output, dash_table
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "Centralized Business Execution Dashboard"

# Dummy Data
projects_data = {
    "id": [1, 2, 3, 4],
    "project_name": ["Project A", "Project B", "Project C", "Project D"],
    "status": ["In Progress", "Completed", "On Hold", "In Progress"],
    "start_date": ["2024-01-01", "2023-05-01", "2024-03-15", "2024-07-01"],
    "end_date": ["2024-12-31", "2023-11-30", "2024-09-30", "2025-06-30"],
}
resources_data = {
    "id": [1, 2, 3, 4],
    "resource_name": ["John Doe", "Jane Smith", "Alan Turing", "Grace Hopper"],
    "allocated_project": ["Project A", "Project B", "Project C", "None"],
    "availability": [50, 0, 75, 100],
}
compliance_data = {
    "id": [1, 2, 3],
    "report_name": ["Data Security", "Financial Audits", "Regulatory Updates"],
    "compliance_status": ["Compliant", "Pending", "Non-Compliant"],
    "date": ["2024-12-01", "2024-12-15", "2024-11-30"],
}

# Convert to DataFrames
projects = pd.DataFrame(projects_data)
resources = pd.DataFrame(resources_data)
compliance = pd.DataFrame(compliance_data)

# App Layout
app.layout = html.Div([
    html.Div([
        html.H1("Business Execution Dashboard", style={
            'text-align': 'center', 
            'color': '#34495E', 
            'font-weight': 'bold', 
            'font-size': '36px'
        }),
        html.P("Streamlining operations for efficiency and compliance", style={
            'text-align': 'center', 
            'font-size': '18px', 
            'color': '#7F8C8D', 
            'margin-bottom': '30px'
        }),
    ], style={'background-color': '#ECF0F1', 'padding': '20px', 'border-bottom': '5px solid #34495E'}),

    dcc.Tabs([
        # Tab 1: Project Tracking
        dcc.Tab(label='Project Tracking', style={'font-size': '18px'}, children=[
            html.Div([
                dcc.Graph(id='project-status-chart'),
                html.Hr(),
                html.H3("Project Details", style={'text-align': 'left', 'margin-top': '20px'}),
                dash_table.DataTable(
                    data=projects.to_dict('records'),
                    columns=[{"name": i.replace("_", " ").capitalize(), "id": i} for i in projects.columns],
                    style_table={'overflowX': 'auto', 'border': '1px solid #ccc'},
                    style_header={'backgroundColor': '#34495E', 'color': 'white', 'fontWeight': 'bold'},
                    style_data={'border': '1px solid #ddd', 'backgroundColor': '#F9F9F9'}
                )
            ], style={'padding': '20px'}),
        ]),

        # Tab 2: Resource Allocation
        dcc.Tab(label='Resource Allocation', style={'font-size': '18px'}, children=[
            html.Div([
                dcc.Graph(id='resource-allocation-chart'),
                html.Hr(),
                html.H3("Resource Details", style={'text-align': 'left', 'margin-top': '20px'}),
                dash_table.DataTable(
                    data=resources.to_dict('records'),
                    columns=[{"name": i.replace("_", " ").capitalize(), "id": i} for i in resources.columns],
                    style_table={'overflowX': 'auto', 'border': '1px solid #ccc'},
                    style_header={'backgroundColor': '#34495E', 'color': 'white', 'fontWeight': 'bold'},
                    style_data={'border': '1px solid #ddd', 'backgroundColor': '#F9F9F9'}
                )
            ], style={'padding': '20px'}),
        ]),

        # Tab 3: Compliance Reporting
        dcc.Tab(label='Compliance Reporting', style={'font-size': '18px'}, children=[
            html.Div([
                dcc.Graph(id='compliance-status-chart'),
                html.Hr(),
                html.H3("Compliance Details", style={'text-align': 'left', 'margin-top': '20px'}),
                dash_table.DataTable(
                    data=compliance.to_dict('records'),
                    columns=[{"name": i.replace("_", " ").capitalize(), "id": i} for i in compliance.columns],
                    style_table={'overflowX': 'auto', 'border': '1px solid #ccc'},
                    style_header={'backgroundColor': '#34495E', 'color': 'white', 'fontWeight': 'bold'},
                    style_data={'border': '1px solid #ddd', 'backgroundColor': '#F9F9F9'}
                )
            ], style={'padding': '20px'}),
        ]),
    ], style={'font-family': 'Arial', 'font-size': '16px'}),
])

# Callbacks for Interactive Charts
@app.callback(
    Output('project-status-chart', 'figure'),
    Input('project-status-chart', 'id')  # Placeholder input
)
def update_project_status_chart(_):
    fig = px.timeline(
        projects, 
        x_start='start_date', 
        x_end='end_date', 
        y='project_name', 
        color='status', 
        title="Project Status Timeline",
        template="plotly_dark"
    )
    fig.update_traces(marker_line_width=1.5, marker_line_color="#2C3E50")
    fig.update_layout(
        paper_bgcolor='#ECF0F1', 
        plot_bgcolor='#ECF0F1', 
        font=dict(color='#34495E'),
        title_font=dict(size=20, color="#2C3E50")
    )
    return fig

@app.callback(
    Output('resource-allocation-chart', 'figure'),
    Input('resource-allocation-chart', 'id')
)
def update_resource_allocation_chart(_):
    fig = px.pie(
        resources, 
        names='resource_name', 
        values='availability', 
        title="Resource Allocation",
        hole=0.4,
        template="seaborn"
    )
    fig.update_traces(textinfo='percent+label', pull=[0.05, 0, 0, 0])
    fig.update_layout(
        showlegend=True, 
        legend_title="Resource Names",
        paper_bgcolor='#ECF0F1',
        title_font=dict(color="#34495E")
    )
    return fig

@app.callback(
    Output('compliance-status-chart', 'figure'),
    Input('compliance-status-chart', 'id')
)
def update_compliance_status_chart(_):
    fig = px.bar(
        compliance, 
        x='report_name', 
        y='compliance_status', 
        title="Compliance Status", 
        color='compliance_status',
        template="ggplot2"
    )
    fig.update_traces(marker_line_width=1.5, marker_line_color="#34495E")
    fig.update_layout(
        paper_bgcolor='#ECF0F1', 
        plot_bgcolor='#ECF0F1', 
        font=dict(color='#34495E'),
        title_font=dict(size=20, color="#34495E")
    )
    return fig

# Run app
if __name__ == '__main__':
    app.run_server(debug=True)
