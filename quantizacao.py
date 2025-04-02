import numpy as np
import streamlit as st
import matplotlib.pyplot as plt 
import komm



def main():
    st.title("Quantização")
    quantizer = komm.ScalarQuantizer(
        levels=[-2, -1, 0, 1, 2],
        thresholds=[-1.5, -0.3, 0.8, 1.4],

    )
    x = np.linspace(-5, 5, 1000)
    y = quantizer.quantize(x)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title("$Curva$ $entrada$ $\\times$ saida")
    ax.set_xlabel("Entrada")
    ax.set_ylabel("Saída")
    st.pyplot(fig)
    m = [-2.5, -2, -1.5, -1, 0]
    mq = quantizer.quantize(m)
    st.table({
        "$m[n]$":m,
        "$m_q[n]$":mq,

    })


main()