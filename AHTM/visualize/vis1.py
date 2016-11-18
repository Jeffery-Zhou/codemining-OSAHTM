import plotly
from plotly.graph_objs import Scatter, Layout

# plotly.offline.plot({
#     "data": [Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
#     "layout": Layout(title="hello world")
# })

plotly.offline.plot([{
    'z': [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ],
    'type': 'heatmap',
    'colorscale': [
        # Let first 10% (0.1) of the values have color rgb(0, 0, 0)
        [0, 'rgb(0, 0, 0)'],
        [0.1, 'rgb(0, 0, 0)'],

        # Let values between 10-20% of the min and max of z
        # have color rgb(20, 20, 20)
        [0.1, 'rgb(20, 20, 20)'],
        [0.2, 'rgb(20, 20, 20)'],

        # Values between 20-30% of the min and max of z
        # have color rgb(40, 40, 40)
        [0.2, 'rgb(40, 40, 40)'],
        [0.3, 'rgb(40, 40, 40)'],

        [0.3, 'rgb(60, 60, 60)'],
        [0.4, 'rgb(60, 60, 60)'],

        [0.4, 'rgb(80, 80, 80)'],
        [0.5, 'rgb(80, 80, 80)'],

        [0.5, 'rgb(100, 100, 100)'],
        [0.6, 'rgb(100, 100, 100)'],

        [0.6, 'rgb(120, 120, 120)'],
        [0.7, 'rgb(120, 120, 120)'],

        [0.7, 'rgb(140, 140, 140)'],
        [0.8, 'rgb(140, 140, 140)'],

        [0.8, 'rgb(160, 160, 160)'],
        [0.9, 'rgb(160, 160, 160)'],

        [0.9, 'rgb(180, 180, 180)'],
        [1.0, 'rgb(180, 180, 180)']
    ],
    'colorbar': {
        'tick0': 0,
        'dtick': 1
    }
}])