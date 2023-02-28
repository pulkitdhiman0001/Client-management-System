"""empty message

Revision ID: cc2f97182ab5
Revises: 76426aa80c78
Create Date: 2023-01-11 14:09:19.369085

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc2f97182ab5'
down_revision = '76426aa80c78'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('records', schema=None) as batch_op:
        batch_op.alter_column('bill',
               existing_type=sa.NUMERIC(),
               type_=sa.String(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('records', schema=None) as batch_op:
        batch_op.alter_column('bill',
               existing_type=sa.String(),
               type_=sa.NUMERIC(),
               existing_nullable=True)

    # ### end Alembic commands ###