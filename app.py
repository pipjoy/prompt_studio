import streamlit as st
from prompts_gemini import generar_descripcion_ia

st.set_page_config(page_title="Prompt Studio", layout="centered")
st.title("Prompt Studio")
st.markdown("Generador de descripciones optimizadas para productos de e-commerce usando IA.")

st.header("📦 Datos del Producto")
nombre = st.text_input("Nombre del producto")
marca = st.text_input("Marca")
modelo = st.text_input("Modelo (opcional)")
uso = st.text_area("Uso sugerido (opcional)")
beneficio = st.text_area("Beneficio principal (opcional)")
canal = st.selectbox("Canal de publicación", ["Genérico", "WooCommerce", "MercadoLibre", "Tiendanube"])

if st.button("Generar Descripción con IA"):
    if not nombre or not marca:
        st.warning("Por favor completá al menos el nombre y la marca.")
    else:
        producto = {
            "nombre": nombre,
            "marca": marca,
            "modelo": modelo,
            "uso": uso,
            "beneficio": beneficio
        }
        with st.spinner("Generando contenido..."):
            resultado = generar_descripcion_ia(producto, canal)
            st.success("Descripción generada:")
            st.text_area("Resultado", resultado, height=300)
