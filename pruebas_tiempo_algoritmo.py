import time
from tp2 import tp2_batallas_solver
import sys

if len(sys.argv) == 2:
    archivo = sys.argv[1]

    start_time = time.time()

    _, _ = tp2_batallas_solver(archivo)

    end_time = time.time()
    execution_time = end_time - start_time

    print("Execution time:", execution_time, "seconds")
else:
    print("Ejemplo de uso: python3 tp2.py 500.txt")
    