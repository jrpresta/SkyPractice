"""Fixing import issue

Revision ID: 6c83dff2dd1d
Revises: 
Create Date: 2025-02-17 15:37:36.389840

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6c83dff2dd1d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_therapists_email', table_name='therapists')
    op.drop_index('ix_therapists_id', table_name='therapists')
    op.drop_table('therapists')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('therapists',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=False),
    sa.Column('email', sa.VARCHAR(), nullable=False),
    sa.Column('password_hash', sa.VARCHAR(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_therapists_id', 'therapists', ['id'], unique=False)
    op.create_index('ix_therapists_email', 'therapists', ['email'], unique=1)
    # ### end Alembic commands ###
