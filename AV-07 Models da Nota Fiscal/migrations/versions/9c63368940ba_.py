"""empty message

Revision ID: 9c63368940ba
Revises: 3ca31ee44ae5
Create Date: 2021-08-05 16:44:54.378619

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c63368940ba'
down_revision = '3ca31ee44ae5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('itens', sa.Column('nota_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'itens', 'notas', ['nota_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'itens', type_='foreignkey')
    op.drop_column('itens', 'nota_id')
    # ### end Alembic commands ###
