import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")
st.title("Principiul lui Malus")
st.write(
    r"Principiul lui Malus definește intensitatea luminii polarizate transmise, conform formulei:$$I_f=I_0 \cos^2\alpha$$"
)
st.sidebar.subheader("Profesor: Savu-Sorin Ciobanu")
st.sidebar.subheader("Student: Popa Ionut Cristian")
df = pd.read_excel("Malus.xlsx")
columns = df.columns.tolist()
ax = st.sidebar.selectbox("Alegeti variabila pentru coloana x", columns)
ay = st.sidebar.multiselect(
    "Alegeți axa Y (poți selecta mai multe!):", columns, default=[columns[-1]]
)
c1, c2 = st.columns(2)
with c1:
    st.subheader("Baza de date")
    st.dataframe(df)
with c2:
    st.subheader("grafic")
    st.line_chart(x=ax, y=ay, data=df)
