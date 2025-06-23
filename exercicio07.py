media01 = int(input("Digite o valor da media da avaliaçao"))
media02 = int(input("Digite o valor da media da avaliaçao"))
media03 = int(input("Digite o valor da media da avaliaçao"))
valor = media01 or media02 or media03
if valor>= 7 :
    print("Voce foi aprovado!")
elif valor >= 5 :
    print("Voce esta esta em treinamento")
elif valor < 7 :
    print("Voce esta em treinamento.")
else:
    print("voce foi aprovado!")

