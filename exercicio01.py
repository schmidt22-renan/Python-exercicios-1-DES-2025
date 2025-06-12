# Gabriel está acompanhando o desempenho de dois cursos online que lançou: Python Básico e JavaScript Essencial.
# Ele quer saber qual curso teve mais avaliações no último mês.

# Crie um programa que receba o número de avaliações de cada curso e exiba qual teve mais.
# Caso as quantidades sejam iguais, exiba uma mensagem dizendo que houve empate.

cuso01 =int(input("digite aquantidade de acessos do curso01"))
cuso02 =int(input("digite aquantidade de acessos do curso02"))

if cuso01 > cuso02 :
    print("curso01 tem mais acessos ")
elif curso02 > curso01 :
    print("cuso02 tem mais acessos")
else:
    print("ambos os cursos tem a mesma quantidade de acessos")