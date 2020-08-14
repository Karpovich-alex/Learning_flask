"""followers

Revision ID: 63324e0fa236
Revises: 9b9c114ae5e4
Create Date: 2020-08-05 14:57:20.627576

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63324e0fa236'
down_revision = '9b9c114ae5e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
