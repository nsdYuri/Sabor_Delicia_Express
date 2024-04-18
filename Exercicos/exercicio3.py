# Crie uma lista para cada informação a seguir:

# Lista de números de 1 a 10:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Lista com quatro nomes:
nomes = ["Guilherme", "Sabrina", "Lucas", "Thais"]

# Lista com o ano que você nasceu e o ano atual
tempo_vida = [2004, 2024]

# Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
produtos = ["Televisão", "Celular", "Notebook", "Tablet", "PC"]
for item in produtos:
    print(item)
    
# Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
soma_impares = 0
for num in range(1, 11, 1):
    if num % 2 != 0:
        impar = num
        soma_impares += impar
print(soma_impares)
    
# Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
for dec in range(10, 0, -1):
    print(dec)
    
# Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
tabu = int(input("Digite um numero para saber sua tabuada: "))
print("Tabuada do ", tabu)
for res in range(1, 11, 1):
    print(tabu * res)
    
# Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. 
# Utilize um bloco try-except para lidar com possíveis exceções.
lista_numeros = [10, 20, 30, 40, 50, "a"]
soma = 0
try:
    for numero in lista_numeros:
        soma += numero
    print(f"Soma dos numeros: {soma}")
except Exception as e:
    print(f"Ocorrreu um erro {e}")

# Construa um código que calcule a média dos valores em uma lista. 
# Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
lista_media = [10, 10, 10]
soma_nmumeros = 0
try: 
    for valores in lista_media:
        soma_nmumeros += valores
    media = soma_nmumeros / len(lista_media)
    print(f"Média dos numeros: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possivel calculalr a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
     
    