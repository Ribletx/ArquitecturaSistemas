from datetime import datetime

class Task:
    def __init__(self, titulo, descripcion, completada=False, creada_en=None):
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = completada
        self.creada_en = creada_en if creada_en else datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def mark_done(self):
        self.completada = True

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "completada": self.completada,
            "creada_en": self.creada_en
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            titulo=data.get("titulo", ""),
            descripcion=data.get("descripcion", ""),
            completada=data.get("completada", False),
            creada_en=data.get("creada_en")
        )
