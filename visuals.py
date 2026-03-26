import plotly.express as px
import plotly.graph_objects as go

def plot_weather_vs_yield(df):
    fig = px.scatter(
        df,
        x='Rainfall_mm',
        y='Yield_Qty',
        color='Avg_Temp',
        size='Yield_Qty',
        hover_data=['Date'],
        trendline="ols",
        title="Rainfall vs. Yield (Hover for details)",
        template="plotly_dark"
    )
    return fig

def plot_yield_timeline(df):
    fig = px.area(
        df,
        x='Date',
        y='Yield_Qty',
        title="Yield Performance Timeline",
        line_shape="spline",
        template="plotly_dark",
        color_discrete_sequence=['#00CC96']
    )
    fig.update_xaxes(rangeslider_visible=True)
    return fig

def plot_correlation_heatmap(df):
    corr = df[['Avg_Temp', 'Rainfall_mm', 'Yield_Qty']].corr()
    fig = px.imshow(
        corr,
        text_auto=True,
        aspect="auto",
        title="Factor Relationship Map",
        color_continuous_scale='RdYlGn',
        template="plotly_dark"
    )
    return fig
