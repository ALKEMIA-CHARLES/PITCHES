"""empty message

Revision ID: 27193c787849
Revises: c192587f7e5d
Create Date: 2019-11-26 14:56:57.138528

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27193c787849'
down_revision = 'c192587f7e5d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('feedback', sa.Column('comments_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'feedback', 'comments', ['comments_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'feedback', type_='foreignkey')
    op.drop_column('feedback', 'comments_id')
    # ### end Alembic commands ###