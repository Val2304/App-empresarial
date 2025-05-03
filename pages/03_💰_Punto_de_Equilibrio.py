import streamlit as st

st.title("💰 Análisis de Punto de Equilibrio")

st.markdown("Calcula el punto en el que los ingresos cubren los costos.")

st.number_input("Costos Fijos", min_value=0.0)
st.number_input("Precio de Venta Unitario", min_value=0.01)
st.number_input("Costo Variable Unitario", min_value=0.01)

st.button("📊 Calcular Punto de Equilibrio")