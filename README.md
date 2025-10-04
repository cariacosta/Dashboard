# Generative AI Dashboard (MySQL)

**Autor:** Cari A.

## 📊 Descripción
Proyecto que crea una base de datos MySQL con herramientas de Inteligencia Artificial Generativa y un dashboard en Colab con gráficos creados con Plotly.

---

## 📦 Dataset
**Fuente:** [Generative AI Tools and Platforms 2025](https://www.kaggle.com/datasets/tarekmasryo/generative-ai-tools-and-platforms-2025/data.csv)

---

## ⚙️ Motor de Base de Datos
**MySQL**  
Base: `Generative_AI`  
Tabla: `generative_ai_tools`

### Creación
Ejecutar en MySQL Workbench o terminal:
```sql
SOURCE database/create_database_mysql.sql;
```

### Carga de datos
Editar el archivo `database/load_data_mysql.py` con tus credenciales y luego ejecutar:
```bash
python database/load_data_mysql.py
```

---

## 💻 Dashboard (Colab)
1. Abrir `notebooks/dashboard_generative_ai.ipynb` en Google Colab.
2. Cargar el CSV desde Kaggle o tu repositorio.
3. Ejecutar todas las celdas para generar los gráficos.

---

## 📦 Requisitos
Instalar dependencias con:
```bash
pip install -r requirements.txt
```

---
