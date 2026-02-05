import streamlit as st
import plotly.graph_objects as go
import numpy as np

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Auditoría de Obsolescencia Profesional", layout="wide")

# --- DISEÑO CLARO PROFESIONAL (Light Mode) ---
st.markdown("""
    <style>
    /* Fondo blanco y texto negro */
    .main { background-color: #ffffff; color: #000000; }
    
    /* Ajuste de métricas para contraste */
    div[data-testid="stMetricValue"] { color: #007BFF; font-size: 45px; font-weight: bold; }
    div[data-testid="stMetricLabel"] { color: #333333; }
    
    /* Estilo para el Expander de Referencias */
    .stExpander { 
        border: 1px solid #dee2e6; 
        background-color: #f8f9fa; 
        border-radius: 8px;
    }
    .stMarkdown p { color: #000000; font-size: 1.05rem; }
    
    /* Estilo de los Sliders */
    .stSlider > div > div > div > div { background-color: #007BFF; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: INPUTS ESTRATÉGICOS ---
with st.sidebar:
    st.header("🔍 Perfil Profesional")
    carrera = st.selectbox("Área de Especialidad:", 
                         ["Tecnología / Software", "Salud / Medicina", "Leyes / Humanidades", "Ingeniería Industrial", "Marketing / Ventas"])
    
    año_grad = st.slider("Año de Graduación", 1990, 2026, 2020)
    
    st.divider()
    st.subheader("🛠️ Tipo de Habilidad")
    tipo_habilidad = st.radio("Enfocar análisis en:", ["Habilidades Duras (Técnicas)", "Habilidades Blandas (Soft Skills)"])

# --- LÓGICA DE CADUCIDAD ---
if tipo_habilidad == "Habilidades Duras (Técnicas)":
    v_media_map = {"Tecnología / Software": 2.5, "Salud / Medicina": 5, "Leyes / Humanidades": 10, "Ingeniería Industrial": 6, "Marketing / Ventas": 3}
    desc_tipo = "El conocimiento técnico caduca rápido por la automatización y nuevas herramientas."
else:
    v_media_map = {"Tecnología / Software": 12, "Salud / Medicina": 15, "Leyes / Humanidades": 20, "Ingeniería Industrial": 15, "Marketing / Ventas": 12}
    desc_tipo = "Las habilidades humanas (liderazgo, ética) son resilientes al tiempo."

v_media = v_media_map[carrera]
años_t = 2026 - año_grad
valor_actual = 100 * (0.5)**(años_t / v_media)

# --- VISUALIZACIÓN ---
st.title("🎓 Auditoría de Obsolescencia Profesional")
st.markdown(f"#### Análisis de {tipo_habilidad} | Sector: {carrera}")
st.write("Este informe calcula cuánto valor conserva su formación original frente a la evolución del mercado global.")

col1, col2 = st.columns([1, 2])

with col1:
    st.metric("Relevancia Actual", f"{valor_actual:.1f}%")
    
    st.markdown("### 💡 Diagnóstico")
    if carrera == "Tecnología / Software" and tipo_habilidad == "Habilidades Duras (Técnicas)":
        st.info("Debido a la IA y ciclos cortos de innovación, el conocimiento técnico se vuelve 'legado' rápidamente. Su valor reside hoy en la capacidad de re-aprendizaje.")
    elif carrera == "Leyes / Humanidades":
        st.info("Su campo conserva valor por estructuras institucionales estables, pero la digitalización de procesos está acelerando la erosión de la práctica tradicional.")
    else:
        st.info(f"{desc_tipo} En el sector de {carrera}, la ventaja competitiva se pierde si no hay una actualización en metodologías globales.")

with col2:
    # Gráfica de decaimiento
    x = np.linspace(año_grad, 2035, 100)
    y = 100 * (0.5)**((x - año_grad) / v_media)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, line=dict(color='#007BFF', width=4), name="Curva de Valor"))
    fig.add_trace(go.Scatter(x=[2026], y=[valor_actual], 
                             marker=dict(color='#DC3545', size=14, symbol='diamond'), 
                             name="Estado Actual (2026)"))
    
    fig.update_layout(
        template="plotly_white", # Cambio a plantilla blanca para visibilidad total
        height=450, 
        xaxis_title="Año / Evolución Temporal",
        yaxis_title="Valor del Título (%)",
        yaxis=dict(range=[0, 105]),
        margin=dict(l=20, r=20, t=40, b=20)
    )
    st.plotly_chart(fig, on_select="ignore")

# --- SECCIÓN DE TRANSPARENCIA (Legibilidad Mejorada) ---
with st.expander("📚 Fuentes de Datos y Metodología (Transparencia)"):
    st.markdown(f"""
    * **Metodología Científica:** Basado en el concepto de *Half-life of Knowledge* desarrollado por Samuel Arbesman.
    * **Habilidades Duras:** Datos ponderados según el reporte *'The Future of Jobs'* del **World Economic Forum (WEF)**, que proyecta cambios del 44% en habilidades técnicas para 2027.
    * **Habilidades Blandas:** Proyecciones de resiliencia laboral basadas en estándares de la **OCDE** para economías en transición digital.
    * **Cálculo:** Función de decaimiento exponencial: **Valor = 100 * (0.5)^(t/v)**, donde *t* es tiempo transcurrido y *v* es la vida media del sector.
    """)

# --- LEYENDA OFICIAL ---
st.markdown("---")
st.markdown("<div style='text-align: center; color: #333333;'>Desarrollado por <b>Jesus Osmar Gutierrez Fernandez</b> con Python & Streamlit 🐍</div>", unsafe_allow_html=True)