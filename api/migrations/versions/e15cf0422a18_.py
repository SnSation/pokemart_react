"""empty message

Revision ID: e15cf0422a18
Revises: 9c4462a40fbf
Create Date: 2020-12-03 00:09:35.266096

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e15cf0422a18'
down_revision = '9c4462a40fbf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('unova_pokemon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('dex_id', sa.Integer(), nullable=True),
    sa.Column('type1', sa.String(length=20), nullable=True),
    sa.Column('type2', sa.String(length=20), nullable=True),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('sprite', sa.String(length=200), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('unova_pokemon')
    # ### end Alembic commands ###
