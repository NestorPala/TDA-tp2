import matplotlib.pyplot as plt


# Pruebas de la catedra
x3 = [5, 10, 20, 50, 100, 200, 500, 1000, 5000]
y3 = [0.0009996891021728516,0.001069784164428711,0.0012545585632324219,0.0014770030975341797,
      0.0020072460174560547,0.0065190792083740234,0.042632102966308594,0.1700453758239746, 4.421553611755371]

# Pruebas propias
x2p = [100, 200, 500, 1000, 5000, 10000]
y2p = [0.0010771751403808594,0.007334709167480469,0.04227137565612793,
       0.17256784439086914,4.443042278289795,17.748655796051025]


#--------------------------------------


plt.scatter(x3, y3)

plt.plot(x3, y3, color='blue', linestyle='-', linewidth=1)

plt.xlabel('Cantidad de batallas')
plt.ylabel('Tiempo en segundos')
plt.title('Tiempo de ejecución del algoritmo en funcion de los datos de entrada\n \
          (Algoritmo O(n^2))')

plt.show()


#--------------------------------------


plt.scatter(x2p, y2p)

plt.plot(x2p, y2p, color='blue', linestyle='-', linewidth=1)

plt.xlabel('Cantidad de batallas')
plt.ylabel('Tiempo en segundos')
plt.title('Tiempo de ejecución del algoritmo en funcion de los datos de entrada\n \
          (Algoritmo O(n^2))')

plt.show()
