"""add coach table

Revision ID: a5bb430189c1
Revises: 7508966be218
Create Date: 2022-08-14 20:09:00.579714

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a5bb430189c1"
down_revision = "7508966be218"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "coaches",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("nationality", sa.String(length=50), nullable=False),
        sa.Column("date_of_birth", sa.Date()),
        sa.Column("team_id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(["team_id"], ["teams.id"]),
    )


def downgrade() -> None:
    op.drop_table("coaches")
