# Bianca está programando o controle de acesso a uma plataforma que só funciona entre 9h e 21h.
# O programa deve receber a hora atual (formato 24h) e informar se o acesso é permitido.
hora_atual = int(input("Digite o horario que voce esta acessando a plataforma"))

if 9 <= hora_atual <= 21:
    print("A plataforma esta funcionando perfeitamente.")
else:
    print("A plataforma esta fora do horario de funcionamento.") 

