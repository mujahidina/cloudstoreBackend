"""added is_delete column

Revision ID: 307cbc6ee6d7
Revises: 538a6f02b505
Create Date: 2024-05-21 12:39:14.842161

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '307cbc6ee6d7'
down_revision = '538a6f02b505'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('files', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_delete', sa.Boolean(), nullable=True))

    with op.batch_alter_table('folders', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_delete', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('folders', schema=None) as batch_op:
        batch_op.drop_column('is_delete')

    with op.batch_alter_table('files', schema=None) as batch_op:
        batch_op.drop_column('is_delete')

    # ### end Alembic commands ###