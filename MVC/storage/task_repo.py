import json
import os
from models.task import Task

class TaskRepo:
    FILE_PATH = "tasks.json"

    def load_tasks(self):
        if not os.path.exists(self.FILE_PATH):
            return []

        try:
            with open(self.FILE_PATH, "r") as file:
                data = json.load(file)
                return [Task.from_dict(d) for d in data]
        except (json.JSONDecodeError, ValueError):
            # Si está vacío o corrupto, reinicia el archivo
            self.save_tasks([])
            return []

    def save_tasks(self, tareas):
        with open(self.FILE_PATH, "w") as file:
            json.dump([t.to_dict() for t in tareas], file, indent=4)
