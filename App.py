import os
os.system('cls') # Comando para limpar o terminal toda vez que rodarmos o programa
#os.system('clear') Mackbook

# Criando uma lista vazia dos restaurantes que serão cadastrados
restaurantes = [{"Nome":"Dhaigo", "Categoria":"Japonesa", "Ativo":True},
               {"Nome":"Piemonte", "Categoria":"Italiana", "Ativo":False},
               {"Nome":"Habibbs", "Categoria":"Árabe", "Ativo":True}]

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

def retornar_ao_menu():
    input("\nDigite a tecla Enter para voltar ao menu principal...")
    os.system('cls')
    main()
    
def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()
    
def cadastra_restaurante():
    exibir_subtitulo("Cadastrando novo restaurante...\n")
    nome_restaurante = input("Informe o nome do restaurante: ")
    categoria_restaurante = input(f"Informe a categoria do restaurante - {nome_restaurante}: ")
    dados_restaurante = {"Nome":nome_restaurante, 
                         "Categoria":categoria_restaurante, 
                         "Ativo":False}
    restaurantes.append(dados_restaurante)
    print(f"Restarurante: {nome_restaurante} foi cadastrado com sucesso! \( ͡ᵔ ͜ʖ ͡ᵔ)/")
    retornar_ao_menu()
    
def lista_restaurante():
    exibir_subtitulo("Lista de restaurantes:")
    
    for restaurante in restaurantes:
        nome_restaurante = restaurante["Nome"]
        categoria_restaurante = restaurante["Categoria"]
        ativo = restaurante["Ativo"]
        print(f" - {nome_restaurante} | {categoria_restaurante} | {ativo}")
        
    retornar_ao_menu()

def ativa_restaurante():
    exibir_subtitulo("Ativando restaurante...")

def sair():
    exibir_subtitulo("Encerrando...\n")

def opcao_invalida():
    print("Opção invalida!\n")
    retornar_ao_menu()
    

def escolhe_opcao():
    # Pegar a informação do usuário
    opcao_escolhida = input("Escolha uma opção: ")
    # opcao_escolhida = int(opcao_escolhida)
    print(f"Opção escolhida: {opcao_escolhida}")
    
    # tramaento de excessões que ira tentar relizar uma tarefa, caso ela seja direcionada para um erro, o código tenta executar outra função.
    try:
        if opcao_escolhida == "1":
            cadastra_restaurante()
        elif opcao_escolhida == "2":
            lista_restaurante()
        elif opcao_escolhida == "3":
            ativa_restaurante()
        elif opcao_escolhida == "4":
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