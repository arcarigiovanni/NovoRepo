'''Dado o seguinte array de produtos:

[“Celular”, “Notebook”, “Televisão”, “Tablet”, “Câmera”, “Smartwatch”]

a) Implemente um algoritmo em python de ordenação por seleção (Selection Sort) para ordenar os produtos em ordem alfabética.
b) Apresente a quantidade de comparações e trocas realizadas durante o processo de ordenação.'''

def selection_sort(arr):
    comparisons = 0
    swaps = 0
    print(arr[1])
    
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
        
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1
    
    return comparisons, swaps

produtos = ["Celular", "Notebook", "Abajour","Televisão", "Tablet", "Câmera", "Smartwatch"]

comparisons, swaps = selection_sort(produtos)

print("Produtos ordenados:", produtos)
print("Quantidade de comparações:", comparisons)
print("Quantidade de trocas:", swaps)


