from varios import *
import numpy as np
import matplotlib.pyplot as plt


def coeficientes_fft(y, n):
    c = np.fft.fft(y)
    #print(c)
    fft_n = (1/len(y)) * c
    an_list = []
    bn_list = []

    positivos = len(fft_n)//2

    for i in range(1, n):

        an = 2 * fft_n[i].real
        bn = 2 * fft_n[-i].imag
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


n = 10

t1, y1 = fourier_fft(ejemplo1.t, ejemplo1.y, n, 500)
t2, y2 = fourier_fft(ejemplo2.t, ejemplo2.y, n, 500)
t3, y3 = fourier_fft(ejemplo3.t, ejemplo3.y, n, 500)
t4, y4 = fourier_fft(ejemplo4.t, ejemplo4.y, n, 500)
t5, y5 = fourier_fft(ejemplo_libro.t, ejemplo_libro.y, 5, 500)
t6, y6 = fourier_fft(ejemplo_analitico.t, ejemplo_analitico.y, 100, 2000)

t7, y7 = fourier_fft(ejemploatp1.t, ejemploatp1.v, 100, 500)
t8, y8 = fourier_fft(ejemploatp2.t, ejemploatp2.v, 100, 500)


graficar(t1, y1, ejemplo1.t, ejemplo1.y, 'Ejemplo 1 fft', n)
graficar(t2, y2, ejemplo2.t, ejemplo2.y, 'Ejemplo 2 fft', n)
graficar(t3, y3, ejemplo3.t, ejemplo3.y, 'Ejemplo 3 fft', n)
graficar(t4, y4, ejemplo4.t, ejemplo4.y, 'Ejemplo 4 fft', n)
graficar(t5, y5, ejemplo_libro.t, ejemplo_libro.y, 'Ejemplo libro fft', 5)
graficar(t6, y6, ejemplo_analitico.t, ejemplo_analitico.y, 'Ejemplo analitico fft', 100)

graficar(t7, y7, ejemploatp1.t, ejemploatp1.v, 'Ejemplo atp 1 fft', 100)
graficar(t8, y8, ejemploatp2.t, ejemploatp2.v, 'Ejemplo atp 2 fft', 100)
