import os
import time
from tp2 import ABS_OPTION, FILE_OPTION, USO, tp2_batallas_solver
import sys

if len(sys.argv) == 3 and sys.argv[1] in [FILE_OPTION, ABS_OPTION]:
    if (sys.argv[1] == FILE_OPTION):
        path = sys.argv[2]
    else:
        path = os.path.normpath(sys.argv[2])

    start_time = time.time()

    _, _ = tp2_batallas_solver(path)

    end_time = time.time()
    execution_time = end_time - start_time

    print("Execution time:", execution_time, "seconds")
else:
    print(USO)
    