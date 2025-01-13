"""add passport fields for user

Revision ID: 77e0aae138c7
Revises: 9aed14d0ac81
Create Date: 2024-12-02 00:21:15.188786

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

from uav_service.domain.user.enums.gender_type import UserGenderType


# revision identifiers, used by Alembic.
revision: str = '77e0aae138c7'
down_revision: Union[str, None] = '9aed14d0ac81'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("CREATE TYPE user_gender_type AS ENUM ('male', 'female')")
    op.add_column('users', sa.Column('issued_by', sa.String(), nullable=False))
    op.add_column('users', sa.Column('date_of_issue', sa.DateTime(timezone=True), nullable=False))
    op.add_column('users', sa.Column('subdivision_code', sa.String(), nullable=False))
    op.add_column('users', sa.Column('gender', sa.Enum(UserGenderType, name='user_gender_type'), nullable=False))
    op.add_column('users', sa.Column('year_of_birth', sa.DateTime(timezone=True), nullable=False))
    op.add_column('users', sa.Column('place_of_birth', sa.String(), nullable=False))
    op.add_column('users', sa.Column('serial_number', sa.String(), nullable=False))
    op.add_column('users', sa.Column('number', sa.String(), nullable=False))
    op.add_column('users', sa.Column('snils', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'snils')
    op.drop_column('users', 'number')
    op.drop_column('users', 'serial_number')
    op.drop_column('users', 'place_of_birth')
    op.drop_column('users', 'year_of_birth')
    op.drop_column('users', 'gender')
    op.drop_column('users', 'subdivision_code')
    op.drop_column('users', 'date_of_issue')
    op.drop_column('users', 'issued_by')
    # ### end Alembic commands ###
