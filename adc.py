import komm
import matplotlib.pyplot as plt 
import numpy as np
import streamlit as st


from amostragem import amostragem, rescontrucao

def m(t:float) -> float:
    return 6 * np.sim(2*np.pi*t) - 0.0001

def main():
    st.title("Conversão A/D")
    fa = st.slider(
        label = "Taxa de amostragem $f_a$",
        min_values=2
        max_value=16,
        step=1,
        value=8,
        format ="%d amostras"

        col1,col2 = st.colu
        L = st.select_slider(

        )
        with col2:
        L = st.select_slider(
            label=" NUmero de níveis de qunatizaçao  $L$: ",
            option = [ 2, 4, 8, 16, 32, 64, 128, 256 ],
            value =16,
        )
        Ta = 1/fa
        Nb = int(np.log2(L))
        delta= 1#Do enunciado
        mp = 
        quantizer = Komm.UniformQuantizer(
            num_levels = L,
            input_range= (-8, 8),
            choice= "mid-riser"

        )
        tab1 = st.tabs(["quantizador", "Sinais"])
        with tab1:
            x = np.linspace(-8, 8, 1000)
            y = quantizer.quantize(x)
            fig, ax = plt.subplots()
            ax.plot(x, y)
            ax.set_title("$Curva$ $entrada$ $\\times$ saida")
            ax.set_xlabel("Entrada")
            ax.set_ylabel("Saída")
            ax.set_ylim(-8, 8)
            st.pyplot(fig)
            ax.grid()
            st.pyplot(fig)
            pass
            
        with tab2:
        a,b =(0.5 , 0.5)
        times = np.linspace(a, b,1000)
        Na = int (( b -a )/Ta)
        instantes, amostras = amostragem(m, Ta, a, Na)
        amostras_q = quunatizer.quantizer (amostras)
        m_hat = rescontrucao(amostras_q, a, Ta)
        fig, ax = plt.subplots()
        ax.plot(
            times,
            [m(t) for t in times],
            label = "$m(t)$",
        )
        ax.plot(
            instantes,
            amostras,
            linestyle="Nome",
            marker="o",
            label="$m[n]$",
        )
         ax.plot(
            instantes,
            amostras,
            linestyle="Nome",
            marker="o",
            label="$m[n]$",
        )
        ax.plot()
        ax.set_xlabel("$t$ [s]")
        ax.legend()
        st.pyplot(fig)
        
        
        main()
    )