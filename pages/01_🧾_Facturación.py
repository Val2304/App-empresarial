import streamlit as st
import pandas as pd
import os

st.title("Inicio de Sesión")

empresa = st.text_input("Ingrese el nombre de su empresa")

if empresa:
    ruta_datos = f"datos_empresas/{empresa}"
    if not os.path.exists(ruta_datos):
        os.makedirs(ruta_datos)
    st.session_state['empresa'] = empresa
    st.success(f"Sesión iniciada para la empresa: {empresa}")
st.title("🧾 Módulo de Facturación")

st.markdown("Genera facturas fácilmente y visualiza el historial de ventas.")

st.button("➕ Nueva Factura")
st.button("📂 Ver Historial")
st.button("📤 Exportar PDF")
