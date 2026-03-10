import streamlit as st

st.title("Physics Equations")

st.write("This page displays some important physics equations.")

st.header("1. Newton's Second Law")
st.latex(r"F = ma")

st.header("2. Einstein Mass-Energy Equation")
st.latex(r"E = mc^2")

st.header("3. Kinematic Equation")
st.latex(r"v = u + at")

st.header("4. Gravitational Force")
st.latex(r"F = \frac{G m_1 m_2}{r^2}")

st.header("5. Ohm's Law")
st.latex(r"V = IR")

st.write("These equations are commonly used in physics.")

