"""add player table

Revision ID: c6fec9eea9f3
Revises: e107ebf7a5ff
Create Date: 2022-08-12 02:38:38.116015

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c6fec9eea9f3"
down_revision = "e107ebf7a5ff"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "player",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("position", sa.String(length=10), nullable=False),
        sa.Column("nationality", sa.String(length=50), nullable=False),
        sa.Column("date_of_birth", sa.Date(), nullable=False),
        sa.Column(
            "created_at", sa.DateTime, nullable=False, server_default=sa.text("now()")
        ),
    )


def downgrade() -> None:
    op.drop_table("player")    
