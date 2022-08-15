"""add indexes

Revision ID: 146c8173a7b8
Revises: 42c12f1c5e7f
Create Date: 2022-08-15 06:37:27.838992

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '146c8173a7b8'
down_revision = '42c12f1c5e7f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_index('ix_league_code', 'leagues', ['code'])
    op.create_index('ix_team_name', 'teams', ['name'])
    op.create_index('ix_team_id', 'players', ['team_id'])


def downgrade() -> None:
    op.drop_index('ix_league_code', 'leagues')
    op.drop_index('ix_team_name', 'teams')
    op.drop_index('ix_team_id', 'player')
