"""Add initial table and columns

Revision ID: be52fb341b1f
Revises: 852a9c869b8e
Create Date: 2018-04-02 10:17:29.536305

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be52fb341b1f'
down_revision = '852a9c869b8e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('kind', sa.String(length=30), nullable=True),
    sa.Column('comment', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('event')
