import numpy as np

print("elecciones consejo superior")
print("ingresa los votos de cada candidato del 1 al 30")

votos = []
for i in range(1, 31):
    x = int(input(f"votos candidato {i}: "))
    votos.append(x)

v = np.array(votos, dtype=int)
total = int(v.sum())
print("total de votos:", total)

orden = np.argsort(-v)

print("lista de mayor a menor")
print("pos | candidato | votos")
for pos, idx in enumerate(orden, start=1):
    candidato = idx + 1
    print(f"{pos} | {candidato} | {int(v[idx])}")
