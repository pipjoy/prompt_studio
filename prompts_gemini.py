import google.generativeai as genai
import os
from dotenv import load_dotenv

# 🔐 Cargar variables de entorno desde .env
load_dotenv()

# 🔐 Cargar clave desde entorno o error explícito
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key or not api_key.startswith("AIza"):
    raise ValueError("❌ GOOGLE_API_KEY no encontrada o malformada. Revisá tu archivo .env o clave API.")

# Configurar cliente Gemini
genai.configure(api_key=api_key)

# Usar modelo Gemini 1.5 Flash (compatible y disponible)
try:
    modelo = genai.GenerativeModel("gemini-1.5-flash")
except Exception as e:
    # Fallback a gemini-1.5-pro si flash no está disponible
    try:
        modelo = genai.GenerativeModel("gemini-1.5-pro")
    except Exception as e2:
        raise RuntimeError(f"❌ Error al inicializar modelo Gemini: {e2}")

def generar_descripcion_ia(producto: dict, canal: str = "Genérico") -> str:
    prompt = f"""Generá una descripción persuasiva para un producto de e-commerce en el canal {canal}.

Producto: {producto.get("nombre")}
Marca: {producto.get("marca")}
Modelo: {producto.get("modelo") or 'N/A'}
Uso sugerido: {producto.get("uso") or 'N/A'}
Beneficio principal: {producto.get("beneficio") or 'N/A'}

Formato:
- Título del producto
- Párrafo introductorio
- Lista de beneficios
- Meta descripción SEO
"""

    try:
        respuesta = modelo.generate_content(prompt)
        return respuesta.text.strip()
    except Exception as e:
        return f"⚠️ Error al generar contenido con Gemini: {e}"
