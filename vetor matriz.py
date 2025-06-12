alunos = ["alice","bruno","clara"]

dias = ["seg", "ter", "qua","qui"]

reservas = [["Asusente" for _ in dias] for _ in alunos ]

print("Preemcha com 'S' para e 'X' para ausenca:")

for i, aluno in enumerate(alunos):
    print(f"\nALUNO: {aluno}")
    for j,dia in enumerate(dias):
    entrada = input(f"  {dias}: ")
    if entrda.upper() == 'S':
    reservas[i][j] = "presente"

print("\nTabela de reservas:")
print(f"{Aluna:<10} {' 'join ( [f'{d:<10}' for d in dias])}")
for i, aluno in enumerate(alunos):
     print(f"{aluno:<10} {' 'join([f'{res:<10}'for res in reservas [i]])}")