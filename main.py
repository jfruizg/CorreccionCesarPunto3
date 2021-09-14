from collections import Counter

mensajeEncriptado = "LS WLYYV KL ZHU YVXBL UV APLUL YHIV WVYXBL YHTVU YVKYPNBLG ZL SV OH JVYAHKV"
abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def remover_espacio(cadena):
    return cadena.replace(' ', '')

def lefraMasRepetida(mensajeEncriptado,num):
    matriz = []
    for i in range(0,len(mensajeEncriptado)):
        matriz.append(mensajeEncriptado[i])
    counter = Counter(remover_espacio(mensajeEncriptado))
    first, second,third ,*_, last = counter.most_common()
    resultdo = ""
    if num == 1:
        resultado = first
    elif num == 2:
        resultdo = second
    elif num == 3:
        resultdo = third
    matrizFinal = []
    for i in range(0,len(resultado)):
        matrizFinal.append(resultado[i])
    return matrizFinal[0]
def buscarPosicionAbecedario(letra,abecedario):
    posicion = 0
    for i in range(0,len(abecedario)):
        if(abecedario[i] == letra):
            posicion = i
    return posicion+1
def buscarPosicionLetraE():
    posicion = 0
    for i in range(0,len(abecedario)):
        if(abecedario[i] == "E"):
            posicion = i
    return posicion+1
def decifrarCesar(abc,listaEncriptada,desplazamiento):
    mensajeFinal = ""
    for i in range(0, len(listaEncriptada)):
        for j in range(0, len(abc)):
            if listaEncriptada[i] == abecedario[j]:
                mensajeFinal = mensajeFinal + abecedario[j - desplazamiento]
        if listaEncriptada[i] == " ":
            mensajeFinal = mensajeFinal + " "
    return mensajeFinal
def verificarDeslazamiento(desplazamiento,mensajeEncriptado):
    desplazamiento
    for i in mensajeEncriptado:
        posicionLetra = ord(i)
        pos1 = ord(i) - ord("A")
        desplazamiento2 = (pos1-desplazamiento)%26
    return desplazamiento2






desplazamiento = verificarDeslazamiento(desplazamiento,mensajeEncriptado)
print(lefraMasRepetida(mensajeEncriptado))
print(desplazamiento)
print(decifrarCesar(abecedario,mensajeEncriptado,desplazamiento))







