lista_tarefas = []
tarefas_concluidas = []

# INTERFACE DO PROGRAMA
def menu():
    print("==== Sistema de Gerenciamento de Tarefas ====")
    print("1. Adicionar uma tarefa")
    print("2. Listar todas as tarefas")
    print("3. Editar uma tarefa")
    print("4. Remover uma tarefa")
    print("5. Concluir tarefa")
    print("6. Mostrar tarefas concluídas")
    print("7. Sair do programa")

# FUNCAO ADICIONAR TAREFA
def adicionar_tarefa():
    try:
        tarefa = str(input("Digite a tarefa que deseja adicionar: ")).upper()
        lista_tarefas.append(tarefa)
        print('-'*30)
        print()
        print("     TAREFA ADICIONADA")
        print()
        print('-'*30)
    except Exception as e:
        print(f"Erro ao adicionar a tarefa: {str(e)}")

# FUNCAO LISTAR TAREFAS
def listar_tarefas():
    print("\nLISTA DE TAREFAS A FAZER:")
    for i, tarefa in enumerate(lista_tarefas, 1):
        print(f"{i}. {tarefa}")
    print()

# FUNCAO EDITAR TAREFA
def atualizar_tarefa():
    try:
        while True:
            nova_tarefa = input("Digite a nova tarefa: ").upper()
            listar_tarefas()
            tarefa_trocada = int(input("Qual número da tarefa que deseja substituir? "))
            if tarefa_trocada >= 1 and tarefa_trocada <= len(lista_tarefas):
                lista_tarefas[tarefa_trocada - 1] = nova_tarefa
                print('-'*30)
                print()
                print("     Lista atualizada com sucesso!!")
                print()
                print('-'*30)
                listar_tarefas()
                break  
            else:
                print('-'*30)
                print()
                print("     Número de tarefa inválido.")
                print()
                print('-'*30)
    except Exception as e:
        print(f"Erro ao atualizar a tarefa: {str(e)}")

# FUNCAO REMOVER TAREFA
def remover_tarefa():
    try:
        while True:
            listar_tarefas()
            tarefa_remover = int(input("Qual número da tarefa que deseja remover? "))
            if tarefa_remover >= 1 and tarefa_remover <= len(lista_tarefas):
                lista_tarefas.pop(tarefa_remover - 1)
                print('-'*30)
                print()
                print("     Tarefa removida com sucesso!")
                print()
                print('-'*30)
                listar_tarefas()
                break  
            else:
                print('-'*30)
                print()
                print("     Número de tarefa inválido.")
                print()
                print('-'*30)
    except Exception as e:
        print(f"Erro ao remover a tarefa: {str(e)}")

# FUNCAO CONCLUIR TAREFA
def concluir_tarefa():
    try:
        while True:
            listar_tarefas()
            concluida = int(input("Qual número da tarefa que deseja marcar como concluída? "))
            if concluida >= 1 and concluida <= len(lista_tarefas):
                tarefa_concluida = lista_tarefas[concluida - 1]
                lista_tarefas.pop(concluida - 1)
                tarefas_concluidas.append(tarefa_concluida)
                print(f"Tarefa n°{concluida} concluída!")
                print()
                break  
            else:
                print("Número de tarefa inválido.")
                print()
    except Exception as e:
        print(f"Erro ao concluir a tarefa: {str(e)}")

# FUNCAO MOSTRAR TAREFAS CONCLUIDAS
def mostrar_tarefas_concluidas():
    print("\nLISTA DE TAREFAS CONCLUIDAS:")
    if len(tarefas_concluidas) == 0:
        print("Nenhuma tarefa concluída.")
    else:
        for i, tarefa in enumerate(tarefas_concluidas, 1):
            print(f"{i}. {tarefa}")
        print()

# FUNCIONAMENTO PROGRAMA
def main():
    try:
        while True:
            menu()
            opcao = int(input("\nEscolha uma opção: "))
            if opcao == 1:
                adicionar_tarefa()
            elif opcao == 2:
                listar_tarefas()
            elif opcao == 3:
                atualizar_tarefa()
            elif opcao == 4:
                remover_tarefa()
            elif opcao == 5:
                concluir_tarefa()
            elif opcao == 6:
                mostrar_tarefas_concluidas()
            elif opcao == 7:
                print("PROGRAMA ENCERRADO")
                from time import sleep
                sleep(2)
                break
            else:
                print("Escolha inválida, digite novamente")
    except Exception as e:
        print(f"Ocorreu um erro no programa: {str(e)}")
main()
