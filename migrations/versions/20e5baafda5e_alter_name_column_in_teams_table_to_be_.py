"""alter name column in teams table to be unique

Revision ID: 20e5baafda5e
Revises: 360a1d0bd57a
Create Date: 2022-08-13 00:38:39.309341

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "20e5baafda5e"
down_revision = "360a1d0bd57a"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_unique_constraint("name_unique", "teams", ["name"])


def downgrade() -> None:
    op.drop_constraint("name_unique", "teams", type_="unique")
