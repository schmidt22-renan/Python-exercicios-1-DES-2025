# Renata quer solicitar um financiamento, mas precisa verificar se cumpre os critérios:

# Salário mensal acima de R$ 3.000,00
# A parcela não pode ser maior que 35% do sal


pagamento = float(input("Digite o pagamento recebido mensalmente: "))
parcela = float(input("Digite a parcela do pagamento que está destinada ao financeiro:"))

if pagamento > 3.000 or parcela < 35:
    print("O financiamento não pode ser efetuado.")
else:
    print("O financiamento pode ser efetuado.")
