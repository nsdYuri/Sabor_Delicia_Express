import os
os.system('cls')

# Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
num = int(input("Digite um número: "))
if num % 2 == 0:
    print(f"{num} é par")
else:
    print(f"{num} é impar")


#  Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições: Criança: 0 a 12 anos, Adolescente: 13 a 18 anos, Adulto: acima de 18 anos.
idade = int(input("Digite sua idade: "))
if 0 <= idade <= 12:
    print("Criança")
elif 13 <= idade <= 18:
    print("Adolescente")
elif 18 < idade <= 110:
    print ("Adulto")
else:
    print("Idade invalida")


# Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.
user = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")
if user == "paciencia" and senha == "12345":
    print("Acesso liberado")
else:
    print("Usuário ou senha invalidos.")


# Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:
x = float(input("Digite um valor coordenada x"))
y = float(input("Digite um valor coordenada y"))

if x > 0 and y > 0:
    print("Primeiro Quadrante")
elif x < 0 and y > 0:
    print("Segundo Quadrante")
elif x < 0 and y < 0:
    print("Terceiro Quadrante")
elif x > 0 and y < 0:
    print("Qaurto Quadrante")
else:
    print("O ponto está localizado no ponto ou na origem")



