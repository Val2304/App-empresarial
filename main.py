
import streamlit as st
from PIL import Image

st.set_page_config(page_title="App Empresarial", layout="wide")

st.title("🚀 Aplicación Empresarial Profesional")
st.markdown("Bienvenido a tu sistema de gestión empresarial todo-en-uno.")

st.image("assets/banner.jpg", use_column_width=True)

st.markdown("""
### 📊 Módulos disponibles:
- 🧾 Facturación
- 📦 Stock y Productos
- 💰 Punto de Equilibrio
- 📈 Reportes Financieros
- 📤 Exportación a PDF

Utiliza el menú lateral para navegar por los distintos módulos.
""")
