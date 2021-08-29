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


def export_lists(name, aj, bj):
    df = pd.DataFrame({'aj': aj, 'bj': bj})
    df.to_csv('./coeficientes_minimos_cuadrados/{}.csv'.format(name), index=False)


def fourier(t, y, g, title, resolucion):

    aj_list = []
    bj_list = []

    print("\nFuncion {}".format(title))

    print(len(t)-1)
    w = (2*np.pi)/abs(t[len(t)-1] - t[0])

    print("Frecuencia angular:{}".format(w))

    n = y.size
    a0 = y.sum()/n

    print(a0, n)

    resultado = np.zeros(resolucion)

    ax = create_fig(t, y, title)

    for j in range(1, g+1):
        print('Iteracion #:{}'.format(j))
        ycoswt = y*np.cos(j*w*t)
        ysinwt = y*np.sin(j*w*t)

        # print(ycoswt)

        aj = (2/n) * ycoswt.sum()
        bj = (2/n) * ysinwt.sum()

        #print('suma cos', ycoswt.sum())
        #print('suma sen', ysinwt.sum())

        aj_list.append(aj)
        bj_list.append(bj)
        print('Coeficientes')
        print('A{}:{}--B{}:{}'.format(j, aj, j,  bj))

        new_t = np.linspace(t[0], t[len(t)-1], resolucion)

        resultado += aj*np.cos(j*w*new_t) + bj*np.sin(j*w*new_t)
        add_ax(ax, new_t, resultado, a0)

    #export_lists(title, aj_list, bj_list)


df1 = pd.read_csv('./data/ejemplo1.csv', delimiter=';', names=['t', 'y'])
df2 = pd.read_csv('./data/ejemplo2.csv', delimiter=';', names=['t', 'y'])
df3 = pd.read_csv('./data/ejemplo3.csv', delimiter=';', names=['t', 'y'])
df4 = pd.read_csv('./data/ejemplo4.csv', delimiter=';', names=['t', 'y'])
df5 = pd.read_csv('data/ejemplo_analitico.csv', delimiter=',', names=['t', 'y'])
df6 = pd.read_csv('data/ejemplo_libro.csv', delimiter=',', names=['t', 'y'])

#fourier(t1, y1, 5, 'guia', 500)
fourier(df1.t, df1.y, 40, 'ejemplo1', 5000)
fourier(df2.t, df2.y, 40, 'ejemplo2', 5000)
fourier(df3.t, df3.y, 40, 'ejemplo3', 5000)
fourier(df4.t, df4.y, 40, 'ejemplo4', 5000)

#fourier(df5.t, df5.y, 10, 'ejemplo final', 2000)

#fourier(df6.t, df6.y, 1, 'example book', 10)

