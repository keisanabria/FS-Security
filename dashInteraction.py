# import dash
# from dash import dcc, html, Input, Output
import imageListGenerator
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Create the Dash app
app = dash.Dash(__name__)

# List of images
images = imageListGenerator.getImages()

# Layout
# app.layout = html.Div([
#     html.H1("Select an Image"),
#     dcc.Dropdown(
#         id="image-dropdown",
#         options=[{"label": key, "value": value} for key, value in images.items()],
#         value=list(images.values())[0]
#     ),
#     html.Img(id="image-display", style={"width": "500px", "height": "auto"})
# ])
app.layout = html.Div([
    dcc.Dropdown(
        id="image-dropdown",
        options=[
            {"label": key, "value": value} for key, value in images.items()],
        value=list(images.values())[0]
    ),
    html.Div([
        html.Img(id="image-display", 
                 src=list(images.values())[0], 
                 style={
                "width": "100%",  # Adjusts the width to fit the screen
                "height": "auto",  # Keeps the aspect ratio intact
                "display": "block",  # Centers the image
                "margin": "0 auto"  # Centers horizontally
                })  # Initial image
    ])
])

# Callback to update the image
@app.callback(
    Output("image-display", "src"),
    Input("image-dropdown", "value")
)
def update_image(selected_image):
    return selected_image

# Run the app
app.run_server(debug=True)