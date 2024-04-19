# Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
dados_pessoais = {"Nome":"Augusto", "Idade":28, "Cidade":"Campinas"}

# Utilizando o dicionário criado no item 1:

# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa)
dados_pessoais.update({"Idade":50})
print(dados_pessoais)

# Adicione um campo de profissão para essa pessoa
profissao = {"Profissão":"Engenheiro de dados"}
dados_pessoais.update(profissao)
print(dados_pessoais)

# Remova um item do dicionário.
dados_pessoais.pop("Cidade")
del dados_pessoais["Profissão"]
print(dados_pessoais)

# criar um dicionário que apresente os números de 1 a 5 e seus respectivos quadrados
numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)


# Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
dados = {"Matricula":"552262", "Usuario":"Luana", "Cargo":"Gerente"}
if dados["Matricula"] == "550202":
    print("Iniicando sessão")
else:
    print("Matricula ivalida")
    
# Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)