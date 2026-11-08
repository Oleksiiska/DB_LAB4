"""Етап 3.3: go_outside NOT NULL"""
from alembic import op
import sqlalchemy as sa

revision = "0005"
down_revision = "0004"


def upgrade():
    op.alter_column("precipitation", "go_outside", existing_type=sa.Boolean, nullable=False)


def downgrade():
    op.alter_column("precipitation", "go_outside", existing_type=sa.Boolean, nullable=True)
