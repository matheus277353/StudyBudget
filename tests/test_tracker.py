import os
import tempfile
import pytest
from unittest.mock import patch

from src.tracker import add_subject, log_hours, get_report

@pytest.fixture(autouse=True)
def mock_storage_file():
    # Cria arquivo temporario para o teste
    fd, temp_path = tempfile.mkstemp(suffix=".json")
    os.close(fd)
    
    # Força a importação a usar o temp_path
    with patch("src.storage.DATA_FILE", temp_path):
        yield temp_path
        
    os.remove(temp_path)

def test_add_subject_and_log_hours_successfully():
    """Testa o caminho feliz de cadastro e log de horas."""
    assert add_subject("Matematica") == True
    report = get_report()
    assert "Matematica" in report
    
    new_total = log_hours("Matematica", 2.5)
    assert new_total == 2.5
    assert get_report()["Matematica"] == 2.5

def test_prevent_negative_hours():
    """Testa a entrada inválida de horas (negativas)."""
    add_subject("Fisica")
    with pytest.raises(ValueError, match="Não é possível adicionar horas negativas."):
        log_hours("Fisica", -1.0)

def test_prevent_logging_hours_on_invalid_subject():
    """Testa o caso limite/erro ao adicionar horas em materia inexistente."""
    with pytest.raises(ValueError, match="A matéria 'Inexistente' não está cadastrada."):
        log_hours("Inexistente", 2.0)
