import streamlit as st
import plotly.graph_objects as go
import numpy as np

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Auditoría de Obsolescencia Profesional", layout="wide")

# --- CSS DE BLINDAJE TOTAL (Fuerza contraste máximo) ---
st.markdown("""
    <style>
    /* 1. Fondo general de la App y la Barra Lateral */
    .stApp, [data-testid="stSidebar"], [data-testid="stHeader"] {
        background-color: #FFFFFF !important;
    }

    /* 2. Texto General (Forzamos Negro Profundo) */
    h1, h2, h3, h4, h5, h6, p, li, span, label {
        color: #000000 !important;
    }

    /* 3. Menús Desplegables y Entradas de Texto (Contraste Crítico) */
    div[data-baseweb="select"] > div, 
    div[data-baseweb="popover"] div,
    [data-testid="stSelectbox"] div {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border-color: #CCCCCC !important;
    }

    /* 4. Opciones del Menú (Para que no se vean negras en el móvil) */
    ul[role="listbox"] li {
        background-color: #FFFFFF !important;
        color: #000000 !important;
    }
    
    /* 5. Métricas (Azul profesional) */
    div[data-testid="stMetricValue"] {
        color: #007BFF !important;
        font-size: 45px !important;
        font-weight: 800 !important;
    }

    /* 6. Expander de Referencias */
    .stExpander {
        background-color: #F8F9FA !important;
        border: 1px solid #DEE2E6 !important;
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
st.write("Análisis de relevancia académica frente a la evolución del mercado global.")

col1, col2 = st.columns([1, 2])

with col1:
    st.metric("Relevancia Actual", f"{valor_actual:.1f}%")
    st.markdown("### 💡 Diagnóstico")
    st.info(f"{desc_tipo} En el sector de {carrera}, la ventaja competitiva depende de la actualización constante.")

with col2:
    # Gráfica de decaimiento
    x = np.linspace(año_grad, 2035, 100)
    y = 100 * (0.5)**((x - año_grad) / v_media)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, line=dict(color='#007BFF', width=5), name="Curva de Valor"))
    fig.add_trace(go.Scatter(x=[2026], y=[valor_actual], marker=dict(color='#E63946', size=14, symbol='diamond'), name="Hoy (2026)"))
    
    fig.update_layout(template="plotly_white", height=400, margin=dict(l=10, r=10, t=30, b=10))
    st.plotly_chart(fig, on_select="ignore")

# --- SECCIÓN DE TRANSPARENCIA (Corregida con Raw String) ---
with st.expander("📚 Fuentes de Datos y Metodología (Transparencia)"):
    st.markdown(r"""
    * **Metodología Científica:** Basado en el concepto de *Half-life of Knowledge* (Samuel Arbesman).
    * **Habilidades Duras:** Datos ajustados según el reporte *'The Future of Jobs'* del **World Economic Forum (WEF)**.
    * **Habilidades Blandas:** Proyecciones de resiliencia laboral basadas en estándares de la **OCDE**.
    * **Cálculo:** Función de decaimiento exponencial:  
      $$Valor = 100 \cdot (0.5)^{\frac{t}{v}}$$
    """, unsafe_allow_html=True)

# --- LEYENDA OFICIAL ---
st.markdown("---")
st.markdown("<div style='text-align: center; color: #333333;'>Desarrollado por <b>Jesus Osmar Gutierrez Fernandez</b> con Python & Streamlit 🐍</div>", unsafe_allow_html=True)