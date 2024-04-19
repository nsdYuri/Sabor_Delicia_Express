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
    linha = '-' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()
    
def cadastra_restaurante():
    """ Função responsavel por cadastras um novo restaurante ao sistema 
    Inputs:
    - Nome do Restaurante
    - Categoria
    
    Output:
    - Adiciona um novo restaurante ao dicionario """
    exibir_subtitulo("Cadastrando novo restaurante...\n")
    nome_restaurante = input("Informe o nome do restaurante: ")
    categoria_restaurante = input(f"Informe a categoria do restaurante - {nome_restaurante}: ")
    dados_restaurante = {"Nome":nome_restaurante, 
                         "Categoria":categoria_restaurante, 
                         "Ativo":False}
    restaurantes.append(dados_restaurante)
    print(f"Restarurante: {nome_restaurante} foi cadastrado com sucesso! <( ͡ᵔ ͜ʖ ͡ᵔ)>")
    retornar_ao_menu()
    
def lista_restaurante():
    """ Função responsavel por exibir a lista de restaurantes presntes no sistema """
    exibir_subtitulo("Lista de restaurantes:")
    
    print(f"{"RESTAURANTE:".ljust(23)} | {"CATEGORIA:".ljust(20)} | STATUS:")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["Nome"]
        categoria_restaurante = restaurante["Categoria"]
        ativo = "Ativado" if restaurante["Ativo"] else "Desativado" # Estrutura de Ternário: Condicional em uma linha apenas
        print(f" - {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo.ljust(20)}")
        
    retornar_ao_menu()

def ativa_ou_desativa_restaurante():
    exibir_subtitulo("Alterando status do restaurante:")
    nome_restaurante = input("Informe do nome do restaurante que deseja alterar o status: ")
    restaurante_escolhido = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante["Nome"]:
            restaurante_escolhido = True
            restaurante["Ativo"] = not restaurante["Ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso" if restaurante["Ativo"] else f"O restaurante {nome_restaurante} foi desativado"
            print(mensagem)
    if not restaurante_escolhido:
        print("Restaurante não encontrado")
    # if not restaurante_escolhido: # Como a variavel restaurante_escolhido é false, o not ira tranforma-la em True e executar o if
    #     print("Restaurante não encontrado.")
    retornar_ao_menu()

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
            ativa_ou_desativa_restaurante()
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