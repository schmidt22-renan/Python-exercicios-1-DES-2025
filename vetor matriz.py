alunos = ["alice", "bruno ,"carla"]

dias = ["seg", "ter", "qua","qui"]

reservas = [["Asusente" for _ in dias] for _ in alunos ]

 print("Preemcha com 'S' para e 'X' para ausenca: )

for i, aluno in enumerate(alunos):
    print(f"\nALUNO: {aluno}")
    for j,dia in enumerate(dias):
    emtrada = input(f"  {dias}: ")
    if entrda.upper() == 'S':
    reservas[i][j] = "presente"

print("\nTabela de Reservas:)"
print(f"{Aluna:<10} {' 'join( [f{d:<10