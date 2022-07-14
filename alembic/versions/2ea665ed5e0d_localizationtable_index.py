"""LocalizationTable index migration

Revision ID: 2ea665ed5e0d
Revises: 336795744e40
Create Date: 2022-07-14 21:29:25.816203

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = '2ea665ed5e0d'
down_revision = '336795744e40'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(
        op.f('ix_localizationtiles_localization_id'),
        'localizationtiles',
        ['localization_id'],
        unique=False,
    )
    op.create_index(
        op.f('ix_localizationtiles_probdensity'),
        'localizationtiles',
        ['probdensity'],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        op.f('ix_localizationtiles_probdensity'), table_name='localizationtiles'
    )
    op.drop_index(
        op.f('ix_localizationtiles_localization_id'), table_name='localizationtiles'
    )
    # ### end Alembic commands ###