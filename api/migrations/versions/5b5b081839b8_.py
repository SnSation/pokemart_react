"""empty message

Revision ID: 5b5b081839b8
Revises: 506ccf65e57f
Create Date: 2020-12-03 00:44:22.946957

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b5b081839b8'
down_revision = '506ccf65e57f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pokemon_types', sa.Column('attack_immune', sa.String(length=100), nullable=True))
    op.add_column('pokemon_types', sa.Column('attack_strength', sa.String(length=100), nullable=True))
    op.add_column('pokemon_types', sa.Column('attack_weakness', sa.String(length=100), nullable=True))
    op.add_column('pokemon_types', sa.Column('defense_immune', sa.String(length=100), nullable=True))
    op.add_column('pokemon_types', sa.Column('defense_strength', sa.String(length=100), nullable=True))
    op.add_column('pokemon_types', sa.Column('defense_weakness', sa.String(length=100), nullable=True))
    op.drop_column('pokemon_types', 'immune')
    op.drop_column('pokemon_types', 'strong')
    op.drop_column('pokemon_types', 'weak')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pokemon_types', sa.Column('weak', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    op.add_column('pokemon_types', sa.Column('strong', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    op.add_column('pokemon_types', sa.Column('immune', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    op.drop_column('pokemon_types', 'defense_weakness')
    op.drop_column('pokemon_types', 'defense_strength')
    op.drop_column('pokemon_types', 'defense_immune')
    op.drop_column('pokemon_types', 'attack_weakness')
    op.drop_column('pokemon_types', 'attack_strength')
    op.drop_column('pokemon_types', 'attack_immune')
    # ### end Alembic commands ###
