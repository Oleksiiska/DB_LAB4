import argparse
from datetime import date

import services

parser = argparse.ArgumentParser(prog="cli.py")
parser.add_argument("--db", choices=["pg", "mysql"], default="pg")
commands = parser.add_subparsers(dest="command", required=True)
commands.add_parser("import").add_argument("csv")
commands.add_parser("stats")
show = commands.add_parser("show")
show.add_argument("country")
show.add_argument("date", type=date.fromisoformat)
args = parser.parse_args()

if args.command == "import":
    print("Імпортовано рядків:", services.import_csv(args.csv, args.db))
elif args.command == "stats":
    for name, value in services.stats(args.db).items():
        print(f"{name}: {value}")
elif args.command == "show":
    records = services.find(args.country, args.date, args.db)
    for record in records:
        print()
        for name, value in vars(record).items():
            print(f"{name}: {getattr(value, 'value', value)}")
    print("Знайдено спостережень:", len(records))
