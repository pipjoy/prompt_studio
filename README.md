# Prompt Studio

**Prompt Studio** es una aplicación web desarrollada con Streamlit que permite generar descripciones optimizadas para productos de e-commerce, utilizando inteligencia artificial de Google (Gemini / PaLM).

Incluye:
- Descripción persuasiva adaptada por canal (MercadoLibre, WooCommerce, etc.)
- Formato estructurado con HTML y SEO
- Exportación de resultados
- Notebook de experimentación con prompting

---

## 🚀 Cómo ejecutarla localmente

1. Clonar este repositorio:
```bash
git clone https://github.com/pipjoy/prompt_studio.git
cd prompt-studio
```

2. Crear un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # en Windows: venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Crear el archivo `.env`:
```
GOOGLE_API_KEY=AIza-XXXXXXXXXXXXXXXXXXXXXXXX
```

5. Ejecutar la app:
```bash
streamlit run app.py
```

---

## 🌐 Despliegue en Streamlit Cloud

1. Subí este proyecto a GitHub.
2. Entrá en [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Clic en "New app", elegí tu repo y en `Main file path` escribí: `app.py`
4. En "Advanced settings" agregá la variable de entorno:

```
GOOGLE_API_KEY=AIza-XXXXXXXXXXXXXXXXXXXXXXXX
```

5. Clic en Deploy.

---

## 📁 Estructura del proyecto

```
.
├── app.py
├── prompts_gemini.py
├── requirements.txt
├── .env.example
├── notebooks/
│   └── Notebook_Gemini_Producto.ipynb
```

---

## 🧠 Créditos

- Modelo: [Gemini (gemini-1.5-flash)](https://makersuite.google.com)
- Plataforma: [Streamlit](https://streamlit.io)
