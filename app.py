import streamlit as st
import plotly.graph_objects as go
import numpy as np
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Obsolescencia de Títulos", layout="wide")

# --- ESTILO DESIGN SYSTEM (DARK MODE & CIAN) ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    div[data-testid="stMetricValue"] { color: #00f2ff; }
    .stSlider > div > div > div > div { background-color: #00f2ff; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: INPUTS ---
with st.sidebar:
    st.header("⚙️ Configuración")
    año_graduacion = st.slider("Año de Graduación", 1990, 2026, 2018)
    vida_media = st.slider("Vida Media de la Habilidad (años)", 1, 15, 5)
    st.info("La 'Vida Media' es el tiempo que tarda en quedar obsoleto el 50% de lo que aprendiste.")

# --- LÓGICA: DECADENCIA EXPONENCIAL ---
año_actual = 2026
años_transcurridos = año_actual - año_graduacion

# Fórmula: Valor = 100 * (0.5) ^ (Años / Vida Media)
valor_actual = 100 * (0.5)**(años_transcurridos / vida_media)

# Generar puntos para la curva (desde graduación hasta 10 años al futuro)
x_linea = np.linspace(año_graduacion, año_actual + 10, 100)
y_linea = 100 * (0.5)**((x_linea - año_graduacion) / vida_media)

# --- VISUALIZACIÓN PRINCIPAL ---
st.title("🎓 Obsolescencia de Títulos")
st.markdown("¿Cuánto de lo que estudiaste sigue siendo relevante hoy?")

col1, col2 = st.columns([1, 2])

with col1:
    st.metric("Valor Actual del Título", f"{valor_actual:.1f}%")
    if valor_actual < 30:
        st.error("📉 Tu título es casi una pieza de museo. ¡Actualízate!")
    elif valor_actual < 60:
        st.warning("⚠️ Estás en la zona de riesgo. La obsolescencia te alcanza.")
    else:
        st.success("✅ Tu conocimiento aún es competitivo.")

with col2:
    # Gráfica Plotly
    fig = go.Figure()
    
    # Curva de decadencia
    fig.add_trace(go.Scatter(
        x=x_linea, y=y_linea,
        mode='lines',
        name='Curva de Decadencia',
        line=dict(color='#00f2ff', width=4)
    ))
    
    # Punto actual
    fig.add_trace(go.Scatter(
        x=[año_actual], y=[valor_actual],
        mode='markers+text',
        name='Hoy',
        text=["ESTÁS AQUÍ"],
        textposition="top right",
        marker=dict(color='red', size=15, symbol='x')
    ))
    
    fig.update_layout(
        template="plotly_dark",
        title="Valor del Conocimiento a través del Tiempo",
        xaxis_title="Año",
        yaxis_title="% de Relevancia",
        yaxis=dict(range=[0, 105]),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    st.plotly_chart(fig, use_container_width=True)

# --- LEYENDA OFICIAL ---
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #00f2ff; font-family: sans-serif; padding: 10px;'>
        <p style='font-size: 0.9rem;'>
            Desarrollado por <b>Jesus Osmar Gutierrez Fernandez</b> con <b>Python & Streamlit 🐍</b>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)