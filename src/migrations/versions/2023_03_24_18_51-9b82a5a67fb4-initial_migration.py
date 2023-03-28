"""initial_migration

Revision ID: 9b82a5a67fb4
Revises: 
Create Date: 2023-03-24 18:51:39.429584

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b82a5a67fb4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('well_data',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('inclinometry', sa.JSON(), nullable=True),
    sa.Column('d_cas', sa.Float(), nullable=True),
    sa.Column('d_tub', sa.Float(), nullable=True),
    sa.Column('h_tub', sa.Float(), nullable=True),
    sa.Column('wct', sa.Float(), nullable=True),
    sa.Column('rp', sa.Float(), nullable=True),
    sa.Column('gamma_oil', sa.Float(), nullable=True),
    sa.Column('gamma_gas', sa.Float(), nullable=True),
    sa.Column('gamma_wat', sa.Float(), nullable=True),
    sa.Column('t_res', sa.Float(), nullable=True),
    sa.Column('p_wh', sa.Float(), nullable=True),
    sa.Column('geo_grad', sa.Float(), nullable=True),
    sa.Column('h_res', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vlp',
    sa.Column('vlp', sa.JSON(), nullable=True),
    sa.Column('well_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['well_id'], ['well_data.id'], ),
    sa.PrimaryKeyConstraint('well_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vlp')
    op.drop_table('well_data')
    # ### end Alembic commands ###
