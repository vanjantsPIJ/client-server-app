"""add gds pressure

Revision ID: 8a274de2e96d
Revises: a30f5f27142b
Create Date: 2024-05-10 02:13:17.566282

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8a274de2e96d'
down_revision: Union[str, None] = 'a30f5f27142b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('GDS_Pressure',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('GDS_ID', sa.Integer(), nullable=False),
    sa.Column('PressureSensorID', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['GDS_ID'], ['GDS.GDS_ID'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('PressureSensorID')
    )
    op.alter_column('GDS_Temperature', 'TempSensorID',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.create_unique_constraint(None, 'GDS_Temperature', ['TempSensorID'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'GDS_Temperature', type_='unique')
    op.alter_column('GDS_Temperature', 'TempSensorID',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_table('GDS_Pressure')
    # ### end Alembic commands ###
