"""Етап 3.3: go_outside NOT NULL"""
from alembic import op

revision = "0005"
down_revision = "0004"


def upgrade():
    op.alter_column("precipitation", "go_outside", nullable=False)


def downgrade():
    op.alter_column("precipitation", "go_outside", nullable=True)
