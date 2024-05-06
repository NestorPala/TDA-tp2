from tp2 import tp2_batallas_solver

# (file, expected_sum)
amounts = [
    ("5", 1413),
    ("10", 2118),
    ("10_bis", 1237),
    ("20", 11603),
    ("50", 3994),
    ("100", 7492),
    ("200", 4230),
    ("500", 15842),
    ("1000", 4508),
    ("5000", 504220),
]

for a in amounts:
    sum_, _ = tp2_batallas_solver(f"tests_catedra\\data\\{a[0]}.txt")
    print(f"'Cantidad de enemigos abatidos' for value '{a}': {sum_} - ", end="")
    assert sum_ == a[1]
    print("OK!")