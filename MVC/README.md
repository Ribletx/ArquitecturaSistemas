![Logo](mvc/assets/UAI.png)
# Arquitectura de Sistemas: TICS317

---
¡Bienvenidos al repositorio de Arquitectura!. Acá haremos algunos ejercicios complementarios a las clases para profundizar los aprendizajes




# ¿Que necesitamos?
| **Categoría**                  | **Biblioteca**                                                                                          | **Descripción**                                                        |
|-------------------------------|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| **1. Manejo de archivos**     | [![json](https://img.shields.io/badge/json-estándar-yellow)](https://docs.python.org/3/library/json.html) | Lectura y escritura de archivos `.json` para almacenar las tareas.     |
| **2. Sistema de archivos**    | [![os](https://img.shields.io/badge/os-estándar-yellow)](https://docs.python.org/3/library/os.html)       | Interacción con el sistema de archivos (opcional, si lo usaste).       |
| **3. Tipado estático**        | [![typing](https://img.shields.io/badge/typing-estándar-yellow)](https://docs.python.org/3/library/typing.html) | Anotaciones de tipo para mayor claridad y validación estática.         |



### El proyecto se desarrolla en:

* Enviroment de Python [![versions](https://img.shields.io/badge/python-3.13-white)](https://www.python.org/downloads/)

* Entorno de Desarrollo Integrado (IDE) [![versions](https://img.shields.io/badge/PyCharm-2024.3.4-white)](https://www.jetbrains.com/help/pycharm/installation-guide.html)


## 🎓 Caso de Estudio: Desarrollo de una Aplicación de Tareas para Taller Universitario

**Contexto:**  
En un curso de *Arquitectura de Software*, se propone desarrollar una aplicación que gestione tareas personales desde la línea de comandos. El objetivo es que los estudiantes comprendan cómo la elección de una arquitectura afecta el diseño, la mantenibilidad y la evolución del software.

### Escenario A – Enfoque Monolítico no modular
Un estudiante comienza desarrollando la aplicación en un único archivo `main.py`. Esto le permite centrarse rápidamente en la lógica básica y aprender el flujo general de entrada, proceso y salida.  
**Ventajas:** facilidad de codificación rápida, ideal para prototipos o pruebas de concepto.  
**Desventajas:** el código empieza a crecer desordenadamente, dificultando la lectura, pruebas y futuras ampliaciones (como soporte para usuarios múltiples).

### Escenario B – Enfoque MVC
En una segunda fase, el estudiante migra la misma lógica a una estructura basada en MVC, separando:
- `models/` → contiene la lógica de la tarea y la representación de la misma (datos).
- `views/` → impresión en consola y entrada de usuario.
- `controllers/` → Coordina la interacción entre la vista y los componentes del modelo.
- `storage/` → persistencia en archivo JSON.

Esto permite escalar el proyecto fácilmente. Por ejemplo, si más adelante se quiere implementar una interfaz gráfica o una API, solo se necesita modificar la **vista**, sin tocar la lógica de negocio ni el modelo de datos.

---

## Objetivo del repositorio:

Desarrollar una aplicación de consola (CLI) que permita a los usuarios gestionar una lista de tareas u operaciones: agregar, listar, marcar como completadas y eliminar tareas.


> "In many cases, the operations are called CRUD operations, for Create, Read, Update, and Delete."  
> Elmasri, R., & Navathe, S. B. (2016). Fundamentals of database systems seventh edition.


Es un ejemplo clásico, pero muy potente para aprender MVC, ya que tiene:
- Un modelo de datos claro (una tarea).
- Lógica de negocio sencilla (crear, actualizar, eliminar tareas).
- Interacción con el usuario (por ahora vía consola, pero fácilmente extensible).
- Persistencia (se puede empezar con archivos de texto (JSON), y más adelante mostrar cómo adaptar a SQLite o similar).

## Descripción detallada del proyecto:

Descripción del Caso: Todo App (Aplicación de Lista de Tareas)

**Contexto:**

Vamos a desarrollar una aplicación de consola que permitirá gestionar una lista de tareas. Los usuarios podrán agregar, eliminar, listar y marcar tareas como completadas. Este es un caso típico que ilustra cómo aplicar el patrón de arquitectura MVC en Python.

**Requerimientos del Caso:**
1. **Modelo:** La aplicación debe tener una representación de las tareas a través de un modelo, que contenga atributos como el título, la descripción y un indicador de si la tarea está completa o no.
2. **Vista:** Debemos tener una vista que muestre al usuario las opciones disponibles, como agregar una tarea, listar tareas, completar tareas y eliminar tareas.
3. **Controlador:** Debe recibir las solicitudes del usuario, interactuar con el modelo y actualizar la vista.
4. **Persistencia:** Las tareas deben ser almacenadas en un archivo (para simplificar, utilizaremos almacenamiento en un archivo de texto o en formato JSON).
5. **Interfaz de usuario:** La aplicación se ejecutará en la consola (CLI), proporcionando un menú interactivo.


## 📁 Estructura del Repositorio 
```
todo_app/
│
├── controllers/            
│   ├── __init__.py
│   └── task_controller.py
│
├── models/                 
│   ├── __init__.py
│   └── task.py
│
├── views/                  
│   ├── __init__.py
│   └── task_view.py
│
├── storage/                
│   ├── __init__.py
│   └── task_repo.py
│   └── task.json
│
├── assets/                 
│   └── logo.png
│
├── main.py                 
├── requirements.txt        
└── README.md   
```

## Notas adicionales de la aplicación Lista de Tareas

Esta aplicación es un ejemplo educativo diseñado para mostrar cómo una misma funcionalidad —una lista de tareas gestionada por consola— puede desarrollarse siguiendo dos enfoques arquitectónicos distintos:

- 🧱 **Enfoque Monolítico no modular**
- 🧩 **Enfoque MVC (Modelo-Vista-Controlador)**

---

### Descripción de la arquitectura

- **`main.py`**: Punto de entrada que instancia el controlador y lanza la app.
- **`controllers/task_controller.py`**: interactúa con el repositorio (`TaskRepo`), con la vista (`TaskView`) y con el modelo.
- **`models/task.py`**: Define el modelo de datos `Task` y contiene la lógica de la tarea.
- **`views/task_view.py`**: Encargada de mostrar información al usuario por consola.
- **`storage/task_repo.py`**: Encargado de leer/escribir las tareas desde/hacia el archivo JSON (`task.json`).


```

main.py
   |
   v
TaskController
 ├──> TaskView    (input/output)
 ├──> Task        (modelo de datos)
 └──> TaskRepo    (carga/almacenamiento)
         |
         ├──> TaskRepoPersistent (persistence/archivo)
         └──> TaskRepoMemory     (en memoria)
             
             
             
                   +----------------+
                   |    main.py     |
                   +----------------+
                          |
                          v
              +----------------------------+
              |      TaskController        |
              +----------------------------+
              | +show_tasks()              |
              | +add_task()                |
              | +complete_task()           |
              | +delete_task()             |
              +----------------------------+
                 |            |            |
                 v            v            v
          +------------+  +------------+  +----------------+
          | TaskRepo   |--|     Task   |  |   TaskView     |
          +------------+  +------------+  +----------------+
          | load()     |  | validate() |  |  show_menu()   |
          | save()     |  | mark_done  |  |  show_tasks()  |
          +------------+  +------------+  +----------------+
             |
             +-----------------+             
             |                 |              
    +--------------------+    +----------------+
    | TaskRepoPersistent |    | TaskRepoMemory |
    +--------------------+    +----------------+
    | load()             |    | load()         |
    | save()             |    | save()         |
    +--------------------+    +----------------+
```
---

| **Módulo**   | **Objeto**                   | **Métodos**           | **Descripción**                                                                 |
|--------------|------------------------------|-----------------------|---------------------------------------------------------------------------------|
| **Models**   | **Task**                      | `__init__`            | Inicializa una tarea con un título y un estado de completado (por defecto, False). |
|              |                              | `mark_completed`      | Marca la tarea como completada (`completed = True`).                           |
|              |                              | `to_dict`             | Convierte la tarea en un diccionario con las claves `title` y `completed`.     |
|              |                              | `from_dict`           | Crea una instancia de `Task` a partir de un diccionario.                       |
| **Storage**  | **TaskRepoInMemory**          | `__init__`            | Inicializa el repositorio con una lista vacía de tareas (en memoria).          |
|              |                              | `load_tasks`          | Simula la carga de tareas desde una fuente persistente (en este caso, en memoria). |
|              |                              | `save_tasks`          | Simula el guardado de tareas en una fuente persistente (en memoria).            |
|              |                              | `add_task`            | Agrega una nueva tarea al repositorio en memoria.                              |
|              |                              | `get_all_tasks`       | Retorna todas las tareas almacenadas en el repositorio en memoria.             |
|              |                              | `delete_task`         | Elimina una tarea por su índice del repositorio en memoria.                     |
| **Storage**  | **TaskRepoPersistent**        | `load_tasks`          | Carga las tareas desde un archivo JSON o retorna una lista vacía si no hay tareas. |
|              |                              | `save_tasks`          | Guarda las tareas en un archivo JSON.                                           |
| **View**     | **TaskView**                  | `show_tasks`          | Muestra la lista de tareas con su estado (completadas o no).                   |
|              |                              | `get_task_input`      | Solicita al usuario el título de una nueva tarea.                              |
|              |                              | `get_task_number`     | Solicita al usuario el número de una tarea (con manejo de errores si el número no es válido). |
|              |                              | `show_message`        | Muestra un mensaje al usuario.                                                 |
| **Controller**| **TaskController**            | `__init__`            | Inicializa el controlador con el repositorio y la vista.                       |
|              |                              | `show_tasks`          | Muestra todas las tareas disponibles usando la vista.                          |
|              |                              | `add_task`            | Solicita al usuario una nueva tarea y la guarda en el repositorio.             |
|              |                              | `complete_task`       | Marca una tarea como completada según el número ingresado por el usuario.     |
|              |                              | `delete_task`         | Elimina una tarea según el número ingresado por el usuario.                    |
|              |                              | `_get_task_by_number` | Devuelve la tarea correspondiente al número ingresado por el usuario. Si el número es inválido, retorna None. |



## Comparación entre Enfoque Monolítico No Modular y Enfoque Monolítico Modular (MVC)

| Característica                        | Enfoque Monolítico No Modular (`main.py` consolidado)             | Enfoque Monolítico Modular - MVC (`todo_app/`)                                                 |
|--------------------------------------|--------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| **Organización del código**          | Todo el código está en un solo archivo (`main.py`)                | Código separado por responsabilidades: `models/`, `views/`, `controllers/`, `storage/`         |
| **Escalabilidad**                    | Poco escalable; difícil de mantener con nuevas funcionalidades     | Escalable; permite agregar funcionalidades sin romper lo existente                             |
| **Responsabilidad única**            | Varias responsabilidades mezcladas en un solo archivo              | Cada módulo tiene una responsabilidad específica (modelo, vista, etc.)                         |
| **Reutilización de código**          | Baja reutilización; lógica embebida en flujo principal             | Alta reutilización; los modelos y vistas pueden usarse en otros controladores                  |
| **Persistencia de datos**            | Lectura y escritura al JSON dentro de `main.py`                    | Persistencia separada en `storage/task_repo.py`                                                |
| **Facilidad para hacer pruebas**     | Difícil testeo por alto acoplamiento                               | Fácil testeo unitario por módulos independientes                                               |
| **Curva de aprendizaje**             | Baja; ideal para prototipos o scripts simples                      | Media; adecuada para aplicaciones más estructuradas                                            |
| **Separación de lógica y presentación** | Mezcladas en el mismo archivo                                  | Claramente separadas; la vista maneja la presentación, el modelo la lógica interna de la tarea |
| **Mantenibilidad**                   | Bajo mantenimiento a largo plazo                                   | Alto mantenimiento y fácil identificación de errores                                           |

### 💡 Nota:

Ambos enfoques son **monolíticos** porque se ejecutan como una única unidad, pero el enfoque con arquitectura MVC sigue principios de modularidad, lo cual facilita el mantenimiento, la escalabilidad y el testing. Esta es una buena práctica especialmente cuando el proyecto comienza a crecer.

---


## Consideraciones adicionales

Acá hacemos una breve lectura para rescatar algunos puntos tratados en clase

## ¿Qué es el patrón de diseño **Modelo-Vista-Controlador (MVC)**?

El patrón **Modelo-Vista-Controlador (MVC)** es una arquitectura de software que se utiliza para estructurar aplicaciones, separando la lógica de la aplicación en tres componentes principales: **Modelo**, **Vista** y **Controlador**. Esta separación permite un desarrollo más modular, fácil mantenimiento y escalabilidad. 

## Componentes de MVC

1. **Modelo (Model)**:
   - Representa los datos.
   - Es responsable de acceder a la base de datos, almacenar datos, realizar cálculos y gestionar el estado de la aplicación.
   - **Ejemplo**: En una aplicación de tareas, el modelo sería la estructura de datos de una tarea, con atributos como título, descripción y estado de completado.

2. **Vista (View)**:
   - Es la interfaz de usuario (UI) de la aplicación.
   - Se encarga de mostrar los datos proporcionados por el modelo, pero no interactúa directamente con los datos.
   - **Ejemplo**: En la aplicación de tareas, la vista se encargaría de mostrar las tareas al usuario en la pantalla.

3. **Controlador (Controller)**:
   - Actúa como intermediario entre el modelo y la vista.
   - Escucha las entradas del usuario (como clics o entradas de texto) y actualiza el modelo o la vista en consecuencia.
   - **Ejemplo**: En la aplicación de tareas, el controlador podría recibir el comando del usuario para agregar una nueva tarea y luego actualizar tanto el modelo (añadiendo la tarea a la lista) como la vista (mostrando la tarea recién agregada).

## ¿Por qué usar MVC?

- **Modularidad**: Cada componente tiene una responsabilidad clara y separada, lo que hace que el código sea más fácil de mantener y extender.
- **Reutilización**: Los modelos y vistas pueden reutilizarse en diferentes controladores, y viceversa.
- **Mantenibilidad**: Las modificaciones en una parte de la aplicación (como la lógica de negocio o la interfaz de usuario) pueden hacerse sin afectar otras partes.

## Ejemplo simple de MVC

Supongamos que tienes una aplicación para gestionar tareas:

1. **Modelo (Task)**: Define los atributos de la tarea, como título y estado de completado.
2. **Vista (TaskView)**: Muestra una lista de tareas en la consola o en una interfaz gráfica.
3. **Controlador (TaskController)**: Gestiona las acciones del usuario (por ejemplo, agregar o eliminar tareas), y actualiza el modelo y la vista en consecuencia.

---

# Recursos complementarios
- https://plantuml.com/es/sequence-diagram
- 
---

---
<center>TICS 317 - Arquitectura de Sistemas</center>


