"""

Programa Lista de la compra

Que desea comprar? ([Q] para salir) > Leche
Seguro que quiere añadir "Leche"? [S/N] > S
Leche añadido!

Que desea comprar? ([Q] para salir) > Pan
Seguro que quiere añadir "Pan"? [S/N] > N

Que desea comprar? ([Q] para salir) > Pan
Seguro que quiere añadir "Pan"? [S/N] > S
Pan añadido!

Que desea comprar? ([Q] para salir) > Pan
Pan ya está en la lista!

Que desea comprar? ([Q] para salir) > Q
La Lista de la compra es:
["Leche", "Pan"]

"""

lista = []

elemento = None

while elemento != "Q":
<<<<<<< HEAD
    elemento = input("¿Que desea comprar, sugiero que compres leche? ([Q] para salir)\n")
=======
    elemento = input("¿Que desea comprar, mozo del senioh? ([Q] para salir)\n")
>>>>>>> 620b906e622fe5f1f36bdb15ad0567e4c0df347a
    if elemento in lista:
        print("{} ya esta en la lista".format(elemento))
    else:
        if elemento == "Q":
            elemento = "Q"
        else:
            if input("¿Seguro que quiere añadir {}? [S/N]\n".format(elemento)) == "S":
                lista.append(elemento)
            else:
                elemento = None

print("La Lista de la compra es:")
print(lista)

