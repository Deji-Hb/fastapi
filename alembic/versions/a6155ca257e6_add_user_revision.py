"""add user revision

Revision ID: a6155ca257e6
Revises: f49f7a2a7b61
Create Date: 2024-12-14 15:35:08.400206

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a6155ca257e6"
down_revision = "f49f7a2a7b61"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
    "users",
    sa.Column("id", sa.Integer(), nullable=False),
    sa.Column("email", sa.String(), nullable=False),
    sa.Column("password", sa.String(), nullable=False),
    sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("now()"), nullable=False),
    sa.PrimaryKeyConstraint("id"),
    sa.UniqueConstraint("email")
    )
    pass


def downgrade():
    op.drop_table("users")
    pass
