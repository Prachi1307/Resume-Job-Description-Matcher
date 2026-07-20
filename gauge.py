import plotly.graph_objects as go


def match_gauge(score: float):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        number={"suffix": "%", "font": {"size": 44, "color": "#E7EDF3", "family": "Space Grotesk"}},
        gauge={
            "axis": {"range": [0, 100], "tickcolor": "#8496A8", "tickfont": {"color": "#8496A8", "size": 11}},
            "bar": {"color": "#F4A94E", "thickness": 0.28},
            "bgcolor": "rgba(0,0,0,0)",
            "borderwidth": 0,
            "steps": [
                {"range": [0, 45], "color": "#2A1B22"},
                {"range": [45, 70], "color": "#2A2418"},
                {"range": [70, 100], "color": "#1B2A28"},
            ],
        },
        domain={"x": [0, 1], "y": [0, 1]},
    ))
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        font={"color": "#E7EDF3"},
        height=260,
        margin=dict(t=30, b=10, l=30, r=30),
    )
    return fig