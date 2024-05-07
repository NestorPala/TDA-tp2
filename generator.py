import random
import sys


def generate_arrays(n, a, b, c, d):
    x = [random.uniform(a, b) for _ in range(n)]
    f = [random.uniform(c, d) for _ in range(n)]
    for i in range(1, n):
        f[i] += f[i-1]
    return x, f


def write_to_file(x, f, filename):
    with open(filename, 'w', encoding="utf8") as file:
        file.write("N - N enemies values - N reload function values\n")
        file.write(str(len(x)) + '\n')
        for num in x:
            file.write(str(int(num)) + '\n')
        i = 0
        for num in f:
            str_ = str(int(num))
            if i < len(f) - 1:
                file.write(str_ + '\n')
            else: 
                file.write(str_)
            i += 1


def main():
    if len(sys.argv) != 2:
        print("Ejemplo de uso: python generator.py 500")
        return
    
    n = int(sys.argv[1])

    a = 1
    b = 100

    c = 10
    d = 20

    x, f = generate_arrays(n, a, b, c, d)
    write_to_file(x, f, f'{n}.txt')

    print("Archivo generado con éxito!")


main()
