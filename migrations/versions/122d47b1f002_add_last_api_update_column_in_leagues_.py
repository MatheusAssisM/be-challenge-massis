"""add last_api_update column in leagues and teams table

Revision ID: 122d47b1f002
Revises: a5bb430189c1
Create Date: 2022-08-14 22:25:59.033609

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "122d47b1f002"
down_revision = "a5bb430189c1"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "leagues", sa.Column("last_api_update", sa.DateTime(), nullable=False)
    )
    op.add_column("teams", sa.Column("last_api_update", sa.DateTime(), nullable=False))


def downgrade() -> None:
    op.drop_column("leagues", "last_api_update")
    op.drop_column("teams", "last_api_update")
