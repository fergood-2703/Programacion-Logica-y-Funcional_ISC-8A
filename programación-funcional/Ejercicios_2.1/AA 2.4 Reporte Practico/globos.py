# Función normal
def inflar_globo():
    return "🎈"


# Función lambda
inflar_globo_lambda = lambda: "🎈"


# Pedimos el número de invitados una sola vez
numero_invitados = int(input("¿Cuántos invitados van a la fiesta? "))


# Lista de globos usando lambda y comprensión de listas
globos_lambda = [inflar_globo_lambda() for _ in range(numero_invitados)]


# Función para preparar globos
def preparar_globos(numero_invitados):
    globos = [inflar_globo() for _ in range(numero_invitados)]
    return globos


# Llamamos la función y guardamos el resultado
globos_fiesta = preparar_globos(numero_invitados)

# Mostramos la lista de globos
print(globos_fiesta)