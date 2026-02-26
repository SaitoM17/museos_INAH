import pandas as pd

# Carga del conjunto de datos
df_INAH_visitas = pd.read_csv('./data/raw/INAH_visitantes_museos_general.csv')
print(df_INAH_visitas.head(5))