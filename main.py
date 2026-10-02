numeros = [1,2,3,4,5,6,7,8,9,10]

def slicing_string(list=[], num=0, pos= ""):
    if pos == "izq":
        return numeros[len(numeros) - num:] + numeros[:len(numeros) - num]
    elif pos == "der":
        return numeros[num: ] + numeros[0: num]

numero = int(input("Introduce cantidad de numeros: "))
posicion = input("Introduce hacia donde se moverá (izq o der): ")
print(slicing_string(numeros, numero, posicion))
