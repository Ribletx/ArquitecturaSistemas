from flask import Flask, request, jsonify
import os

app = Flask(__name__)
LOG_FILE = 'log.txt'

def save_log(entry):
    # Guardar los logs como texto
    log_entry = f"[{entry.get('timestamp')}] {entry['event']}\n"
    with open(LOG_FILE, 'a') as f:  # Usamos 'a' para agregar al final del archivo
        f.write(log_entry)

@app.route('/log', methods=['POST'])
def log():
    entry = request.json
    save_log(entry)
    print(f"[{entry.get('timestamp')}] {entry['event']}")
    return jsonify({'message': 'Log registrado'}), 201

@app.route('/log', methods=['GET'])
def get_logs():
    if not os.path.exists(LOG_FILE):
        return jsonify([])  # Si no existe el archivo, retorna un array vacío
    
    logs = []
    with open(LOG_FILE, 'r') as f:
        logs = f.readlines()  # Lee todas las líneas del archivo txt
    
    # Convertir cada línea a un diccionario (si es necesario, dependiendo del formato)
    formatted_logs = []
    for line in logs:
        # Suponiendo que el formato de cada línea es: [timestamp] event
        timestamp, event = line.strip().split("] ", 1)
        timestamp = timestamp[1:]  # Quitar el corchete de apertura
        formatted_logs.append({"timestamp": timestamp, "event": event})
    
    return jsonify(formatted_logs)

@app.route('/logs', methods=['GET'])
def view_logs():
    # Simple verificación de "usuario administrador" (puedes personalizarlo)
    password = request.args.get('password')
    if password != 'admin':
        return "<h1>Acceso denegado</h1>", 403  # Error de acceso si la contraseña no es correcta
    
    # Si la contraseña es correcta, carga los logs
    if not os.path.exists(LOG_FILE):
        return jsonify([])
    with open(LOG_FILE, 'r') as f:
        logs = f.readlines()
    
    formatted_logs = []
    for line in logs:
        timestamp, event = line.strip().split("] ", 1)
        timestamp = timestamp[1:]  # Quitar el corchete de apertura
        formatted_logs.append({"timestamp": timestamp, "event": event})
    
    return jsonify(formatted_logs)


if __name__ == "__main__":
    app.run(port=5003)
