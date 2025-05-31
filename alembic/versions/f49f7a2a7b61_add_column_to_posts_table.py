"""add column to posts table

Revision ID: f49f7a2a7b61
Revises: 4903fcdcee13
Create Date: 2024-12-14 15:22:28.601221

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f49f7a2a7b61'
down_revision = '4903fcdcee13'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
