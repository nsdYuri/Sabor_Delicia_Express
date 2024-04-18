import os
os.system('cls') # Comando para limpar o terminal toda vez que rodarmos o programa

# Criando uma lista vazia dos restaurantes que serão cadastrados
dados_restaurante = []

# Função que exibe o nome do sistema
def exibe_nome_programa():
    print("𝓢𝓪𝓫𝓸𝓻 𝓓𝓮𝓵𝓲́𝓬𝓲𝓪 𝓔𝔁𝓹𝓻𝓮𝓼𝓼\n")

# Função que exibe o menu de opções
def exibe_menu():
    # Menu de opções 
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurante")
    print("3. Ativar Restaurante")
    print("4. Sair\n")

# Funções que iram exercer aquilo que o usuario escolher fazer 
def cadastra_restaurante():
    os.system('cls')
    print("Cadastrando novo restaurante...\n")
    nome_restaurante = input("Informe o nome do restaurante: ")
    dados_restaurante.append(nome_restaurante)
    print(f"Restarurante: {nome_restaurante} cadastrado com sucesso! \( ͡ᵔ ͜ʖ ͡ᵔ)/")

def lista_restaurante():
    print("Listando restaurante...")

def ativa_restaurante():
    print("Ativando restaurante...")

def sair():
    os.system('cls') # Windows
    #os.system('clear') Mackbook
    print("Saindo...\n")

def opcao_invalida():
    print("Opção invalida!\n")
    input("Digite a tecla Enter para voltar ao menu principal...")
    os.system('cls')
    main()

def escolhe_opcao():
    # Pegar a informação do usuário
    opcao_escolhida = int(input("Escolha uma opção: "))
    # opcao_escolhida = int(opcao_escolhida)
    print(f"Opção escolhida: {opcao_escolhida}")

# tramaento de excessões que ira tentar relizar uma tarefa, caso ela seja direcionada para um erro, o código tenta executar outra função.
    try:
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
            opcao_invalida()
    except:
        opcao_invalida()

    # Alternativa para o if, elif, else = match (funciona como um switch case)
    
    # match opcao_escolhida:
    #     case 1:
    #         cadastra_restaurante()
    #     case 2:
    #         lista_restaurante()
    #     case 3:
    #         ativa_restaurante()
    #     case 4:
    #         sair()
    #     case _:
    #         print("Opção indisponivel")
    

# Criando função main, que ira exclusivamente rodar aquilo que está no principal
def main():
    exibe_nome_programa()
    exibe_menu()
    escolhe_opcao()

if __name__ == '__main__':
    main()