m = input("Nome do motorista: ")
d = float(input("Distância do percurso (km): "))
v = float(input(f"Velocidade de {m} (km/h): "))
t = float(d/v)
print(f'{m} levará cerca de {t} horas para percorrer {d}km a uma velocidade de {v} km/h.')