"""initial migration

Revision ID: 8d89ed369a8d
Revises: f52c4f9eb3d5
Create Date: 2017-05-22 14:19:48.614000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d89ed369a8d'
down_revision = 'f52c4f9eb3d5'
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
