# StudyBudget 📚📈

O StudyBudget é uma ferramenta simples e eficiente de Linha de Comando (CLI) feita em Python. O objetivo principal do projeto é **resolver a dor real** de estudantes (universitários, concurseiros) que têm dificuldade na gestão e balanceamento das horas de estudo, acabando por negligenciar disciplinas críticas. 

Com o StudyBudget, você consegue rastrear de forma exata quantas horas dedicou a cada matéria, auxiliando no planejamento e sucesso acadêmico.

[![CI](https://github.com/SEU_USUARIO/StudyBudget/actions/workflows/ci.yml/badge.svg)](https://github.com/SEU_USUARIO/StudyBudget/actions/workflows/ci.yml)

## 🎯 Problema Real e Solução
**A Dor (Problema):** Estudantes possuem muitas disciplinas e conciliar o tempo dedicado a cada uma gera desorganização. Geralmente estuda-se apenas as matérias preferidas, deixando de lado as essenciais que definem a aprovação num concurso ou prova final, gerando deficiências na base educacional.
**A Solução:** Uma aplicação de terminal puramente voltada para registrar horas e emitir um relatório limpo e direto, ajudando no controle e criação de um hábito de estudos visualizável que mostre claramente quais matérias estão estagnadas.
**Público-alvo:** Estudantes de nível médio, universitários, concurseiros e vestibulandos.

## 🛠️ Tecnologias Utilizadas
- **Python 3.12+**
- **JSON** (para armazenamento leve em disco)
- **Pytest** (para testes automatizados)
- **Ruff** (para linting e qualidade estática)
- **GitHub Actions** (Pipelines de Integração Contínua - CI)

## 🚀 Instalação e Execução

### Pré-requisitos
- Ter o Python na máquina.
- Clonar este repositório.

### Como Usar passo-a-passo no Terminal

1. Entre na pasta do projeto:
   ```bash
   cd StudyBudget
   ```

2. Registre uma nova disciplina:
   ```bash
   python main.py add "Matematica"
   ```

3. Registre as horas de estudo na disciplina:
   ```bash
   python main.py log "Matematica" 2.5
   ```

4. Veja seu relatório geral:
   ```bash
   python main.py report
   ```

## 🧪 Testes Automatizados e Linting

O projeto contém testes automatizados desenhados para cobrir o "caminho feliz" e as exceções da lógica de negócio. Você pode rodar tudo localmente para verificar a qualidade da aplicação.

### Instruções para rodar os Testes
Instale as dependências nativas (`pytest` e `ruff`) e execute sua pipeline de teste:
```bash
pip install -r requirements.txt
pytest tests/
```

### Instruções para rodar o Linting
Garanta que seu código segue as melhores práticas estruturais lidas pelo Ruff (Linter ultrarrápido):
```bash
ruff check src/ tests/
```

## 📋 Sobre o Projeto (Versão 1.0.0)

- **Autor:** Matheus
- **Versão Atual:** 1.0.0
- **Link do Repositório (Público):** [https://github.com/matheus277353/StudyBudget](https://github.com/matheus277353/StudyBudget)
