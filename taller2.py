""" 3. En pocos días comienza la vuelta a España y la federación
colombiana de ciclismo, como incentivo ha determinado pagar
un valor adicional. El programa pedirá por teclado el sueldo
básico por kilometro recorrido, el número de kilómetros
recorridos durante toda la vuelta, numero de kilómetros
recorridos con la camiseta de líder.
Calcular el valor a pagar total, si se sabe que si recorre en la
bici más de 1800 kilómetros con la camiseta de líder, esos
kilómetros se consideran especiales y tendrán un recargo de
25%.
El total de kilómetros por recorrer durante toda la vuelta serán
3.277 kilómetros,el ganador de la vuelta a España recibirá 700
millones de pesos.
 """

valor_kilometro = int(input("Digite el salario basico por KILOMETRO recorrido "))
kilometros_recorrido = int(input("Digite el TOTAL de kilometros recorridos durente toda la vuelta españa "))
decision = input("Tuvo la camiseta de lider?(si/no) ")

valor_kilometro_lider = 0
valor_total_kilometros = 0
total = 0


if(decision == "si"):
    kilometros_lider = int(input(f"De esos {kilometros_recorrido}km cuantos fueron con la camiseta de lider ")) 
    if(kilometros_lider > 1800):
        kilometros_lider = kilometros_lider - 1800
        recargo = ((valor_kilometro * 25) / 100) + valor_kilometro 
        valor_kilometro_lider = kilometros_lider * recargo
        valor_total_kilometros = (kilometros_recorrido * valor_kilometro)
        total = valor_total_kilometros + valor_kilometro_lider
        print(f"-felicitaciones se le pagara un valor de ${valor_total_kilometros} por los {kilometros_recorrido}km recorrido en la vuelta españa")
        print(f"-Aparte se le pagara un valor de ${valor_kilometro_lider} por superar los 1800km con la camiseta de lider")
        print(f"-Para un total de ${total}")

else:
    valor_total_kilometros = (kilometros_recorrido * valor_kilometro)
    print(f"-felicitaciones se le pagara un valor de ${valor_total_kilometros} por los {kilometros_recorrido}km recorrido en la vuelta españa")







