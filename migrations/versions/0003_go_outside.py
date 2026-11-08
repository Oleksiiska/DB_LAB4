"""Етап 3.1: колонка go_outside, поки без значень"""
from alembic import op
import sqlalchemy as sa

revision = "0003"
down_revision = "0002"


def upgrade():
    op.add_column("precipitation", sa.Column("go_outside", sa.Boolean))


def downgrade():
    op.drop_column("precipitation", "go_outside")
