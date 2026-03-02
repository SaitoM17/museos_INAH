import pandas as pd

# Carga del conjunto de datos
df_INAH_visitas = pd.read_csv('./data/raw/INAH_visitantes_museos_general.csv')
print(df_INAH_visitas.head(5))

# Total de visitas(tanto extranjeras como nacionales)

# Visitas nacionales
estados_nacionales = [c for c in df_INAH_visitas.columns if c.endswith('_nac')]
total_visitas_nacional = df_INAH_visitas[estados_nacionales].sum().sum()

# Visitas extranjeras
estados_extranjeros = [c for c in df_INAH_visitas.columns if c.endswith('_ext')]
total_visitas_extranjeras = df_INAH_visitas[estados_extranjeros].sum().sum()

total_visitas = total_visitas_nacional + total_visitas_extranjeras
print(f'Total de visitas: {total_visitas:,}')

# Promedio de visitas(tanto nacionales como extranjeras)
series_concatenado = pd.concat([suma_nacional,suma_extranjera])
visitas_n_e = pd.DataFrame(series_concatenado)

promedio_vistas = visitas_n_e.mean().iloc[0]

print(f'Promedio de visitas: {promedio_vistas:,.2f}')

# Estado con más vistas(nacionales)
estados_nacionales = df_INAH_visitas.groupby('estado')[estados_nacionales].sum()

visitas_por_estado_nacional = estados_nacionales.sum(axis=1)
estado_top_nac = visitas_por_estado_nacional.idxmax()
valor_top_nac = visitas_por_estado_nacional.max()

print(f'Estado con más visitas Nacionales: {estado_top_nac} con {valor_top_nac:,} visitas')

# Estados con más visitas(extranjeras)
estados_extranjeros = df_INAH_visitas.groupby('estado')[estados_extranjeros].sum()

visitas_por_estado_extranjeras = estados_extranjeros.sum(axis=1)
estado_top_ext = visitas_por_estado_extranjeras.idxmax()
valor_top_ext = visitas_por_estado_extranjeras.max()

print(f'Estado con más visitas Extranjeras: {estado_top_ext} con {valor_top_ext:,} visitas')