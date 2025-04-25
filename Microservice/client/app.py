from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)
TASK_URL = "http://localhost:5001"
LOG_URL = "http://localhost:5003"

def registrar_log(evento):
    try:
        requests.post(f"{LOG_URL}/log", json={"event": evento})  # Cambié de /logs a /log
    except requests.exceptions.RequestException:
        pass

@app.route('/')
def index():
    try:
        tasks_response = requests.get(f"{TASK_URL}/tasks")
        tasks_response.raise_for_status()
        tasks = tasks_response.json()
    except requests.exceptions.RequestException as e:
        return f"<h1>Error al conectar con los servicios: {e}</h1>"

    return render_template("index.html", tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    try:
        requests.post(f"{TASK_URL}/tasks", json={"title": title})
        registrar_log(f"Se agregó la tarea: {title}")
    except requests.exceptions.RequestException:
        pass
    return redirect('/')

@app.route('/complete/<int:task_id>')
def complete(task_id):
    try:
        response = requests.put(f"{TASK_URL}/tasks/{task_id}/complete")
        if response.status_code == 200:
            task = response.json()
            registrar_log(f"Se completó la tarea: {task['title']}")
    except requests.exceptions.RequestException:
        pass
    return redirect('/')

@app.route('/complete_all')
def complete_all():
    try:
        tasks = requests.get(f"{TASK_URL}/tasks").json()
        for task in tasks:
            if not task['completed']:
                requests.put(f"{TASK_URL}/tasks/{task['id']}/complete")
                registrar_log(f"Se completó la tarea: {task['title']}")
    except requests.exceptions.RequestException:
        pass
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete(task_id):
    try:
        response = requests.get(f"{TASK_URL}/tasks").json()
        title = next((t['title'] for t in response if t['id'] == task_id), f"ID {task_id}")
        requests.delete(f"{TASK_URL}/tasks/{task_id}")
        registrar_log(f"Se eliminó la tarea: {title}")
    except requests.exceptions.RequestException:
        pass
    return redirect('/')

@app.route('/delete_all')
def delete_all():
    try:
        tasks = requests.get(f"{TASK_URL}/tasks").json()
        for task in tasks:
            requests.delete(f"{TASK_URL}/tasks/{task['id']}")
            registrar_log(f"Se eliminó la tarea: {task['title']}")
    except requests.exceptions.RequestException:
        pass
    return redirect('/')

if __name__ == "__main__":
    app.run(port=5000)
