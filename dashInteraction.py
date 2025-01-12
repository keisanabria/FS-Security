import imageListGenerator
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Create the Dash app
app = dash.Dash(__name__)
server = app.server

# List of images
images = imageListGenerator.getImages()

# Sort the keys of the images dictionary by the year extracted from the key in descending order
sorted_keys = sorted(images.keys(), key=lambda x: int(x.split(" ")[-1]), reverse=True) # Extract the year and sort numerically

# Layout
app.layout = html.Div([
    dcc.Dropdown(
        id="image-dropdown",
        options=[{"label": key, "value": key} for key in sorted_keys],
        value=sorted_keys[0]
    ),
    html.Div(id='image-display-container')
])

# Callback to update images based on the dropdown value
@app.callback(
    Output('image-display-container', 'children'),
    Input('image-dropdown', 'value'),
)
def update_images(selected_key):
    # Get the list of images based on the selected key
    image_paths = images[selected_key]
    # Return the images in a column
    return [
        html.Img(src=image_paths[0], style={"width": "80%", "height": "auto", "display": "block", "margin": "10px auto"}),
        html.Img(src=image_paths[1], style={"width": "80%", "height": "auto", "display": "block", "margin": "10px auto"}),
        html.Img(src=image_paths[2], style={"width": "80%", "height": "auto", "display": "block", "margin": "10px auto"})
    ]

# Run the app
app.run_server(host="0.0.0.0", port=8080, debug=True) # Changed to 0.0.0.0 to make it available for Render.com

# Uncomment and comment the line above to view how Dash looks  
# app.run_server(host="127.0.0.1", port=8080, debug=True)