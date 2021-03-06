"""empty message

Revision ID: ad31d371c8fd
Revises: 
Create Date: 2020-12-03 11:32:11.648466

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad31d371c8fd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('match',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('match_name', sa.String(), nullable=False),
    sa.Column('date', sa.Integer(), nullable=False),
    sa.Column('winner1', sa.String(), nullable=False),
    sa.Column('winner2', sa.String(), nullable=False),
    sa.Column('loser1', sa.String(), nullable=False),
    sa.Column('loser2', sa.String(), nullable=False),
    sa.Column('winner_get_game', sa.Integer(), nullable=False),
    sa.Column('loser_get_game', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('match')
    # ### end Alembic commands ###
