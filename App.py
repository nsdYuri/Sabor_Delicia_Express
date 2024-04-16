import os

print("𝓢𝓪𝓫𝓸𝓻 𝓓𝓮𝓵𝓲́𝓬𝓲𝓪 𝓔𝔁𝓹𝓻𝓮𝓼𝓼\n")

# Menu de opções 
print("1. Cadastrar Restaurante")
print("2. Listar Restaurante")
print("3. Ativar Restaurante")
print("4. Sair\n")

# Pegar a informação do usuário
opcao_escolhida = int(input("Escolha uma opção: "))
# opcao_escolhida = int(opcao_escolhida)
print(f"Opção escolhida: {opcao_escolhida}")

# Funções que iram exercer aquilo que o usuario escolher fazer 
def cadastra_restaurante():
    print("Cadastando restaurante...")

def lista_restaurante():
    print("Listando restaurante...")

def ativa_restaurante():
    print("Ativando restaurante...")

def sair():
    os.system('cls') # Windows
    #os.system('clear') Mackbook
    print("Saindo...\n")

# Condicional que executa a função que corresponde a opção escolhida pelo usuário
if opcao_escolhida == 1:
    cadastra_restaurante()
elif opcao_escolhida == 2:
    lista_restaurante()
elif opcao_escolhida == 3:
    ativa_restaurante()
elif opcao_escolhida == 4:
    sair()
else:
    print("Opção indisponivel.")