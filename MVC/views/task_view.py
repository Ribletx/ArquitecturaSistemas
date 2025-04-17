class TaskView:
    def show_message(self, message):
        print(message)

    def show_tasks(self, tareas):
        if not tareas:
            print("No hay tareas registradas.\n")
        else:
            for i, tarea in enumerate(tareas, start=1):
                estado = "✅ Completada" if tarea.completada else "⏳ Pendiente"
                print(f"{i}. {tarea.titulo} - {estado}")
                print(f"   Descripción: {tarea.descripcion}")
                print(f"   Fecha de creación: {tarea.creada_en}\n")
