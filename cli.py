import argparse

import services

parser = argparse.ArgumentParser(prog="cli.py")
commands = parser.add_subparsers(dest="command", required=True)
commands.add_parser("import").add_argument("csv")
commands.add_parser("stats")
args = parser.parse_args()

if args.command == "import":
    print("Імпортовано рядків:", services.import_csv(args.csv))
elif args.command == "stats":
    for name, value in services.stats().items():
        print(f"{name}: {value}")
