import pandas as pd

# Carga del conjunto de datos
df_INAH_visitas = pd.read_csv('./data/raw/INAH_visitantes_museos_general.csv')
print(df_INAH_visitas.head(5))

# Total de visitas(tanto extranjeras como nacionales)

# Visitas nacionales
visitas_nacionales = df_INAH_visitas[['enero_nac', 
                                      'febrero_nac', 
                                      'marzo_nac', 
                                      'abril_nac', 
                                      'mayo_nac', 
                                      'junio_nac', 
                                      'julio_nac', 
                                      'agosto_nac', 
                                      'septiembre_nac', 
                                      'octubre_nac', 
                                      'noviembre_nac', 
                                      'diciembre_nac'
                                    ]]
suma_nacional = visitas_nacionales.sum()
total_visitas_nacional = suma_nacional.sum()

# Visitas extranjeras
visitas_extranjeras = df_INAH_visitas[['enero_ext', 
                                      'febrero_ext', 
                                      'marzo_ext', 
                                      'abril_ext', 
                                      'mayo_ext', 
                                      'junio_ext', 
                                      'julio_ext', 
                                      'agosto_ext', 
                                      'septiembre_ext', 
                                      'octubre_ext', 
                                      'noviembre_ext', 
                                      'diciembre_ext'
                                    ]]
suma_extranjera = visitas_extranjeras.sum()
total_visitas_extranjeras = suma_extranjera.sum()

total_visitas = total_visitas_nacional + total_visitas_extranjeras
print(f'Total de visitas: {total_visitas:,}')

# Promedio de visitas(tanto nacionales como extranjeras)
series_concatenado = pd.concat([suma_nacional,suma_extranjera])
visitas_n_e = pd.DataFrame(series_concatenado)

promedio_vistas = visitas_n_e.mean().iloc[0]

print(f'Promedio de visitas: {promedio_vistas:,.2f}')

# Estado con más vistas(nacionales)
estados_nacionales = [c for c in df_INAH_visitas.columns if c.endswith('_nac')]

estados_nacionales = df_INAH_visitas.groupby('estado')[estados_nacionales].sum()

print(estados_nacionales.sum(axis=1).sort_values(ascending=False).head(1))

# Estados con más visitas(extranjeras)
estados_extranjeros = [c for c in df_INAH_visitas.columns if c.endswith('_ext')]

estados_extranjeros = df_INAH_visitas.groupby('estado')[estados_extranjeros].sum()

print(estados_extranjeros.sum(axis=1).sort_values(ascending=False).head(1))