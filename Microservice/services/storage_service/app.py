from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# Obtener la ruta del directorio actual del archivo
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TASKS_FILE = os.path.join(BASE_DIR, 'tasks.json')

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f)

@app.route('/tasks', methods=['POST'])
def add_task():
    tasks = load_tasks()
    new_task = request.json
    new_task['id'] = len(tasks) + 1
    new_task['completed'] = False
    tasks.append(new_task)
    save_tasks(tasks)
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
            return jsonify(task)
    return jsonify({'error': 'Tarea no encontrada'}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    return jsonify({'message': 'Tarea eliminada'}), 200

if __name__ == "__main__":
    app.run(port=5002)
