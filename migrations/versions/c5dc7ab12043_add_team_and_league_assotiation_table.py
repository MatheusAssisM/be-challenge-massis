"""add team and league association table

Revision ID: c5dc7ab12043
Revises: 20e5baafda5e
Create Date: 2022-08-14 15:20:10.646895

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c5dc7ab12043"
down_revision = "20e5baafda5e"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "leagues_teams_association",
        sa.Column("league_id", sa.Integer(), nullable=False),
        sa.Column("team_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["league_id"], ["leagues.id"]),
        sa.ForeignKeyConstraint(["team_id"], ["teams.id"]),
    )


def downgrade() -> None:
    op.drop_table("leagues_teams_association")
