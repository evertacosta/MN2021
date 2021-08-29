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

def graficar(t, y, dft, dfy, title):
    fig, ax = plt.subplots()
    ax.plot(dft, dfy, label='archivo')
    ax.plot(t, y, label='resultado')
    ax.set_title(title)
    plt.show()


t1, y1 = fourier_regla_trapezoidal(ejemplo1.t, ejemplo1.y, 40, 5000)
t2, y2 = fourier_regla_trapezoidal(ejemplo2.t, ejemplo2.y, 40, 5000)

graficar(t1, y1, ejemplo1.t, ejemplo1.y, 'ejemplo1 rt')
graficar(t2, y2, ejemplo2.t, ejemplo2.y, 'ejemplo2 rt')
