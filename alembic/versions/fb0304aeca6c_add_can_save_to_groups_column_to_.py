"""Add can_save_to_groups column to invitations table

Revision ID: fb0304aeca6c
Revises: e4cfcff820c5
Create Date: 2021-05-24 17:17:14.288485

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'fb0304aeca6c'
down_revision = 'e4cfcff820c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        'invitations',
        sa.Column('can_save_to_groups', postgresql.ARRAY(sa.Boolean()), nullable=True),
    )
    invitations = sa.Table(
        "invitations",
        sa.MetaData(),
        sa.Column("id", sa.Integer()),
        sa.Column("can_save_to_groups", postgresql.ARRAY(sa.Boolean())),
    )
    conn = op.get_bind()
    conn.execute(
        invitations.update()
        .where(invitations.c.can_save_to_groups.is_(None))
        .values(can_save_to_groups=[True])
    )
    op.alter_column("invitations", "can_save_to_groups", nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('invitations', 'can_save_to_groups')
    # ### end Alembic commands ###