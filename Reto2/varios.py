import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def frecuencia_angular(t):
    """
    Calcula la frecuencia angular de una funcion discreta
    :param t: np.array
    :return: float
    """
    return (2*np.pi)/periodo(t)


def periodo(t):
    """
    Calcula el periodo de la funcion discreta
    :param t: np.array
    :return: float
    """
    return abs(t[len(t)-1] - t[0])


def coeficiente_ao(y):
    return y.sum()/y.size


def graficar(t, y, dft, dfy, title):
    fig, ax = plt.subplots()
    ax.plot(dft, dfy, label='archivo')
    ax.plot(t, y, label='resultado')
    ax.set_title(title)
    plt.show()


ejemplo1 = pd.read_csv('./data/ejemplo1.csv', delimiter=';', names=['t', 'y'])
ejemplo2 = pd.read_csv('./data/ejemplo2.csv', delimiter=';', names=['t', 'y'])
ejemplo3 = pd.read_csv('./data/ejemplo3.csv', delimiter=';', names=['t', 'y'])
ejemplo4 = pd.read_csv('./data/ejemplo4.csv', delimiter=';', names=['t', 'y'])
ejemplo_libro = pd.read_csv('data/ejemplo_libro.csv', delimiter=',', names=['t', 'y'])
ejemplo_analitico = pd.read_csv('./data/ejemplo_analitico.csv', delimiter=',', names=['t', 'y'])
ejemploatp1 = pd.read_csv("./data/Ejemplo_ATP01.adf", delimiter='\t', names=['t', 'v', 'a', 'n'], skiprows=2)
ejemploatp2 = pd.read_csv("./data/Ejemplo_ATP01.adf", delimiter='\t', names=['t', 'v', 'a', 'n'], skiprows=2)
