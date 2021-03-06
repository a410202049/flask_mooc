"""initial migration

Revision ID: 531ae271926c
Revises: d1cb6f1bddc6
Create Date: 2017-05-22 15:01:31.492000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '531ae271926c'
down_revision = 'd1cb6f1bddc6'
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
