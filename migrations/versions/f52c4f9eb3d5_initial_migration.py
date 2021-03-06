"""initial migration

Revision ID: f52c4f9eb3d5
Revises: c83b808fab81
Create Date: 2017-05-22 13:55:52.981000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f52c4f9eb3d5'
down_revision = 'c83b808fab81'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('create_time', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('group_id', sa.Integer(), nullable=True))
    op.add_column('users', sa.Column('update_time', sa.DateTime(), nullable=True))
    op.create_foreign_key(None, 'users', 'users_group', ['group_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'update_time')
    op.drop_column('users', 'group_id')
    op.drop_column('users', 'create_time')
    # ### end Alembic commands ###
