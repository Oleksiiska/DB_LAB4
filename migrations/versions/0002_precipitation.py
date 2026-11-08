"""Етап 2: опади в окрему таблицю precipitation"""
from alembic import op
import sqlalchemy as sa

revision = "0002"
down_revision = "0001"


def columns():
    return [
        sa.Column("precip_mm", sa.Float),
        sa.Column("precip_in", sa.Float),
        sa.Column("humidity", sa.Integer),
        sa.Column("cloud", sa.Integer),
    ]


def upgrade():
    op.create_table(
        "precipitation",
        sa.Column("weather_id", sa.Integer, sa.ForeignKey("weather.id"), primary_key=True),
        *columns(),
    )
    op.execute("""
        INSERT INTO precipitation (weather_id, precip_mm, precip_in, humidity, cloud)
        SELECT id, precip_mm, precip_in, humidity, cloud FROM weather
    """)
    for column in columns():
        op.drop_column("weather", column.name)


def downgrade():
    for column in columns():
        op.add_column("weather", column)
    op.execute("""
        UPDATE weather
        SET precip_mm = p.precip_mm, precip_in = p.precip_in, humidity = p.humidity, cloud = p.cloud
        FROM precipitation p WHERE p.weather_id = weather.id
    """)
    op.drop_table("precipitation")
