import logging

from alembic import context
from sqlalchemy import create_engine

from data_access import URLS, Base

logging.basicConfig(format="%(message)s")
logging.getLogger("alembic").setLevel(logging.INFO)

db = context.get_x_argument(as_dictionary=True).get("db", "pg")
with create_engine(URLS[db]).connect() as connection:
    context.configure(connection=connection, target_metadata=Base.metadata, transaction_per_migration=True)
    with context.begin_transaction():
        context.run_migrations()
