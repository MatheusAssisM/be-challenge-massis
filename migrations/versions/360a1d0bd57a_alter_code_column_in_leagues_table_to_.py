"""alter code column in leagues table to be unique

Revision ID: 360a1d0bd57a
Revises: c6fec9eea9f3
Create Date: 2022-08-12 19:45:23.598867

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "360a1d0bd57a"
down_revision = "c6fec9eea9f3"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_unique_constraint("unique_code", "leagues", ["code"])


def downgrade() -> None:
    op.drop_constraint("unique_code", "leagues", type_="unique")
