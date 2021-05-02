import pandas as pd
from math import pi
import matplotlib.pyplot as plt
import numpy as np

t1 = np.linspace(-3, 3, 600)
y1 = t1 + 3


def graficar(t, y, resultado, a0, title):
    fig, ax = plt.subplots()
    ax.plot(t, y, label='archivo')
    ax.set_title(title)
    ax.plot(t, resultado + a0, label='Fourier')


def create_fig(t, y, title):
    fig, ax = plt.subplots()
    ax.plot(t, y, label='archivo')
    ax.set_title(title)
    ax.legend()
    return ax


def add_ax(ax, t, resultado, a0):
    ax.plot(t, resultado + a0, label='Fourier')


def fourier(t, y, g, title, resolucion):
    print("\nFuncion {}".format(title))

    w = (2*pi)/abs(t[len(t)-1] - t[0])
    print("Frecuencia angular:{}".format(w))

    n = y.size
    a0 = y.sum()/n

    resultado = np.zeros(resolucion)

    ax = create_fig(t, y, title)

    for j in range(1, g+1):
        print('Iteracion #:{}'.format(j))
        ycoswt = y*np.cos(j*w*t)
        ysinwt = y*np.sin(j*w*t)

        # print(ycoswt)

        aj = (2/n) * ycoswt.sum()
        bj = (2/n) * ysinwt.sum()

        print('suma cos', ycoswt.sum())
        print('suma sen', ysinwt.sum())

        print('A{}:{}--B{}:{}'.format(j, aj, j,  bj))

        new_t = np.linspace(t[0], t[len(t)-1], resolucion)

        resultado += aj*np.cos(j*w*new_t) + bj*np.sin(j*w*new_t)
        add_ax(ax, new_t, resultado, a0)


df1 = pd.read_csv('./data/ejemplo1.csv', delimiter=';', names=['t', 'y'])
df2 = pd.read_csv('./data/ejemplo2.csv', delimiter=';', names=['t', 'y'])
df3 = pd.read_csv('./data/ejemplo3.csv', delimiter=';', names=['t', 'y'])
df4 = pd.read_csv('./data/ejemplo4.csv', delimiter=';', names=['t', 'y'])


fourier(t1, y1, 3, 'guia', 500)
fourier(df1.t, df1.y, 10, 'ejemplo1', 500)
fourier(df2.t, df2.y, 6, 'ejemplo2', 500)
fourier(df3.t, df3.y, 3, 'ejemplo3', 500)
fourier(df4.t, df4.y, 3, 'ejemplo4', 500)
