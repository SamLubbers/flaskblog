"""empty message

Revision ID: 6b015407680e
Revises: 8239523337f7
Create Date: 2018-01-26 08:11:53.374552

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b015407680e'
down_revision = '8239523337f7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', sa.String(length=80), nullable=True))
    op.add_column('user', sa.Column('username', sa.String(length=80), nullable=False))
    op.drop_column('user', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('name', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
    op.drop_column('user', 'username')
    op.drop_column('user', 'password')
    # ### end Alembic commands ###