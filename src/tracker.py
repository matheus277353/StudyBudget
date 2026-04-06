from .storage import load_data, save_data

def add_subject(name: str) -> bool:
    """Adiciona uma nova matéria à base de dados."""
    name = name.strip()
    if not name:
        raise ValueError("O nome da matéria não pode ser vazio.")
        
    data = load_data()
    if name in data["subjects"]:
        raise ValueError(f"A matéria '{name}' já está cadastrada.")
        
    data["subjects"][name] = 0.0
    save_data(data)
    return True

def log_hours(name: str, hours: float) -> float:
    """Registra uma quantidade de horas estudadas em uma matéria."""
    name = name.strip()
    if hours < 0:
        raise ValueError("Não é possível adicionar horas negativas.")
        
    data = load_data()
    if name not in data["subjects"]:
        raise ValueError(f"A matéria '{name}' não está cadastrada.")
        
    data["subjects"][name] += hours
    save_data(data)
    return data["subjects"][name]

def get_report() -> dict:
    """Retorna todas as matérias e suas respecitvas horas registradas."""
    data = load_data()
    return data["subjects"]
