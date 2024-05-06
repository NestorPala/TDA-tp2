import sys


def inicializar_memo(n):
    memo = []
    z = -1
    for i in range(n):
        memo.append([])
        z += 1
        for j in range(n):
            memo[z].append(0)
    return memo


def indice_elemento_maximo(lista):
    maximo = lista[0]
    indice_maximo = 0

    for i in range(len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
            indice_maximo = i

    return indice_maximo


def beautify_solucion(indices_solucion, cantidad_oleadas_enemigos):
    beautified = []
    for i in range(1, cantidad_oleadas_enemigos + 1):
        if i in indices_solucion:
            beautified.append("Atacar")
        else:
            beautified.append("Cargar")
    return beautified


def reconstruir_solucion(memo):
    enemigos_eliminados = max(memo[len(memo) - 1])
    solucion = [ len(memo), ]
   
    indice = len(memo)
    while indice > 0:
        indice = indice_elemento_maximo(memo[indice - 1])
        if indice > 0:
            solucion.append(indice)

    return enemigos_eliminados, list(reversed(solucion))


def tp2_dp(lista_xi, lista_fj):
    n = len(lista_xi)
    OPT = inicializar_memo(n)

    for minuto_actual in range(1, n+1):
        for minuto_origen in range(n):

            if minuto_actual <= minuto_origen:
                continue

            if minuto_origen == 0:
                no_usar_opt = True

            minuto_actual_ = minuto_actual - 1

            if no_usar_opt:
                maximo_batallas_anteriores = 0
                no_usar_opt = False
            else:
                maximo_batallas_anteriores = max(OPT[minuto_origen - 1][:])

            j = minuto_actual_ - minuto_origen
            ataque_actual = min(lista_xi[minuto_actual_], lista_fj[j])

            # ecuacion de recurrencia: OPT[i][j] = max(OPT[i-1][k] ∀ k ∈ {0,...,j-1}) + min(X[i], f(j))
            # X = lista de cantidad enemigos en el minuto i ("lista_xi")
            # f = función de recarga ("lista_fj")

            OPT[minuto_actual_][minuto_origen] = maximo_batallas_anteriores + ataque_actual

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


# def main():
#     # 1413 ok
#     x = [271,533,916,656, 664]
#     f = [ 21,671,749,833,1543]

#     # 2118 ok
#     # x = [254,515, 647, 454, 126, 406,  69,  48, 781, 920]
#     # f = [170,312,1000,2131,2975,3026,3035,3402,3463,3496]

#     enemigos_eliminados, orden_recargar_atacar = tp2(x, f)

#     print("Enemigos eliminados: ", enemigos_eliminados)
#     print("Orden de recarga/ataque: ", orden_recargar_atacar)


main()
