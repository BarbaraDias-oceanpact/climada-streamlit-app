import streamlit as st
from climada.util import demo

st.title("CLIMADA no Streamlit")

st.header("Testar DAOs Demo do CLIMADA")
st.write("Carregando hazard e exposure de exemplo...")

# Carregar hazard e exposure demo do climada
hazard = demo.hazard.HazardDemo().get()
exposure = demo.exposures.ExposuresDemo().get()

if st.button("Mostrar informações dos demos"):
    st.write("Hazard (demo):")
    st.write(hazard)
    st.write("Exposure (demo):")
    st.write(exposure)
