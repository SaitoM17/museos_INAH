# 📊 Museos INAH
# Análisis de las visitas a los museos INAH

El Instituto Nacional de Antropología e Historia (INAH) gestiona un vasto patrimonio cultural que requiere una administración basada en datos. Este proyecto busca transformar los registros históricos de visitas en información estratégica para la toma de decisiones.

---

## 📚 Tabla de Contenidos

- [🎯 Propósito](#-propósito)
- [📦 Conjunto de Datos](#-conjunto-de-datos)
- [🧪 Desarrollo del Proyecto](#-desarrollo-del-proyecto)
- [📈 Conclusiones y Recomendaciones](#-conclusiones-y-recomendaciones)
- [🛠️ Tecnologías](#️-tecnologías)
- [⚙️ Instalación](#️-instalación)
- [👤 Autor](#-autor)

---

## 🎯 Propósito

 Visualizar la evolución histórica de las visitas nacionales y extranjeras en los distintos estados de la República Mexicana y desarrollar un modelo predictivo para la afluencia esperada durante el 2026.

---

## 📦 Conjunto de Datos

El conjunto de datos utilizado contiene las siguientes columnas:

- `anio`: Año en que se registro la visita
- `estado`: Nombre del estado
- `ckave_siinah`: Clave númerica de registro
- `recinto`: Nombre del museo
- `enero_nac`: Visitas nacionales
- `enero_ext`: Visitas extranjeras
- `febrero_nac`: Visitas nacionales
- `febrero_ext`:Visitas extranjeras
- `marzo_nac`: Visitas nacionales
- `marzo_ext`:Visitas extranjeras
- `abril_nac`: Visitas nacionales
- `abril_ext`:Visitas extranjeras
- `mayo_nac`: Visitas nacionales
- `mayo_ext`: Visitas extranjeras
- `junio_nac`: Visitas nacionales
- `julio_ext`: Visitas extranjeras
- `agosto_nac`: Visitas nacionales
- `agosto_ext`:Visitas extranjeras
- `septiembre_nac`: Visitas nacionales
- `septiembre_ext`: Visitas extranjeras
- `octubre_nac`: Visitas nacionales
- `octubre_ext`: Visitas extranjeras
- `noviembre_nac`: Visitas nacionales
- `noviembre_ext`: Visitas extranjeras
- `diciembre_nac`: Visitas nacionales
- `diciembre_ext`: Visitas extranjeras

Fuente: [Visitantes a museos abiertos al público](https://www.datos.gob.mx/dataset/visitantes_museos_abiertos_publico).

---

## 🧪 Desarrollo del Proyecto

1. **Carga y exploración inicial de los datos**:
   - Exploración básica con `.head()`, `.info()`, `.describe()`, etc.

2. **Limpieza y preprocesamiento**:
   - Manejo de valores nulos, duplicados, formatos y conversiones de fechas.

3. **Análisis exploratorio de datos (EDA)**:
   - [Ej. Distribución, correlaciones, agrupaciones, etc.]

4. **Visualización de datos**:
   - Uso de gráficos de barras, líneas, cajas, dispersión y mapas de calor.

5. **Modelado o reportes (opcional)**:
   - [Si aplica: modelos de ML, clustering, predicciones, etc.]

6. **Conclusiones y recomendaciones**:
   - Síntesis de hallazgos clave y propuestas de acción.

---

## 📈 Conclusiones y Recomendaciones

- [Insight 1]
- [Insight 2]
- [Recomendación práctica o estratégica basada en los datos]

---

## 🛠️ Tecnologías

- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook / Google Colab
- [Otras herramientas que uses, como Scikit-learn, Plotly, etc.]

---

## ⚙️ Instalación

### 1. Clonar este repositorio:
```bash
git clone https://github.com/tu_usuario/nombre_del_proyecto.git
```
### 2. Uso de un Entorno Virtual para Aislar Dependencias

Para evitar conflictos con versiones de librerías, se recomienda usar entornos virtuales.

####  Crear y Activar un Entorno Virtual

##### Crear el entorno virtual:
```
python -m venv venv
```
##### Activar el entorno:
* #### En Windows:

    ```
    venv\Scripts\activate
    ```

* #### En Mac/Linux::

    ```
    source venv/bin/activate
    ```
#### 3. Instalar dependencias dentro del entorno:
* #### Opición 1:
    ```
    pip install -r requirements.txt
    ```

* #### Opción 2 (De forma manual):
    ```
    pip install numpy pandas matplotlib seaborn scikit-learn
    ```

---

## 👤 Autor

**Said Mariano Sánchez** – *smariano170@gmail.com*  
Este proyecto forma parte de mi portafolio como analista de datos Jr.

---

## 📝 Licencia

Este proyecto está licenciado bajo la **Licencia MIT**. Puedes usarlo, modificarlo y distribuirlo libremente, siempre que menciones al autor original.

---