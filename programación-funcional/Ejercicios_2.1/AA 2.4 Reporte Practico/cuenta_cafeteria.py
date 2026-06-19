from functools import reduce

orden = [25.50, 22.00, 35.75, 40.00, 18.50]

# Aplicar 10% de descuento
precios_con_descuento = list(
    map(lambda precio: precio * 0.90, orden)
)

print(precios_con_descuento)


# Filtrar bebidas con precio mayor a 25
bebidas_caras = list(
    filter(lambda precio: precio > 25, precios_con_descuento)
)

print(bebidas_caras)


# Sumar las bebidas 
total = reduce(
    lambda acumulado, precio: acumulado + precio,
    bebidas_caras
)

print(f"Total a pagar: ${total:.2f}")