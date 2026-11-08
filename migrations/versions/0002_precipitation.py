"""Етап 2: опади в окрему таблицю precipitation"""
from alembic import op
import sqlalchemy as sa

revision = "0002"
down_revision = "0001"


def columns():
    return [
        sa.Column("precip_mm", sa.Double),
        sa.Column("precip_in", sa.Double),
        sa.Column("humidity", sa.Integer),
        sa.Column("cloud", sa.Integer),
    ]


def upgrade():
    op.create_table(
        "precipitation",
        sa.Column("weather_id", sa.Integer, sa.ForeignKey("weather.id"), primary_key=True),
        *columns(),
        mysql_charset="utf8mb4",
        mysql_collate="utf8mb4_bin",
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
        UPDATE weather SET
            precip_mm = (SELECT precip_mm FROM precipitation WHERE weather_id = weather.id),
            precip_in = (SELECT precip_in FROM precipitation WHERE weather_id = weather.id),
            humidity = (SELECT humidity FROM precipitation WHERE weather_id = weather.id),
            cloud = (SELECT cloud FROM precipitation WHERE weather_id = weather.id)
    """)
    op.drop_table("precipitation")
