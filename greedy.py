
pesoObjeto = [3, 4, 5, 2, 1, 3]
beneficioObjeto = [4, 5, 5, 3, 2, 4]
capacidadMochila = 17

def valorOptimo(solucion):
    pesoTotalObjetos = sum(pesoObjeto[i] for i in range(len(solucion)) if solucion[i])
    if pesoTotalObjetos > capacidadMochila:
        return -float("inf")
    valorTotalOptimo = sum(beneficioObjeto[i] for i in range(len(solucion)) if solucion[i])
    return valorTotalOptimo


def busquedaInformada():
    capacidadMochilaRestante = capacidadMochila
    solucion = [0] * len(pesoObjeto)
    mejorItem = 0
    while mejorItem != -1:
        mejorValorActual = -float("inf")
        mejorItem = -1
        for i in range(len(pesoObjeto)):
            if solucion[i] == 0 and beneficioObjeto[i]/pesoObjeto[i] > mejorValorActual and pesoObjeto[i] <= capacidadMochilaRestante:
                    mejorValorActual = beneficioObjeto[i]/pesoObjeto[i]
                    mejorItem = i
        if mejorItem == -1:
            break
        solucion[mejorItem] = 1
        capacidadMochilaRestante -= pesoObjeto[mejorItem]
    return solucion

# Ejemplo de uso
solucion = busquedaInformada()
print("Solución encontrada:")
print(solucion)
print("Valor total de los elementos seleccionados:", valorOptimo(solucion))
