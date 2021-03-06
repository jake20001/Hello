"""empty message

Revision ID: 7709655c9185
Revises: 
Create Date: 2021-02-08 15:28:40.004205

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7709655c9185'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('t_adr')
    op.add_column('t_user', sa.Column('address', sa.String(length=128), nullable=True))
    op.add_column('t_user', sa.Column('age', sa.Integer(), nullable=True))
    op.add_column('t_user', sa.Column('dad', sa.String(length=128), nullable=True))
    op.add_column('t_user', sa.Column('username', sa.String(length=20), nullable=True))
    op.create_index(op.f('ix_t_user_age'), 't_user', ['age'], unique=False)
    op.create_unique_constraint(None, 't_user', ['username'])
    op.drop_column('t_user', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('t_user', sa.Column('name', mysql.VARCHAR(length=20), nullable=True))
    op.drop_constraint(None, 't_user', type_='unique')
    op.drop_index(op.f('ix_t_user_age'), table_name='t_user')
    op.drop_column('t_user', 'username')
    op.drop_column('t_user', 'dad')
    op.drop_column('t_user', 'age')
    op.drop_column('t_user', 'address')
    op.create_table('t_adr',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('detail', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['t_user.id'], name='t_adr_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
