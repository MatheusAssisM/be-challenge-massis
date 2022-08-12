"""add team table

Revision ID: e107ebf7a5ff
Revises: 46504be7d9e3
Create Date: 2022-08-12 02:35:20.373929

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e107ebf7a5ff"
down_revision = "46504be7d9e3"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "teams",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("tla", sa.String(length=3), nullable=False),
        sa.Column("short_name", sa.String(length=30), nullable=False),
        sa.Column("area_name", sa.String(length=50), nullable=False),
        sa.Column("address", sa.String(length=255), nullable=False),
        sa.Column(
            "created_at", sa.DateTime, nullable=False, server_default=sa.text("now()")
        ),
    )


def downgrade() -> None:
    op.drop_table("team")
