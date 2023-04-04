from flask import Flask, Response, request
import plotly.graph_objs as go
import plotly.io as pio

app = Flask(__name__)

@app.route('/spider-web-graph')
def spider_web_graph():
    # Get query parameters
    categories = request.args.get('categories', '').split(',')
    values = [int(v) for v in request.args.get('values', '').split(',')]
    width = int(request.args.get('width', 500))
    height = int(request.args.get('height', 500))
    scale = int(request.args.get('scale', 2))

    # Create the chart object
    trace = go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself'
    )

    # Create the chart layout
    layout = go.Layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10]
            )
        ),
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )

    # Create the chart figure
    figure = go.Figure(data=[trace], layout=layout)

    # Save the chart as a PNG image with transparent background
    img_bytes = pio.to_image(
        figure, 
        format='png', 
        engine='kaleido', 
        scale=scale, 
        width=width, 
        height=height,
        validate=True
    )

    # Return the image as a Flask response
    return Response(img_bytes, mimetype='image/png')

if __name__ == '__main__':
    app.run()

