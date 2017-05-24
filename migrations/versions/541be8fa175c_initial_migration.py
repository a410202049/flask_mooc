"""initial migration

Revision ID: 541be8fa175c
Revises: be5c46a19037
Create Date: 2017-05-22 14:40:24.865000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '541be8fa175c'
down_revision = 'be5c46a19037'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('group_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'users', 'users_group', ['group_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'group_id')
    # ### end Alembic commands ###
