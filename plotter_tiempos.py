import matplotlib.pyplot as plt


# O(n^3) algorithm - 10.txt
x2 = [5, 10, 20, 50, 100, 200, 500, 1000]
y2 = [0.00099945068359375000, 0.00000000000000000000, 0.00150609016418457031,
        0.00203466415405273438, 0.02012777328491210938, 0.06371688842773437500,
        0.74523496627807617188, 5.32637214660644531250]

# O(n^2) algorithm - 10.txt
x3 = [5, 10, 20, 50, 100, 200, 500, 1000]
y3 = [0.00099754333496093750, 0.00000000000000000000, 0.00099873542785644531,
        0.00100183486938476562, 0.00507354736328125000, 0.01508188247680664062,
        0.08023452758789062500, 0.24034714698791503906]


plt.scatter(x2, y2)

plt.plot(x2, y2, color='blue', linestyle='-', linewidth=1)

plt.xlabel('Cantidad de batallas')
plt.ylabel('Tiempo en segundos')
plt.title('Tiempo de ejecución del algoritmo en funcion de los datos de entrada\n \
          (Algoritmo O(n^3))')

plt.show()


#--------------------------------------


plt.scatter(x3, y3)

plt.plot(x3, y3, color='blue', linestyle='-', linewidth=1)

plt.xlabel('Cantidad de batallas')
plt.ylabel('Tiempo en segundos')
plt.title('Tiempo de ejecución del algoritmo en funcion de los datos de entrada\n \
          (Algoritmo O(n^2))')

plt.show()
