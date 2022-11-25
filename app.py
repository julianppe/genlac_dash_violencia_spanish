import dash
from dash import html, dcc, Input, Output, State, html
import dash_bootstrap_components as dbc
from dash import page_registry, page_container

from dash_extensions.enrich import (
    DashProxy,
    MultiplexerTransform,
    html,
    dcc,
)

external_stylesheets = [dbc.themes.JOURNAL]

app = DashProxy(
    __name__,
    transforms=[MultiplexerTransform()],
    use_pages=True,
    prevent_initial_callbacks=True,
    suppress_callback_exceptions=True,
    external_stylesheets=external_stylesheets,
)

server = app.server

GENLAC_LOGO = "/assets/genlac.png"

dropdown = dbc.Row([
    dbc.Col(
        dbc.DropdownMenu(
        children=[
            dbc.DropdownMenuItem("Violencia doméstica", header=True),
            dbc.DropdownMenuItem("Porcentaje de mujeres que han experimentado violencia psicologica por parte de su pareja", href="/"),
            dbc.DropdownMenuItem("Porcentaje de mujeres que han experimentado violencia física doméstica", href="/violencia-fisica-domestica"),
            dbc.DropdownMenuItem("Porcentaje de mujeres que han experimentado violencia sexual doméstica", href="/violencia-sexual-domestica"),
            dbc.DropdownMenuItem("Porcentaje de mujeres que han experimentado algún tipo de violencia doméstica", href="/violencia-domestica"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Violencia no doméstica", header=True),
            dbc.DropdownMenuItem("Porcentaje de mujeres que han sufrido violencia física no domestica", href="/violencia-fisica-no-domestica"),
            dbc.DropdownMenuItem("Porcentaje de mujeres que han experimentado violencia sexual no doméstica", href="/violencia-sexual-no-domestica"),
        ],
        size="lg",
        nav=True,
        in_navbar=True,
        label="Indicadores",
        className="ms-0",
        toggle_style={"color": "#460074"},
        align_end=False,
        style={'width':'100%'}

        )
    )
],
className="g-0 ms-auto flex-nowrap mt-5 mt-md-0",
align="center",
)


navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                        dbc.Collapse(
                            dropdown, 
                            className="ml-auto",
                            id="navbar-collapse",
                            is_open=False,
                            navbar=True,
                        ),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/",
                style={"textDecoration": "none"},
            ),
        ],
    fluid=True),
    #outline=True, 
    color="light",
    dark=True,
)
# Definimos el layout:
app.layout = html.Div(
    [
        dcc.Store(id="store", data='Bolivia'),
        dbc.Container([
    dbc.Row(
        [
            navbar # Navbar
        ]
    ),
    html.Br(),        
    dbc.Row(
        [
            dash.page_container # Contenido de cada pagina
        ]
    )
], fluid=True)
    ]
)


if __name__ == "__main__":
    app.run_server()