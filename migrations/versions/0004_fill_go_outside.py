"""Етап 3.2: заповнення go_outside"""
from alembic import op

revision = "0004"
down_revision = "0003"


def upgrade():
    op.execute("UPDATE precipitation SET go_outside = precip_mm < 2.5")


def downgrade():
    op.execute("UPDATE precipitation SET go_outside = NULL")
