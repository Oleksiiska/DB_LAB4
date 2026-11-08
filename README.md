```bash
git checkout stage-1
alembic upgrade head
python cli.py import GlobalWeatherRepository.csv
python cli.py stats

git checkout stage-2
alembic upgrade head
python cli.py stats

git checkout stage-3
alembic upgrade head
python cli.py stats

git checkout stage-4
python cli.py show Hungary 2024-11-20

git checkout stage-5
alembic -x db=mysql upgrade head
python cli.py --db mysql import GlobalWeatherRepository.csv
python cli.py --db pg stats
python cli.py --db mysql stats
```
