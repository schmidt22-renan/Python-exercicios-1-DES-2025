# Isabela está desenvolvendo um aplicativo de corrida que calcula a velocidade média do usuário.
# O programa deve receber a distância percorrida e o tempo gasto, calcular a velocidade e indicar se foi 
# lenta (<5 km/h), moderada (5 a 10 km/h) ou rápida (>10 k

distamcia = float(imput("digite a distamcia"))
tempo = float(imput("digite o tempo "))
v_media= distamcia / tempo 
 
    if v_media < 5 :
    prit("lento")
elef v_media>=5  <=10
    print("moderado")
else :
print("ropeclo")