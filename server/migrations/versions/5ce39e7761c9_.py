"""empty message

Revision ID: 5ce39e7761c9
Revises: 
Create Date: 2023-06-16 12:38:27.652832

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ce39e7761c9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('authors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('phone_number', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('content', sa.String(), nullable=True),
    sa.Column('summary', sa.String(length=250), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    op.drop_table('authors')
    # ### end Alembic commands ###
