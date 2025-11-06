import pandas as pd
import mysql.connector

# Configuración de conexión
config = {
    'user': 'root',
    'password': 'tu_contraseña',
    'host': 'localhost',
    'database': 'Generative_AI'
}

# Leer CSV
df = pd.read_csv("data/generative_ai_tools_sample.csv")

# Conexión a MySQL
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

# Insertar datos
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO generative_ai_tools (
            tool_name, company, category_canonical, modality_canonical,
            open_source, api_available, api_status, website, source_domain,
            release_year, years_since_release, mod_text, mod_image, mod_video,
            mod_audio, mod_code, mod_design, mod_infra, mod_productivity,
            mod_safety, mod_multimodal, modality_count
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, tuple(row))

conn.commit()
conn.close()
print("✅ Datos cargados correctamente en la base MySQL 'Generative_AI'")
