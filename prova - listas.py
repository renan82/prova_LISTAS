lista_par = []
lista_impar = []
for i in range(10):
    n = int(input("Digite um número para adicionar na lista: "))
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)
print(f"Os números PARES da lista são: {lista_par}, contendo ao total {len(lista_par)} números!")
print(f"Os números ÍMPARES da lista são: {lista_impar} contendo ao total {len(lista_impar)} números!")
soma = 0
for numero in lista_par:
    soma = numero + soma
print(f"A soma dos números PARES é {soma}")
soma1 = 0
for numero in lista_impar:
    soma1 = numero + soma1
print(f"A soma dos números ÍMPARES é {soma1}")
tupla_impar = tuple(lista_impar)
print(f"Os números ímpares na tupla é {tupla_impar}")
print(" ---- FIM ----")
    



