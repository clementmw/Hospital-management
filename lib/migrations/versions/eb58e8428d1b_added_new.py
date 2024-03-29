"""added new

Revision ID: eb58e8428d1b
Revises: 568eaf6c0e0b
Create Date: 2024-01-21 01:09:43.728598

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb58e8428d1b'
down_revision = '568eaf6c0e0b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('doctors', sa.Column('id_no', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('doctors', 'id_no')
    # ### end Alembic commands ###
