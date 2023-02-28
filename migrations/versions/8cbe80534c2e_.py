"""empty message

Revision ID: 8cbe80534c2e
Revises: fc62d74cafc3
Create Date: 2023-02-22 14:11:09.015911

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8cbe80534c2e'
down_revision = 'fc62d74cafc3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sales_order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('total_payable', sa.Float(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sales_order', schema=None) as batch_op:
        batch_op.drop_column('total_payable')

    # ### end Alembic commands ###