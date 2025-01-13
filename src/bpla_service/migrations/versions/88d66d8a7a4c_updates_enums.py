"""updates enums

Revision ID: 88d66d8a7a4c
Revises: 1f91c1982ad9
Create Date: 2024-12-02 23:47:13.546341

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

from bpla_service.domain.uav_flight.enums.status_type import UavFlightStatusType
from bpla_service.domain.user.enums.gender_type import UserGenderType


# revision identifiers, used by Alembic.
revision: str = '88d66d8a7a4c'
down_revision: Union[str, None] = '1f91c1982ad9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute('DROP TYPE IF EXISTS user_gender_type CASCADE;')
    op.execute('DROP TYPE IF EXISTS uav_flight_status_type CASCADE;')
    op.execute("CREATE TYPE user_gender_type AS ENUM ('male', 'female')")
    op.execute("CREATE TYPE uav_flight_status_type AS ENUM ('accepted', 'finished', 'rejected', 'under_review')")
    op.add_column(
        'users',
        sa.Column('gender', sa.Enum(*map(str, UserGenderType), name='user_gender_type'), nullable=False)
    )
    op.add_column(
        'uav_flight',
        sa.Column('status', sa.Enum(*map(str, UavFlightStatusType), name='uav_flight_status_type'), nullable=False)
    )


def downgrade() -> None:
    pass
