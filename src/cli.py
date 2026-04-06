import argparse
import sys
from .tracker import add_subject, log_hours, get_report

def main():
    parser = argparse.ArgumentParser(description="StudyBudget - Gerencie suas horas de estudo.")
    subparsers = parser.add_subparsers(dest="command", help="Comandos disponíveis")

    # Comando: add
    parser_add = subparsers.add_parser("add", help="Adiciona uma nova matéria")
    parser_add.add_argument("name", type=str, help="Nome da matéria")

    # Comando: log
    parser_log = subparsers.add_parser("log", help="Registra horas de estudo para uma matéria")
    parser_log.add_argument("name", type=str, help="Nome da matéria")
    parser_log.add_argument("hours", type=float, help="Quantidade de horas (ex: 2.5)")

    # Comando: report
    subparsers.add_parser("report", help="Mostra o relatório de horas estudadas")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    if args.command == "add":
        try:
            add_subject(args.name)
            print(f"Sucesso: Matéria '{args.name}' adicionada!")
        except Exception as e:
            print(f"Erro: {e}", file=sys.stderr)
            sys.exit(1)

    elif args.command == "log":
        try:
            total = log_hours(args.name, args.hours)
            print(f"Sucesso: {args.hours} horas registradas em '{args.name}'. Total agora: {total}h.")
        except Exception as e:
            print(f"Erro: {e}", file=sys.stderr)
            sys.exit(1)

    elif args.command == "report":
        try:
            report = get_report()
            print("\n--- Relatório de Horas ---")
            if not report:
                print("Nenhuma matéria cadastrada ainda.")
            else:
                for subj, hours in report.items():
                    print(f"- {subj}: {hours} horas")
            print("--------------------------\n")
        except Exception as e:
             print(f"Erro ao gerar relatório: {e}", file=sys.stderr)
             sys.exit(1)

if __name__ == "__main__":
    main()
