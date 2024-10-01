'''
Crie um programa que cadastre uma lista de tarefas do dia. Ao final, o programa deve exibir a lista de tarefas. Obs.: Não Ordenar as lista.
'''
tarefas = []

# loop
while True:
    # Tratamendo de exceção
    try:
        # insere nova tarefa
        nova_tarefa = input("Informe a nova tarefa a ser executada ou 'Enter' para exibir a lista: ")

        # verifica se possui valor ou não
        if nova_tarefa:
            # insere nova tarefa na lista
            tarefas.append(nova_tarefa)
            print(f"Nova tarefa cadastrada com sucesso!")
            continue
        else:
            break
    except Exception as e:
        print(f"Não foi possível cadastrar nova tarefa. {e}.")

# exibe a lista
for nova_tarefa in tarefas:
    print(nova_tarefa)