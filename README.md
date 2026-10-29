# 📊 Ciencia de Datos y Álgebra Lineal Computacional (Exactas - UBA)

Repositorio con proyectos prácticos desarrollados durante la **Licenciatura en Ciencias de Datos** en la **Facultad de Ciencias Exactas y Naturales (FCEN - UBA)**. Incluye implementaciones numéricas desde cero y pipelines completos de análisis exploratorio, reducción de dimensionalidad y Machine Learning.

---

## 📂 Estructura del Repositorio

### 1. [`01-pagerank-lu/`](./01-pagerank-lu) — Algoritmo PageRank mediante Descomposición $LU$
Implementación desde cero del algoritmo **PageRank** para rankear nodos en redes dirigidas (páginas web):
- Construcción de la matriz estocástica de conectividad y planteo del sistema lineal $(I - p W D) x = e$.
- Implementación propia de **Eliminación Gaussiana con pivoteo parcial** y factorización $PA = LU$ (`escalonar_matriz`, `separar_matriz`, `desc_lu` en [`funciones.py`](./01-pagerank-lu/funciones.py)).
- Resolución mediante sistemas triangulares (`scipy.linalg.solve_triangular`) y visualización de grafos dirigidos con `NetworkX`.
- Análisis cuantitativo y cualitativo variando el factor de amortiguamiento (damping factor $p$).

### 2. [`02-pca-reconocimiento-imagenes/`](./02-pca-reconocimiento-imagenes) — PCA, SVD y Cuadrados Mínimos
- **Análisis de Componentes Principales (PCA)**: Reducción de dimensionalidad sobre conjuntos de datos de alta dimensión e imágenes, cálculo de autovalores/autovectores de la matriz de covarianza mediante el método de la potencia / deflación, y análisis de varianza explicada.
- **Cuadrados Mínimos**: Ajuste de modelos lineales y no lineales mediante descomposición QR y SVD (`minimos_cuadrados.ipynb`).

### 3. [`03-laboratorio-datos-tp1/`](./03-laboratorio-datos-tp1) — Análisis Exploratorio, Limpieza y Visualización de Datos
- Curaduría, integración de fuentes de datos, manejo de valores faltantes y detección de outliers.
- Visualizaciones estadísticas avanzadas con `Matplotlib` y `Seaborn` para responder preguntas de negocio e hipótesis sobre los datos.

### 4. [`04-futbol-europeo-ml/`](./04-futbol-europeo-ml) — Estadística y Machine Learning en Fútbol Europeo
- Análisis de métricas avanzadas de rendimiento y valuación de mercado de jugadores en las grandes ligas europeas integrando datasets de **FBRef** (`FBRef2020-21.csv`), **Transfermarkt** (`transfermarkt_fbref_201920.csv`) y **Superleague** (`superleague2023.csv`).
- Ingeniería de features, regresión, clasificación y validación cruzada con `Scikit-Learn`.

---

## 🛠️ Tecnologías Utilizadas
- **Python 3** (`NumPy`, `SciPy`, `Pandas`, `Scikit-Learn`)
- **Visualización & Grafos** (`Matplotlib`, `Seaborn`, `NetworkX`)
- **Jupyter Notebooks**
