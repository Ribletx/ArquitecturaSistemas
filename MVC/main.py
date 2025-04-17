from controllers.task_controller import TaskController
import os
import shutil

def eliminar_cache():
    """Recorre todos los directorios y elimina las carpetas __pycache__."""
    for root, dirs, files in os.walk("."):
        if "__pycache__" in dirs:
            pycache_path = os.path.join(root, "__pycache__")
            print(f"Eliminando cache en: {pycache_path}")  # Para verificar qué directorios se están eliminando
            shutil.rmtree(pycache_path)
            print(f"Cache eliminado en: {pycache_path}")
        else:
            print(f"No se encontró __pycache__ en: {root}")  # Verificamos los directorios escaneados

def main():
    controller = TaskController()

    while True:
        print("\n=== Menú ===")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Eliminar tarea")
        print("4. Marcar tarea como completada")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ").strip()

        if opcion == '1':
            titulo = input("Título de la tarea: ").strip()
            descripcion = input("Descripción de la tarea: ").strip()
            controller.add_task(titulo, descripcion)
        elif opcion == '2':
            controller.list_tasks()
        elif opcion == '3':
            try:
                task_index = int(input("Índice de la tarea a eliminar: ")) - 1
                controller.remove_task(task_index)
            except ValueError:
                print("Por favor ingresa un número válido.")
        elif opcion == '4':
            try:
                task_index = int(input("Índice de la tarea a marcar como completada: ")) - 1
                controller.mark_task_done(task_index)
            except ValueError:
                print("Por favor ingresa un número válido.")
        elif opcion == '5':
            print("Adiós!")

            # Eliminar cache de todos los directorios
            eliminar_cache()

            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()