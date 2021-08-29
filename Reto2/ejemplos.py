import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x = np.linspace(-1, 1, 2000)


def an(n):
    return (((-1)**n)-1)/((n**2)*(np.pi**2))


def bn(n):
    return (-1)/(n*np.pi)


def ejemplo3(x, n, puntos):
    ao = 3/4

    final = np.zeros(puntos)

    for i in range(1, n):
        final += ((an(i)*np.cos(i*np.pi*x)) + (bn(i)*np.sin(i*np.pi*x)))

    return ao + final



def graficar(t, y):
    fig, ax = plt.subplots()
    ax.plot(t, y, label='archivo')
    plt.show()


if __name__ == "__main__":

    df5 = pd.read_csv('data/ejemplo_analitico.csv', delimiter=',', names=['t', 'y'])

    n = int(input('numero de sumas'))
    print('Coeficientes')
    for i in range(1, n):
        print('i:{} - an: {} - bn: {}'.format(i, an(i), bn(i)))

    fig, ax = plt.subplots()
    ax.plot(df5.t, df5.y, label='archivo')
    ax.plot(x, ejemplo3(x, n, 2000), label='resultado')
    ax.set_title('ejemplo analitico')
    plt.show()
