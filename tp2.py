def inicializar_memo(n):
    memo = []
    z = -1
    for i in range(n):
        memo.append([])
        z += 1
        for j in range(n):
            memo[z].append(0)
    return memo


def reconstruir_solucion(memo):
    pass


def tp2_dp(lista_xi, lista_fj):
    n = len(lista_xi)
    OPT = inicializar_memo(n)
    enemigos_eliminados = 0

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

    print(OPT)

    return enemigos_eliminados, OPT


def tp2(x, f):
    enemigos_eliminados, memo = tp2_dp(x, f)
    orden_recargar_atacar = reconstruir_solucion(memo)
    return enemigos_eliminados, orden_recargar_atacar


def main():
    # 1413 ok
    x = [271,533,916,656, 664]
    f = [ 21,671,749,833,1543]

    # 2118 ok
    # x = [254,515, 647, 454, 126, 406,  69,  48, 781, 920]
    # f = [170,312,1000,2131,2975,3026,3035,3402,3463,3496]

    enemigos_eliminados, orden_recargar_atacar = tp2(x, f)

    print("Enemigos eliminados: ", enemigos_eliminados)
    print("Orden de recarga/ataque: ", orden_recargar_atacar)


main()
