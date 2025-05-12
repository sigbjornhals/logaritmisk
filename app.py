import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Logaritmisk skala")
st.write("Skriv inn verdier for a og b i eksponentialfunksjonen")
st.latex(r"f(x) = a \cdot b^x")

# Input-felt
a = st.number_input("a:", value=2000.0, format="%.2f")
b = st.number_input("b:", value=1.15,  format="%.3f")
x_min = st.number_input("Nedre x-grense:", value=1.0, format="%.2f")
x_max = st.number_input("Øvre x-grense:", value=24.0, format="%.2f")

# Velg skala
x_log = st.checkbox("Logaritmisk x-akse", value=False)
y_log = st.checkbox("Logaritmisk y-akse", value=True)

# Valider input
if x_min >= x_max:
    st.error("Nedre grense må være < øvre grense")
elif x_log and x_min <= 0:
    st.error("Når x er log, må nedre grense > 0")
else:
    x = np.linspace(x_min, x_max, 500)
    y = a * b**x

    fig, ax = plt.subplots(figsize=(6,4))
    ax.plot(x,y,linewidth=2)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")

    if x_log:
        ax.set_xscale("log")
    if y_log:
        ax.set_yscale("log")
        ax.axhline(1, color="black", linewidth=1)

    ax.grid(True, which="both", ls="--", lw=0.5)
    st.pyplot(fig)
