import random

def select_sort(V):
    n = len(V)
    for i in range(n - 1):
        menor = i
        for j in range(i + 1, n):
            if V[j] < V[menor]:
                menor = j
        # Troca de valores
        V[menor], V[i] = V[i], V[menor]

#Geração de uma lista aleatória de números
tamanho = int(input("Digite o tamanho do vetor: "))
vetor = [random.randint(0, 99) for _ in range(tamanho)]

#Chama a função select_sort para ordenar o vetor
select_sort(vetor)

#Imprime o vetor ordenado
for i in range(tamanho):
    print(f"Vetor na posição {i}: {vetor[i]}")
