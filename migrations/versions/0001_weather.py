"""Етап 1: таблиця weather"""
from alembic import op
import sqlalchemy as sa

revision = "0001"
down_revision = None

DIRECTIONS = "N NNE NE ENE E ESE SE SSE S SSW SW WSW W WNW NW NNW".split()


def upgrade():
    op.create_table(
        "weather",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("country", sa.String(100)),
        sa.Column("location_name", sa.String(100)),
        sa.Column("last_updated", sa.DateTime),
        sa.Column("latitude", sa.Double),
        sa.Column("longitude", sa.Double),
        sa.Column("wind_kph", sa.Double),
        sa.Column("wind_degree", sa.Integer),
        sa.Column("wind_direction", sa.Enum(*DIRECTIONS, name="winddirection")),
        sa.Column("sunrise", sa.Time),
        sa.Column("precip_mm", sa.Double),
        sa.Column("precip_in", sa.Double),
        sa.Column("humidity", sa.Integer),
        sa.Column("cloud", sa.Integer),
        mysql_charset="utf8mb4",
        mysql_collate="utf8mb4_bin",
    )


def downgrade():
    op.drop_table("weather")
    sa.Enum(name="winddirection").drop(op.get_bind(), checkfirst=True)
