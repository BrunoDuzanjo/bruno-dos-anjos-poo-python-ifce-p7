"""empty message

Revision ID: 3ca31ee44ae5
Revises: d8ea7ac63fcd
Create Date: 2021-08-05 15:34:10.065817

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ca31ee44ae5'
down_revision = 'd8ea7ac63fcd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('produtos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('codigo', sa.Integer(), nullable=True),
    sa.Column('descricao', sa.String(length=20), nullable=True),
    sa.Column('valor_unitario', sa.Float(precision=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('itens',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sequencial', sa.Integer(), nullable=True),
    sa.Column('quantidade', sa.Integer(), nullable=True),
    sa.Column('produto_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['produto_id'], ['produtos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('notas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('codigo', sa.Integer(), nullable=True),
    sa.Column('cliente_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cliente_id'], ['clientes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('proutos')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('proutos',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('codigo', sa.INTEGER(), nullable=True),
    sa.Column('descricao', sa.VARCHAR(length=20), nullable=True),
    sa.Column('valor_unitario', sa.FLOAT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('notas')
    op.drop_table('itens')
    op.drop_table('produtos')
    # ### end Alembic commands ###
