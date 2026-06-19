def ver_menu(menu):
    menu_formateado = [
        f"{nombre.capitalize()}: ${precio:.2f}"
        for nombre, precio in menu.items()
    ]
    return menu_formateado


menu = {
    "americano": 25.50,
    "café de olla": 22.00,
    "capuchino": 35.75,
    "coca": 40.00,
    "agua": 18.50
}


menu_formateado = ver_menu(menu)

for bebida in menu_formateado:
    print(bebida)
 