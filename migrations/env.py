import logging

from alembic import context
from sqlalchemy import create_engine

from data_access import URL, Base

logging.basicConfig(format="%(message)s")
logging.getLogger("alembic").setLevel(logging.INFO)

with create_engine(URL).connect() as connection:
    context.configure(connection=connection, target_metadata=Base.metadata, transaction_per_migration=True)
    with context.begin_transaction():
        context.run_migrations()
