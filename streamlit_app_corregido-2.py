
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Evaluación de Madurez Digital", layout="centered")

st.title("📊 Evaluación de Madurez Digital y CX")
st.write("Sube la plantilla Excel con los niveles de madurez por dimensión.")

uploaded_file = st.file_uploader("Cargar archivo Excel", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file, engine="openpyxl")

    if "Dimensión" in df.columns and "Nivel" in df.columns:
        st.subheader("📋 Datos cargados")
        st.dataframe(df)

        promedio = df["Nivel"].mean()
        st.markdown(f"### 🔢 Promedio de madurez: **{promedio:.2f}**")

        if promedio < 2:
            interpretacion = "La empresa tiene una madurez digital baja. Se recomienda iniciar un plan de transformación digital."
        elif promedio < 3.5:
            interpretacion = "La empresa tiene una madurez digital intermedia. Se recomienda optimizar el uso de datos y tecnologías para mejorar la experiencia del cliente."
        else:
            interpretacion = "La empresa tiene una madurez digital avanzada. Puede enfocarse en innovación y personalización."

        st.markdown(f"### 🧠 Interpretación:\n> {interpretacion}")
> {interpretacion}")

        # Gráfico radar
        st.subheader("📈 Visualización de madurez por dimensión")
        import numpy as np

        labels = df["Dimensión"].tolist()
        values = df["Nivel"].tolist()
        values += values[:1]
        angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
        angles += angles[:1]

        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
        ax.plot(angles, values, color="blue", linewidth=2)
        ax.fill(angles, values, color="skyblue", alpha=0.4)
        ax.set_yticks([1, 2, 3, 4, 5])
        ax.set_yticklabels(["1", "2", "3", "4", "5"])
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(labels)
        st.pyplot(fig)
    else:
        st.error("El archivo debe contener las columnas 'Dimensión' y 'Nivel'.")
