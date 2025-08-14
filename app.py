import streamlit as st
import joblib
import numpy as np

# Cargar modelo entrenado
modelo = joblib.load('primermillon.joblib')

# Título y autor
st.title("🎓 Predictor de Éxito Académico")
st.markdown("**Autor: Jose Vicente**")

# Imagen debajo del autor (usamos una imagen de internet)
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_sjlLXiqST6zFVK4uDi5E136R4RXq_wNw7A&s",use_container_width=True, 
         caption="El camino al éxito académico")

# Introducción
st.markdown("""
Bienvenido a la aplicación de predicción de éxito académico.  
Introduce tus datos a continuación para saber si es probable que te gradúes con éxito.

Los valores deben estar entre 0.0 y 1.0 (con un decimal de precisión).
""")

# Sliders para variables de entrada
nota_ia = st.slider("Nota IA", 0.0, 1.0, step=0.1)
gpa = st.slider("GPA", 0.0, 1.0, step=0.1)

# Botón para predecir
if st.button("📊 Predecir"):
    entrada = np.array([[nota_ia, gpa]])
    prediccion = modelo.predict(entrada)[0]

    if prediccion == 1:
        st.success("🎉 Felicitaciones, te vas a graduar con honores 🎓", icon="✅")
    else:
        st.error("❌ No se graduará. ¡Sigue esforzándote!", icon="⚠️")

# Pie de página
st.markdown("---")
st.markdown("© 2025 Jose Vicente")