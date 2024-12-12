from dataset import df
import pandas as pd

def format_number(value, prefix=''):
    for unit in ['', ' mil', ' milhões']:
        if value < 1000:
            return f'{prefix}{value:.2f}{unit}'
        value /= 1000
    return f'{prefix}{value:.2f} bilhões'  


#======================================================
# Receita Estado
#======================================================


df_rec_estado = df.groupby('Local da compra')[['Preço']].sum()
df_rec_estado['Preço Formatado'] = df_rec_estado['Preço'].apply(format_number, prefix='R$')
df_rec_estado = (
    df.drop_duplicates(subset='Local da compra')[['Local da compra', 'lat', 'lon']]
    .merge(df_rec_estado, left_on='Local da compra', right_index=True)
    .sort_values('Preço', ascending=False) 
)

#======================================================
# Receita Mês + Dias
#======================================================
df['Data da Compra'] = pd.to_datetime(df['Data da Compra'])

df_rec_mensal = (
    df.set_index('Data da Compra')
      .groupby(pd.Grouper(freq='M'))['Preço']
      .sum()
      .reset_index()
)
print(df_rec_mensal)
# Extraindo ano e mês
df_rec_mensal['Ano'] = df_rec_mensal['Data da Compra'].dt.year
df_rec_mensal['Mes'] = df_rec_mensal['Data da Compra'].dt.month_name()

# Por Dia
df_rec_diario = (
    df.set_index('Data da Compra').groupby(pd.Grouper(freq='D'))['Preço'].sum().reset_index()
)
df_rec_diario['Dia'] = df_rec_diario['Data da Compra'].dt.day


#======================================================
# Receita Categorias
#======================================================


df_categoria = df.groupby('Categoria do Produto')[['Preço']].sum().sort_values('Preço', ascending=False)