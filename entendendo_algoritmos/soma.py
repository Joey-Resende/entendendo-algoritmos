def soma(lista):
    if lista == []:
        return 0
    return lista[0] + soma(lista[1:])


resultado = soma([1, 2, 3, 4])
print(resultado)

