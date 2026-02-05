import streamlit as st
import plotly.graph_objects as go
import numpy as np

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Auditoría de Obsolescencia Profesional", layout="wide")

# --- CSS DE BLINDAJE VISUAL (Fuerza fondo blanco y texto negro) ---
st.markdown("""
    <style>
    /* Obligamos a toda la app a ser fondo blanco */
    .stApp {
        background-color: #FFFFFF !important;
        color: #000000 !important;
    }
    
    /* Forzamos el color negro en párrafos, títulos y métricas */
    h1, h2, h3, h4, p, li, span, div {
        color: #1A1A1A !important;
    }

    /* Estilo para las métricas (Azul profesional sobre blanco) */
    div[data-testid="stMetricValue"] {
        color: #007BFF !important;
        font-size: 48px !important;
        font-weight: 800 !important;
    }

    /* Estilo para el Expander de Referencias (Gris muy claro) */
    .stExpander {
        background-color: #F1F3F5 !important;
        border: 1px solid #DEE2E6 !important;
        border-radius: 10px !important;
    }

    /* Ajuste para que los Sliders se vean bien */
    .stSlider > div > div > div > div {
        background-color: #007BFF !important;
    }

    /* Sidebar con contraste moderado */
    section[data-testid="stSidebar"] {
        background-color: #F8F9FA !important;
        border-right: 1px solid #E9ECEF !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: INPUTS ---
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
    desc_tipo = "El conocimiento técnico caduca rápido por la automatización."
else:
    v_media_map = {"Tecnología / Software": 12, "Salud / Medicina": 15, "Leyes / Humanidades": 20, "Ingeniería Industrial": 15, "Marketing / Ventas": 12}
    desc_tipo = "Las habilidades humanas son resilientes al tiempo."

v_media = v_media_map[carrera]
años_t = 2026 - año_grad
valor_actual = 100 * (0.5)**(años_t / v_media)

# --- VISUALIZACIÓN ---
st.title("🎓 Auditoría de Obsolescencia Profesional")
st.write("Informe técnico sobre la relevancia de su formación académica frente al mercado global.")

col1, col2 = st.columns([1, 2])

with col1:
    st.metric("Relevancia Actual", f"{valor_actual:.1f}%")
    
    st.markdown("### 💡 Diagnóstico")
    if carrera == "Tecnología / Software" and tipo_habilidad == "Habilidades Duras (Técnicas)":
        st.info("Debido a la IA y ciclos cortos de innovación, el conocimiento técnico se vuelve 'legado' rápidamente.")
    else:
        st.info(f"{desc_tipo} En {carrera}, la ventaja competitiva depende de la actualización metodológica constante.")

with col2:
    # Gráfica de decaimiento
    x = np.linspace(año_grad, 2035, 100)
    y = 100 * (0.5)**((x - año_grad) / v_media)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, line=dict(color='#007BFF', width=5), name="Curva de Valor"))
    fig.add_trace(go.Scatter(x=[2026], y=[valor_actual], 
                             marker=dict(color='#E63946', size=15, symbol='diamond'), 
                             name="Estado Actual (2026)"))
    
    fig.update_layout(
        template="plotly_white", # Fondo blanco para máxima claridad
        height=450, 
        xaxis_title="Evolución Temporal",
        yaxis_title="Valor (%)",
        yaxis=dict(range=[0, 105]),
        margin=dict(l=20, r=20, t=40, b=20)
    )
    st.plotly_chart(fig, on_select="ignore")

# --- SECCIÓN DE TRANSPARENCIA (Legibilidad forzada) ---
with st.expander("📚 Fuentes de Datos y Metodología (Transparencia)"):
    st.markdown(f"""
    * **Metodología Científica:** Basado en el concepto de *Half-life of Knowledge* (Samuel Arbesman).
    * **Habilidades Duras:** Reporte *'The Future of Jobs'* del **World Economic Forum (WEF)**.
    * **Habilidades Blandas:** Proyecciones de resiliencia laboral de la **OCDE**.
    * **Cálculo:** Función de decaimiento exponencial: **Valor = 100 * (0.5)^(t/v)**.
    """)

# --- LEYENDA OFICIAL ---
st.markdown("---")
st.markdown("<div style='text-align: center; color: #333333;'>Desarrollado por <b>Jesus Osmar Gutierrez Fernandez</b> con Python & Streamlit 🐍</div>", unsafe_allow_html=True)