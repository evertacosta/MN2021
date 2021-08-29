from varios import *
import numpy as np


def coeficientes_minimos_cuadrados(t, y, n):
    """
    Calcula los coeficientes de Fourier implemetando el algoritmo de los
    minimos cuadrados
    :param t: Rango de una funcion discreta
    :param y:
    :param n:
    :return: tupla de lista
    """

    w = frecuencia_angular(t)

    N = y.size

    aj_list = []
    bj_list = []
    for j in range(1, n+1):
        ycoswt = y*np.cos(j*w*t)
        ysinwt = y*np.sin(j*w*t)

        aj = (2/N) * ycoswt.sum()
        bj = (2/N) * ysinwt.sum()

        aj_list.append(aj)
        bj_list.append(bj)

    return aj_list, bj_list


def fourier_minimos_cuadrados(t, y, n, intervalos):
    # nuevo dominio de la funcion final correspondiente
    # numero intervalos independiente a los del archivo de muestreo
    nuevo_t = np.linspace(t[0], t[len(t)-1], intervalos)

    nuevo_y = np.zeros(intervalos)

    w = frecuencia_angular(t)

    ao = coeficiente_ao(y)

    an, bn = coeficientes_minimos_cuadrados(t, y, n)

    iteracion_n = 1

    for aj, bj in zip(an, bn):

        nuevo_y += aj*np.cos(iteracion_n*w*nuevo_t) + bj*np.sin(iteracion_n*w*nuevo_t)
        iteracion_n += 1

    return nuevo_t, ao + nuevo_y


t1, y1 = fourier_minimos_cuadrados(ejemplo1.t, ejemplo1.y, 40, 5000)
t2, y2 = fourier_minimos_cuadrados(ejemplo2.t, ejemplo2.y, 40, 5000)



t6, y6 = fourier_minimos_cuadrados(ejemplo_analitico.t, ejemplo_analitico.y, 60, 5000)

graficar(t1, y1, ejemplo1.t, ejemplo1.y, 'ejemplo1 mc')
graficar(t2, y2, ejemplo2.t, ejemplo2.y, 'ejemplo2 mc')
graficar(t6, y6, ejemplo_analitico.t, ejemplo_analitico.y, 'ejemplo final mc')
