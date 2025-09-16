import numpy as np

print("registro de estudiantes uis")

n = int(input("cuantos estudiantes vas a ingresar: "))

codigos = []
nombres = []
carreras = []
anios = []
promedios = []
condicionales = []

for i in range(1, n+1):
    print(f"estudiante {i}")
    codigo = input("codigo: ").strip()
    nombre = input("nombre: ").strip()
    carrera = input("carrera: ").strip().lower()
    anio = int(input("año de ingreso: "))
    prom = float(input("promedio acumulado: ").replace(',', '.'))
    cond = input("esta condicional s/n: ").strip().lower()

    codigos.append(codigo)
    nombres.append(nombre)
    carreras.append(carrera)
    anios.append(anio)
    promedios.append(prom)
    condicionales.append(cond)

codigos = np.array(codigos, dtype=object)
nombres = np.array(nombres, dtype=object)
carreras = np.array(carreras, dtype=object)
anios = np.array(anios, dtype=int)
promedios = np.array(promedios, dtype=float)
condicionales = np.array(condicionales, dtype=object)

carrera_x = input("ingresa la carrera que quieres listar: ").strip().lower()
filtro1 = (carreras == carrera_x) & (promedios >= 4.0)
print("estudiantes de la carrera", carrera_x, "con promedio mayor o igual a 4")
for c, n in zip(codigos[filtro1], nombres[filtro1]):
    print("-", c, "|", n)
print("total:", codigos[filtro1].size)

filtro2 = (anios < 1990) & (condicionales == 's')
print("estudiantes que ingresaron antes de 1990 y estan condicionales")
for c, n in zip(codigos[filtro2], nombres[filtro2]):
    print("-", c, "|", n)
