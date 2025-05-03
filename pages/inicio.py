import streamlit as st
import os

st.title("Inicio de Sesión")

empresa = st.text_input("Ingrese el nombre de su empresa")

if empresa:
    ruta_datos = f"datos_empresas/{empresa}"
    if not os.path.exists(ruta_datos):
        os.makedirs(ruta_datos)
    st.session_state['empresa'] = empresa
    st.success(f"Sesión iniciada para la empresa: {empresa}")
