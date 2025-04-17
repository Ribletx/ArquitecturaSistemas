from storage.task_repo import TaskRepo
from views.task_view import TaskView
from models.task import Task

class TaskController:
    def __init__(self):
        self.task_repo = TaskRepo()
        self.task_view = TaskView()

    def add_task(self, titulo, descripcion):
        nueva_tarea = Task(titulo, descripcion)
        tareas = self.task_repo.load_tasks()
        tareas.append(nueva_tarea)
        self.task_repo.save_tasks(tareas)
        self.task_view.show_message(f"Tarea '{titulo}' agregada exitosamente.")

    def remove_task(self, task_index):
        tareas = self.task_repo.load_tasks()
        if 0 <= task_index < len(tareas):
            tarea_eliminada = tareas.pop(task_index)
            self.task_repo.save_tasks(tareas)
            self.task_view.show_message(f"Tarea '{tarea_eliminada.titulo}' eliminada exitosamente.")
        else:
            self.task_view.show_message("Índice de tarea inválido.")

    def list_tasks(self):
        tareas = self.task_repo.load_tasks()
        self.task_view.show_tasks(tareas)

    def mark_task_done(self, task_index):
        tareas = self.task_repo.load_tasks()
        if 0 <= task_index < len(tareas):
            tarea = tareas[task_index]
            tarea.mark_done()
            self.task_repo.save_tasks(tareas)
            self.task_view.show_message(f"Tarea '{tarea.titulo}' marcada como completada.")
        else:
            self.task_view.show_message("Índice de tarea inválido.")
