distancia = float(input("por gentilesa, digite a distancia da nossa loja ate sua residemcia"))

if distancia <= 50:
    print("o valor de frete e R$5,00")
elif distancia <= 150:
    print("o valor do frete e R$15,00")

else:
print("o valor e R$25,00")