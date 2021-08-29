import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def crear_ejemplo():

    t = np.linspace(-1, 1, 10)

    a = []

    for i in t:
        if i < 0:
            a.append(1)

    y = np.concatenate((np.array(a), t[5:]), axis=None)

    print(y)

    df = pd.DataFrame({'t': t, 'y': y}, columns=['t', 'y'])

    return df.t, df.y


def graficar(t, y):
    fig, ax = plt.subplots()
    ax.plot(t, y, label='archivo')
    ax.set_title('ejemplo creado')
    plt.show()

t, y = crear_ejemplo()

graficar(t, y)
#df.to_csv('./data/ejemplo_analitico.csv', index=False)
