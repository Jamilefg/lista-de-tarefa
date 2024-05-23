class GerenciadorDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, nome):
        self.tarefas.append({"nome": nome, "completa": False})

    def visualizar_tarefas(self):
        if not self.tarefas:
            print("Não há tarefas na lista.")
        else:
            for index, tarefa in enumerate(self.tarefas, start=1):
                status = "Completa" if tarefa["completa"] else "Incompleta"
                print(f"{index}. {tarefa['nome']} - {status}")

    def atualizar_tarefa(self, indice, novo_nome):
        if 1 <= indice <= len(self.tarefas):
            self.tarefas[indice - 1]["nome"] = novo_nome
            print("Nome da tarefa atualizado com sucesso.")
        else:
            print("Índice inválido.")

    def marcar_como_completa(self, indice):
        if 1 <= indice <= len(self.tarefas):
            self.tarefas[indice - 1]["completa"] = True
            print("Tarefa marcada como completa.")
        else:
            print("Índice inválido.")

    def deletar_tarefas_completas(self):
        self.tarefas = [tarefa for tarefa in self.tarefas if not tarefa["completa"]]
        print("Tarefas completas deletadas com sucesso.")


def main():
    gerenciador = GerenciadorDeTarefas()

    while True:
        print("\n=== Gerenciador de Tarefas ===")
        print("1. Adicionar Tarefa")
        print("2. Visualizar Tarefas")
        print("3. Atualizar Tarefa")
        print("4. Marcar como Completa")
        print("5. Deletar Tarefas Completas")
        print("6. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Digite o nome da tarefa: ")
            gerenciador.adicionar_tarefa(nome)
        elif escolha == "2":
            gerenciador.visualizar_tarefas()
        elif escolha == "3":
            indice = int(input("Digite o índice da tarefa a ser atualizada: "))
            novo_nome = input("Digite o novo nome da tarefa: ")
            gerenciador.atualizar_tarefa(indice, novo_nome)
        elif escolha == "4":
            indice = int(input("Digite o índice da tarefa a ser marcada como completa: "))
            gerenciador.marcar_como_completa(indice)
        elif escolha == "5":
            gerenciador.deletar_tarefas_completas()
        elif escolha == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()