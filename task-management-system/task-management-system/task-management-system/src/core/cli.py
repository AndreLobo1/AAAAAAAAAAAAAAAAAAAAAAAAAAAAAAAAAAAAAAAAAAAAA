# src/core/cli.py

from utils.utils import clear_screen, input_with_prompt

class CLI:
    def __init__(self, app):
        self.app = app

    def menu(self):
        while True:
            clear_screen()
            print("📋 Menu Principal:")
            print("1. Criar nova tarefa")
            print("2. Listar todas as tarefas")
            print("3. Editar tarefa")
            print("4. Sair")

            choice = input_with_prompt("Escolha uma opção: ", "Digite um número entre 1 e 4")

            if choice == '1':
                self.create_new_task()
            elif choice == '2':
                self.list_all_tasks()
            elif choice == '3':
                self.edit_task()
            elif choice == '4':
                print("👋 Até logo!")
                break
            else:
                print("❌ Opção inválida.")

    def create_new_task(self):
        print("\n📝 Criação de Nova Tarefa")
        print("Tipos de tarefas disponíveis:")
        print("1. Tarefa Simples")
        print("2. Tarefa com Prazo")
        print("3. Tarefa Recorrente")
        print("4. Subtarefa")

        type_choice = input_with_prompt("Selecione o tipo de tarefa: ", "Digite um número entre 1 e 4")

        title = input_with_prompt("Título da tarefa: ")
        description = input_with_prompt("Descrição da tarefa: ")
        assignee = input_with_prompt("Responsável pela tarefa: ")
        status = input_with_prompt("Status (Pendente/Em Andamento/Concluída): ")
        priority = input_with_prompt("Prioridade (Alta/Média/Baixa): ")

        # Mapeia tipos de tarefas
        task_types = {
            '1': 'simple',
            '2': 'deadline',
            '3': 'recurring',
            '4': 'subtask'
        }

        task_type = task_types.get(type_choice, 'simple')

        if task_type == 'deadline':
            deadline = input_with_prompt("Data do prazo (ex: 2025-05-10): ")
            self.app.create_task(task_type, title, description, assignee, status, priority, deadline=deadline)
        elif task_type == 'recurring':
            frequency = input_with_prompt("Frequência (diária/semanal/mensal): ")
            self.app.create_task(task_type, title, description, assignee, status, priority, frequency=frequency)
        elif task_type == 'subtask':
            parent_id = input_with_prompt("ID da tarefa pai: ")
            self.app.create_task(task_type, title, description, assignee, status, priority, parent_id=parent_id)
        else:
            self.app.create_task(task_type, title, description, assignee, status, priority)

        print("✅ Tarefa criada com sucesso!")

    def list_all_tasks(self):
        self.app.list_tasks()
        input("\nPressione Enter para voltar ao menu...")

    def edit_task(self):
        self.app.list_tasks()
        index = input_with_prompt("Selecione o número da tarefa que deseja editar: ", "Digite um número válido")

        try:
            index = int(index) - 1
            task = self.app.get_task_by_index(index)
            if task:
                new_title = input_with_prompt("Novo título: ", task.title)
                new_description = input_with_prompt("Nova descrição: ", task.description)
                new_assignee = input_with_prompt("Novo responsável: ", task.assignee)
                new_status = input_with_prompt("Novo status: ", task.status)
                new_priority = input_with_prompt("Nova prioridade: ", task.priority)

                task.edit(new_title, new_description, new_assignee, new_status, new_priority)
                self.app.notify_observers(f"Tarefa '{task.title}' foi atualizada.")
                print("✅ Tarefa atualizada com sucesso!")
            else:
                print("❌ Tarefa não encontrada.")
        except ValueError:
            print("❌ Entrada inválida.")
        input("\nPressione Enter para voltar ao menu...")