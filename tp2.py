import math
import sys


def beautify_solucion(indices_solucion, cantidad_oleadas_enemigos):
    beautified = []
    for i in range(1, cantidad_oleadas_enemigos + 1):
        if i in indices_solucion:
            beautified.append("Atacar")
        else:
            beautified.append("Cargar")
    return beautified


def reconstruir_solucion(memo):
    enemigos_eliminados = memo[len(memo) - 1][0]
    solucion = [ len(memo), ]
   
    indice = len(memo)
    while indice > 0:
        indice = memo[indice - 1][1]
        if indice > 0:
            solucion.append(indice)

    return enemigos_eliminados, list(reversed(solucion))


def tp2_dp(lista_xi, lista_fj):
    n = len(lista_xi)

    # Maximos batallas anteriores
    OPT = []

    for minuto_actual in range(1, n+1):
        maximo_batalla_actual = -math.inf
        minuto_maximo_batalla_actual = 0

        for minuto_origen in range(n):
            if minuto_actual <= minuto_origen:
                continue
            
            if minuto_origen == 0:
                maximo_batallas_anteriores = 0
            else:
                maximo_batallas_anteriores = OPT[minuto_origen - 1][0]

            j = (minuto_actual - 1) - minuto_origen
            ataque_actual = min(lista_xi[minuto_actual - 1], lista_fj[j])

            abatidos_batalla_actual = maximo_batallas_anteriores + ataque_actual

            if abatidos_batalla_actual > maximo_batalla_actual:
                maximo_batalla_actual = abatidos_batalla_actual
                minuto_maximo_batalla_actual = minuto_origen
        
        OPT.append((maximo_batalla_actual, minuto_maximo_batalla_actual))

    return OPT


def tp2(x, f):
    memo = tp2_dp(x, f)
    cantidad_oleadas_enemigos = len(x)

    enemigos_eliminados, indices_solucion = reconstruir_solucion(memo)
    orden_recargar_atacar = beautify_solucion(indices_solucion, cantidad_oleadas_enemigos)

    return enemigos_eliminados, orden_recargar_atacar


def tp2_batallas_solver(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()[1:]
        
    n = int(lines[0].strip())
    x_values = [int(x.strip()) for x in lines[1:n+1]]
    function_values = [int(x.strip()) for x in lines[n+1:]]

    return tp2(x_values, function_values)


def escribir_resultados(filename, enemigos_eliminados, orden_recargar_atacar):
    with open(f"solved_{filename}", 'w+') as resultados_file:
        resultados_file.write(filename)

        estrategia = ""
        for i in range(len(orden_recargar_atacar)):
            orden = orden_recargar_atacar[i]
            estrategia += orden
            if i < len(orden_recargar_atacar) - 1:
                estrategia += ", "

        resultados_file.write("\nEstrategia: " + estrategia)
        resultados_file.write("\nCantidad de tropas eliminadas: " + str(enemigos_eliminados))
        resultados_file.write("\n")


def main():
    if len(sys.argv) != 2:
        print("Ejemplo de uso: python3 tp2.py 500.txt")
        return
    
    path = sys.argv[1]
    filename = path.split(".")[0] + ".txt"
    
    enemigos_eliminados, orden_recargar_atacar = tp2_batallas_solver(path)

    escribir_resultados(filename, enemigos_eliminados, orden_recargar_atacar)

    print("\nArchivo procesado con éxito!")
    print(f"Los resultados se encuentran en el archivo solved_{filename}")


main()
