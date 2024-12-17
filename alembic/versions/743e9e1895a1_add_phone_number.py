"""add phone number

Revision ID: 743e9e1895a1
Revises: 9f79731ba0ed
Create Date: 2024-12-15 16:32:30.263738

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '743e9e1895a1'
down_revision = '9f79731ba0ed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###