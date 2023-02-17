""" 4. Una empresa tiene 500 almacenes. Cada almacén debe
reportar el nombre y 5 registros c/u, contiene el tipo de articulo
y el número de unidades vendidas de ese artículo.

Haga un programa en Python para determinar cuál fue el
almacén que mas vendió, cual fue el articulo más vendido de
ese almacén y cual el más vendido en general.
 """
cant_almacenes = 2
articulos = {}
cant_articulos_vendidos_total = 0
nombre_almacen = ""
articulo_mas_vendido = 0
articulo_mas_vendido_almacen = ""

for i in range(cant_almacenes):
    name = input(f"Digite el nombre del almacen {i+1}: ")
    sum = 0
    for b in range(2):
        articulo = input(f"Ingrese el tipo de artículo vendido en el almacén {name}: ")
        unidades = int(input(f"Ingrese el número de unidades vendidas de {articulo}: "))
        sum = sum + unidades
        articulos[articulo] = articulos.get(articulo, 0) + unidades
    articulo_vendido = max(articulos, key=articulos.get)
    print(f"\nEl artículo más vendido en el almacen {name} fue {articulo_vendido} con un total de {articulos[articulo_vendido]} unidades vendidas.\n")

    if(sum >= cant_articulos_vendidos_total):
        nombre_almacen = name
    
    if(articulos[articulo_vendido] >= articulo_mas_vendido):
        articulo_mas_vendido = articulos[articulo_vendido]
        articulo_mas_vendido_almacen = articulo_vendido

print(f"el almacen que mas vedio fue {nombre_almacen}")
print(f"el articulo mas vendido en general fue {articulo_mas_vendido_almacen} con una cantidad de {articulo_mas_vendido}")

