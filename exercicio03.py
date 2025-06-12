# Rafael trabalha com armazenamento de grãos e precisa garantir que a umidade do ar no local não ultrapasse 70%.
# Escreva um programa que receba o valor da umidade atual e exiba um alerta se estiver acima do limite.

umidade = int(input("digite a umidade local"))

if umidade < 100:
    print("atemperatura esta boa")
else:
    print("alerta a temperatura ultrapassou o limite.")
