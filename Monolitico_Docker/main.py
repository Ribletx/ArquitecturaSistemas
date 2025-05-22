import json
import uuid
from datetime import datetime
import os

#Creamos el documento con las tareas
TASKS_FILE = 'tasks.json'

#Apretar enter para continuar
def pausar():
    input("\nPresiona Enter para continuar...")


def cargar_tareas():
    #Si no existe lo crea
    if not os.path.exists(TASKS_FILE):
        return []
    #Si esta lo abre
    with open(TASKS_FILE, 'r') as file:
        return json.load(file)

#CREAR TAREAS_______________
def guardar_tareas(tareas):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tareas, file, indent=4)

def agregar_tarea():
    print("\n=== Agregar nueva tarea ===")
    titulo = input("Título: ").strip()
    descripcion = input("Descripción: ").strip()

    nueva_tarea = {
        'id': str(uuid.uuid4()),
        'titulo': titulo,
        'descripcion': descripcion,
        'completada': False,
        'creada_en': datetime.now().isoformat()
    }

    tareas = cargar_tareas()
    tareas.append(nueva_tarea)
    guardar_tareas(tareas)
    print("✅ Tarea agregada exitosamente.\n")
    pausar()

#VISUALIZAR TAREAS_______________
def listar_tareas():
    print("\n=== Lista de tareas ===")
    tareas = cargar_tareas()

    if not tareas:
        print("No hay tareas registradas.\n")
        pausar()
        return

    for i, tarea in enumerate(tareas, start=1):
        estado = "✅ Completada" if tarea['completada'] else "⏳ Pendiente"
        print(f"{i}. {tarea['titulo']} - {estado}")
        print(f"   Descripción: {tarea['descripcion']}")
        print(f"   Fecha de creación: {tarea['creada_en']}")
        #print(f"   ID: {tarea['id']}\n")
    pausar()

#ESTADO COMPLETO O PENDIENTE_____________
def cambiar_estado_tarea():
    tareas = cargar_tareas()

    if not tareas:
        print("\nNo hay tareas para actualizar.\n")
        return

    print("\n=== Cambiar estado de una tarea ===")
    for i, tarea in enumerate(tareas, start=1):
        estado = "✅" if tarea['completada'] else "⏳"
        print(f"{i}. {tarea['titulo']} [{estado}]")

    try:
        seleccion = int(input("Selecciona el número de la tarea a cambiar: "))
        if seleccion < 1 or seleccion > len(tareas):
            print("❌ Número inválido.\n")
            return
    except ValueError:
        print("❌ Entrada no válida.\n")
        return

    tarea = tareas[seleccion - 1]
    tarea['completada'] = not tarea['completada']
    guardar_tareas(tareas)

    nuevo_estado = "completada" if tarea['completada'] else "pendiente"
    print(f"✅ Tarea '{tarea['titulo']}' marcada como {nuevo_estado}.\n")
    pausar()

#ELIMINAR TAREAS_____________________
def eliminar_tarea():
    tareas = cargar_tareas()

    if not tareas:
        print("\nNo hay tareas para eliminar.\n")
        return

    print("\n=== Eliminar una tarea ===")
    for i, tarea in enumerate(tareas, start=1):
        estado = "✅" if tarea['completada'] else "⏳"
        print(f"{i}. {tarea['titulo']} [{estado}]")

    try:
        seleccion = int(input("Selecciona el número de la tarea a eliminar: "))
        if seleccion < 1 or seleccion > len(tareas):
            print("❌ Número inválido.\n")
            return
    except ValueError:
        print("❌ Entrada no válida.\n")
        return

    tarea_eliminada = tareas.pop(seleccion - 1)
    guardar_tareas(tareas)
    print(f"🗑️ Tarea '{tarea_eliminada['titulo']}' eliminada exitosamente.\n")
    pausar()

#MENU DE DESPLIEGUE__________def menu():
def menu():
    while True:
        print("=== 📝 Todo App - Menú Principal ===")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Cambiar estado de tarea (completada/pendiente)")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("Selecciona una opción (1-5): ").strip()

        if opcion == '1':
            agregar_tarea()
        elif opcion == '2':
            listar_tareas()
        elif opcion == '3':
            cambiar_estado_tarea()
        elif opcion == '4':
            eliminar_tarea()
        elif opcion == '5':
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida. Intenta nuevamente.\n")

if __name__ == "__main__":
    menu()
