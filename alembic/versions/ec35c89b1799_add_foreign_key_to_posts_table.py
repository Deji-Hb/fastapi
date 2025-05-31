"""add foreign key to posts table

Revision ID: ec35c89b1799
Revises: a6155ca257e6
Create Date: 2024-12-14 17:21:15.632477

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec35c89b1799'
down_revision = 'a6155ca257e6'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "post_users_fkey", 
        source_table="posts", 
        referent_table="users", 
        local_cols=["owner_id"], 
        remote_cols=["id"],
        ondelete="CASCADE"
    )
    pass


def downgrade():
    op.drop_constraint("post_users_fkey", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
