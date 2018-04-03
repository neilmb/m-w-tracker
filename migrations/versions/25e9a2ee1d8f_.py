"""Add kind table and indirection for events.

Revision ID: 25e9a2ee1d8f
Revises: be52fb341b1f
Create Date: 2018-04-03 09:37:35.589595

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25e9a2ee1d8f'
down_revision = 'be52fb341b1f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('kind',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('event', sa.Column('kind_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'event', 'kind', ['kind_id'], ['id'])
    op.drop_column('event', 'kind')


def downgrade():
    op.add_column('event', sa.Column('kind', sa.VARCHAR(length=30), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'event', type_='foreignkey')
    op.drop_column('event', 'kind_id')
    op.drop_table('kind')
