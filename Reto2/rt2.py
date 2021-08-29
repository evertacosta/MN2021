from varios import *
import numpy as np


def integracion_trapezoidal_discretas(t, y):
    h = (t[len(y)-1] - t[0]) / t.size

    suma = y[0]

    suma += (2*y[1:]).sum()

    suma += y[len(y)-1]

    I = h * (suma/2)

    return I


def coeficientes_regla_trapezoidal(t, y, n):

    aj_list = []
    bj_list = []

    w = frecuencia_angular(t)

    T = periodo(t)

    for j in range(1, n+1):
        componente_cos = y * np.cos(j*w*t)
        componente_sen = y * np.sin(j*w*t)

        aj = (2/T) * integracion_trapezoidal_discretas(t, componente_cos)
        bj = (2/T) * integracion_trapezoidal_discretas(t, componente_sen)

        aj_list.append(aj)
        bj_list.append(bj)

    return aj_list, bj_list


def fourier_regla_trapezoidal(t, y, n, intervalos):
    # nuevo dominio de la funcion final correspondiente
    # numero intervalos independiente a los del archivo de muestreo
    nuevo_t = np.linspace(t[0], t[len(t)-1], intervalos)

    nuevo_y = np.zeros(intervalos)

    w = frecuencia_angular(t)

    ao = coeficiente_ao(y)

    an, bn = coeficientes_regla_trapezoidal(t, y, n)

    iteracion_n = 1

    for aj, bj in zip(an, bn):

        nuevo_y += aj*np.cos(iteracion_n*w*nuevo_t) + bj*np.sin(iteracion_n*w*nuevo_t)
        iteracion_n += 1

    return nuevo_t, ao + nuevo_y


t1, y1 = fourier_regla_trapezoidal(ejemplo1.t, ejemplo1.y, 10, 500)
t2, y2 = fourier_regla_trapezoidal(ejemplo2.t, ejemplo2.y, 10, 500)
t3, y3 = fourier_regla_trapezoidal(ejemplo3.t, ejemplo3.y, 10, 500)
t4, y4 = fourier_regla_trapezoidal(ejemplo4.t, ejemplo4.y, 10, 500)
t5, y5 = fourier_regla_trapezoidal(ejemplo_libro.t, ejemplo_libro.y, 10, 500)
t6, y6 = fourier_regla_trapezoidal(ejemplo_analitico.t, ejemplo_analitico.y, 10, 2000)

t7, y7 = fourier_regla_trapezoidal(ejemploatp1.t, ejemploatp1.v, 100, 500)
t8, y8 = fourier_regla_trapezoidal(ejemploatp2.t, ejemploatp2.v, 100, 500)

graficar(t1, y1, ejemplo1.t, ejemplo1.y, 'Ejemplo 1 Regla Trapezoidal')
graficar(t2, y2, ejemplo2.t, ejemplo2.y, 'Ejemplo 2 Regla Trapezoidal')
graficar(t3, y3, ejemplo3.t, ejemplo3.y, 'Ejemplo 3 Regla Trapezoidal')
graficar(t4, y4, ejemplo4.t, ejemplo4.y, 'Ejemplo 4 Regla Trapezoidal')
graficar(t5, y5, ejemplo_libro.t, ejemplo_libro.y, 'Ejemplo Libro Regla Trapezoidal')
graficar(t6, y6, ejemplo_analitico.t, ejemplo_analitico.y, 'Ejemplo analitico Regla Trapezoidal')

graficar(t7, y7, ejemploatp1.t, ejemploatp1.v, 'Ejemplo atp 1 Regla Trapezoidal')
graficar(t8, y8, ejemploatp2.t, ejemploatp2.v, 'Ejemplo atp 2 Regla Trapezoidal')
