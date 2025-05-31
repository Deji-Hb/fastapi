"""create posts table

Revision ID: 4903fcdcee13
Revises:
Create Date: 2024-12-14 15:05:06.596408

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "4903fcdcee13"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False),
    )
    pass


def downgrade():
    op.drop_table("posts")
    pass
