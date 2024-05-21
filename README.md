# TP2 de TDA - FIUBA


### Integrantes

* Palavecino Arnold, Nestor Fabian - 108244
* Vázquez Morales, Matias - 111083


## Probar el TP2 con un archivo de pruebas de "n" batallas

Si el archivo está en la misma carpeta que tp2.py:

<code>python tp2.py -file NUMERO_DE_BATALLAS.txt</code>

Ejemplo: *python tp2.py -file 50.txt*

<br>

Si el archivo está en cualquier ruta:

<code>python tp2.py -abs PATH_TO_/NUMERO_DE_BATALLAS.txt</code>

Ejemplo: *python tp2.py -abs C:\Users\Nestor\Desktop\50.txt*

----

## Ejecutar tests de la cátedra

Se corren junto con las pruebas de tiempo. 

<code>python ejecutar_tests_catedra.py</code>

----

## Ejecutar las pruebas de tiempo del algoritmo

Estas pruebas se pueden correr para cualquier archivo de batallas. 

<br>

Si el archivo está en la misma carpeta que pruebas_tiempo_algoritmo.py:

<code>python pruebas_tiempo_algoritmo.py -file NUMERO_DE_BATALLAS.txt</code>

Ejemplo: *python pruebas_tiempo_algoritmo.py -file 50.txt*

<br>

Si el archivo está en cualquier ruta:

<code>python pruebas_tiempo_algoritmo.py -abs PATH_TO_/NUMERO_DE_BATALLAS.txt</code>

Ejemplo: *python pruebas_tiempo_algoritmo.py -abs C:\Users\Nestor\Desktop\50.txt*

----

## Generar archivo de conjunto de batallas de tamaño "n"

<code>python generator.py VALOR_N_ENTERO</code>