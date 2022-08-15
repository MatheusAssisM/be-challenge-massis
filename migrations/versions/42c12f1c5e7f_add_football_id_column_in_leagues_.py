"""add football_id column in leagues, players, teams, and coaches table

Revision ID: 42c12f1c5e7f
Revises: 122d47b1f002
Create Date: 2022-08-14 23:38:40.172565

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "42c12f1c5e7f"
down_revision = "122d47b1f002"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("leagues", sa.Column("football_id", sa.Integer()))
    op.add_column("teams", sa.Column("football_id", sa.Integer()))
    op.add_column("coaches", sa.Column("football_id", sa.Integer()))

    op.create_unique_constraint("uq_leagues_football_id", "leagues", ["football_id"])
    op.create_unique_constraint("uq_teams_football_id", "teams", ["football_id"])
    op.create_unique_constraint("uq_coaches_football_id", "coaches", ["football_id"])


def downgrade() -> None:
    op.drop_column("leagues", "football_id")
    op.drop_column("teams", "football_id")
    op.drop_column("coaches", "football_id")
