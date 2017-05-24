"""initial migration

Revision ID: 347cd826c3dc
Revises: 541be8fa175c
Create Date: 2017-05-22 14:44:18.934000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '347cd826c3dc'
down_revision = '541be8fa175c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'users', 'users_group', ['group_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    # ### end Alembic commands ###