import plotly.express as px
from utils import df_rec_estado, df_rec_mensal, df_categoria

grafico_map_estado = px.scatter_geo(
    df_rec_estado,
    lat='lat',
    lon='lon',
    scope='south america',
    size='Preço',
    template='plotly_dark',  
    color='Preço',  
    color_continuous_scale=px.colors.sequential.Plasma,  
    hover_name='Local da compra',
    hover_data={'lat': False, 'lon': False, 'Preço': True},
    title='Receita por Estado',
)

grafico_map_estado.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))  
grafico_map_estado.update_layout(
    autosize=True,        
    title_font_size=20,
    geo=dict(
        landcolor="LightGray",
        lakecolor="LightBlue",
        projection_type="mercator"
    )
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