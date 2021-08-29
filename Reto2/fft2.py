
import pandas as pd
from varios import *
import numpy as np
import matplotlib.pyplot as plt
import creardatos

def coeficientes_fft(y, n):
    c = np.fft.fft(y)
    #print(c)
    fft_n = (1/len(y)) * c
    an_list = []
    bn_list = []

    for i in range(1, n):

        an = -2 * abs(fft_n[i].real)
        bn = -2 * abs(fft_n[i].imag)
        an_list.append(an)
        bn_list.append(bn)
        print('i:{} - an: {} - bn: {}'.format(i, an, bn))

    return an_list, bn_list


def fourier_fft(t, y, n, intervalos):
    an_list, bn_list = coeficientes_fft(y, n)

    nuevo_y = np.zeros(intervalos)

    nuevo_t = np.linspace(t[0], t[len(t)-1], intervalos)

    ao = coeficiente_ao(y)

    w = frecuencia_angular(t)

    iteracion_n = 1

    for aj, bj in zip(an_list, bn_list):
        nuevo_y += aj*np.cos(iteracion_n*nuevo_t*w) + bj*np.sin(iteracion_n*nuevo_t*w)
        iteracion_n += 1

    return nuevo_t, ao + nuevo_y


def graficar(t, y, dft, dfy, title):
    fig, ax = plt.subplots()
    ax.plot(dft, dfy, label='archivo')
    ax.plot(t, y, label='resultado')
    ax.set_title(title)
    plt.show()


t1, y1 = fourier_fft(ejemplo1.t, ejemplo1.y, 10, 500)
t2, y2 = fourier_fft(ejemplo2.t, ejemplo2.y, 10, 500)
t3, y3 = fourier_fft(ejemplo3.t, ejemplo3.y, 10, 500)
t4, y4 = fourier_fft(ejemplo4.t, ejemplo4.y, 10, 500)
t5, y5 = fourier_fft(ejemplo_libro.t, ejemplo_libro.y, 10, 500)
t6, y6 = fourier_fft(ejemplo_analitico.t, ejemplo_analitico.y, 10, 2000)


graficar(t1, y1, ejemplo1.t, ejemplo1.y, 'ejemplo1 fft')
graficar(t2, y2, ejemplo2.t, ejemplo2.y, 'ejemplo2 fft')
graficar(t3, y3, ejemplo3.t, ejemplo3.y, 'ejemplo3 fft')
graficar(t4, y4, ejemplo4.t, ejemplo4.y, 'ejemplo4 fft')
graficar(t5, y5, ejemplo_libro.t, ejemplo_libro.y, 'ejemplo5 fft')
graficar(t6, y6, ejemplo_analitico.t, ejemplo_analitico.y, 'ejemplo analitico fft')
