"""add competition table

Revision ID: 46504be7d9e3
Revises: 
Create Date: 2022-08-12 01:43:30.737016

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "46504be7d9e3"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "competition",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("code", sa.String(length=10), nullable=False),
        sa.Column("area_name", sa.String(length=50), nullable=False),
        sa.Column(
            "created_at", sa.DateTime, nullable=False, server_default=sa.text("now()")
        ),
    )


def downgrade() -> None:
    op.drop_table("competition")
