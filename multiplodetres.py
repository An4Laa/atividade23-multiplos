soma = 0
for numero in range(1, 501) :
    if numero % 3 == 0:
        print(numero)
        soma += numero

else :
    print(f"A soma dos números no intervalo de 1 à 500 é {soma}")