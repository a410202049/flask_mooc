"""add user is_manage

Revision ID: e62ec86d6085
Revises: 3423c3482291
Create Date: 2017-05-26 15:35:08.959000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e62ec86d6085'
down_revision = '3423c3482291'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_manage', sa.Enum('1', '0'), nullable=True))
    op.create_foreign_key(None, 'users', 'users_group', ['group_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'is_manage')
    # ### end Alembic commands ###
