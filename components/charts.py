import pydeck as pdk
from components.utils import df_rec_estado, df_rec_mensal, df_categoria
import plotly.express as px
import streamlit as st

def create_pydeck_map(data):
    data['color'] = data['Preço'].apply(
        lambda x: [255, 140, 0] if x < 50000 else [220, 20, 60] if x < 150000 else [0, 128, 255]
    )

    scatter_layer = pdk.Layer(
        "ScatterplotLayer",
        data=data,
        get_position=["lon", "lat"],
        get_radius="Preço",
        radius_scale=0.1,
        get_fill_color="color",
        pickable=True,
    )

    view_state = pdk.ViewState(
        latitude=-14.235,
        longitude=-51.9253,
        zoom=4,
        pitch=30,
    )

    tooltip = {
        "html": "<b>Local:</b> {Local da compra}<br/><b>Preço:</b> R$ {Preço:,.2f}",
        "style": {"color": "white", "backgroundColor": "black", "fontSize": "12px"}
    }

    return pdk.Deck(
        layers=[scatter_layer],
        initial_view_state=view_state,
        tooltip=tooltip,
        map_style="mapbox://styles/mapbox/dark-v10"
    )


grafico_rec_mensal = px.line(
    df_rec_mensal,
    x = 'Mes',
    y = 'Preço',
    title='Receita Mensal',
    template='plotly_dark',
    markers=True,
    range_y= (0 , df_rec_mensal.max()),
    color= 'Ano',
    line_dash= 'Ano'
)


grafico_barra_estado = px.bar(
    df_rec_estado.head(5),
    x='Local da compra',
    y='Preço',
    title='Receita por Estado',
    template='plotly_dark',
    color='Local da compra',    
    text_auto= True,
    
)


grafico_rec_categoria = px.bar(
    df_categoria.head(7),
    title='Top 7 Categorias com maior receita',
    template='plotly_dark',
    text_auto= True,
)