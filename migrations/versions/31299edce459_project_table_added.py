"""Project Table Added

Revision ID: 31299edce459
Revises: 38adf2c42591
Create Date: 2021-01-21 11:35:02.139784

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31299edce459'
down_revision = '38adf2c42591'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('creation_date', sa.String(length=20), nullable=False),
    sa.Column('limit_date', sa.String(length=20), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('leader_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['leader_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('project')
    # ### end Alembic commands ###