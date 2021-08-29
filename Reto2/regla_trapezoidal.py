import numpy as np
import pandas as pd
from math import pi


df1 = pd.read_csv('./data/ejemplo0.csv', delimiter=';')


# funcion trapezoidal para una serie
def dis_trapezoidal(t, y):

    h = (t[len(y)-1] - t[0]) / t.size

    suma = y[0]

    suma += (2*y[1:]).sum()

    suma += y[len(y)-1]

    I = h * (suma/2)
    #print(I)

    return I


def funcion(x):
    # return 0.2 + (25*x) - (200*x**2) + (675*x**3) - (900*x**4) + (400*x**5)
    return x

# Funciona trapezoidal para funciones explicitas
def trapezoidal(a, b, n):
    acu = 0

    h = (b - a)/n

    print('h:', h)

    x_n = []
    for i in range(0, n+1):
        x_n.append(acu)
        acu += h

    suma = funcion(a)

    for i in range(1, n):
        #print(i)
        suma += 2 * funcion(x_n[i])
    suma += funcion(x_n[n])

    I = h * (suma/2)

    print('integral', I)

#trapezoidal(0, 1, 10)

#t = np.linspace(0, 3, 500)
#y = t**2

#dis_trapezoidal(t, y)


t1 = np.linspace(-3, 3, 600)
y1 = t1 + 3




def anfr(t):
    w = (2*pi)/abs(t[len(t)-1] - t[0])
    T = abs(t[len(t)-1] - t[0])
    return w, T


def fourier(t, y, g):

    w, T = anfr(t)

    for j in range(1, g+1):
        aja = y * np.cos(j*w*t)
        aja2 = y * np.sin(j*w*t)

        aj = (2/T) * dis_trapezoidal(t, aja)
        bj = (2/T) * dis_trapezoidal(t, aja2)

        print('a{}:{}-b{}:{}'.format(j, aj, j, bj))

#df2 = pd.read_csv('./data/ejemplo4.csv', delimiter=';', names=['t', 'y'])
df3 = pd.read_csv('data/ejemplo_analitico.csv', delimiter=',', names=['t', 'y'])


#fourier(df2.t, df2.y, 3)
fourier(df3.t, df3.y, 10)

