from flask import Flask, request, jsonify
import os
import json
import requests
from datetime import datetime

app = Flask(__name__)

TASKS_FILE = 'tasks.json'
LOG_URL = 'http://localhost:5003/log'

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f)

def log_event(event):
    try:
        timestamp = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        requests.post(LOG_URL, json={'event': event, 'timestamp': timestamp})
    except requests.exceptions.RequestException:
        print(f"⚠️ No se pudo registrar el log: {event}")

@app.route('/tasks', methods=['POST'])
def add_task():
    tasks = load_tasks()
    new_task = request.json
    new_task['id'] = len(tasks) + 1
    new_task['completed'] = False
    tasks.append(new_task)
    save_tasks(tasks)
    log_event(f"Tarea creada: {new_task['title']}")
    return jsonify(new_task), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = load_tasks()
    return jsonify(tasks)

@app.route('/tasks/<int:task_id>/complete', methods=['PUT'])
def complete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            save_tasks(tasks)
            log_event(f"Tarea completada: {task['title']}")
            return jsonify(task)
    return jsonify({'error': 'Tarea no encontrada'}), 404

@app.route('/tasks/complete_all', methods=['PUT'])
def complete_all_tasks():
    tasks = load_tasks()
    for task in tasks:
        task['completed'] = True
    save_tasks(tasks)
    log_event("Todas las tareas fueron marcadas como completadas")
    return jsonify({'message': 'Todas las tareas completadas'}), 200

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks = load_tasks()
    deleted_title = None
    new_tasks = []
    for task in tasks:
        if task['id'] == task_id:
            deleted_title = task['title']
        else:
            new_tasks.append(task)
    save_tasks(new_tasks)
    if deleted_title:
        log_event(f"Tarea eliminada: {deleted_title}")
    return jsonify({'message': 'Tarea eliminada'}), 200

@app.route('/tasks', methods=['DELETE'])
def delete_all_tasks():
    save_tasks([])
    log_event("Todas las tareas fueron eliminadas")
    return jsonify({'message': 'Todas las tareas eliminadas'}), 200

if __name__ == "__main__":
    app.run(port=5001)
