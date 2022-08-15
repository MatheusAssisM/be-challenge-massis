"""add team_id column in players table

Revision ID: 7508966be218
Revises: c5dc7ab12043
Create Date: 2022-08-14 19:07:07.056745

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "7508966be218"
down_revision = "c5dc7ab12043"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("players", sa.Column("team_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "players_team_id_fkey", "players", "teams", ["team_id"], ["id"]
    )


def downgrade() -> None:
    op.drop_constraint("players_team_id_fkey", "players", type_="foreignkey")
    op.drop_column("players", "team_id")
