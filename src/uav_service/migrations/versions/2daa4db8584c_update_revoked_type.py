"""update revoked type

Revision ID: 2daa4db8584c
Revises: fd797b1cc023
Create Date: 2024-12-03 16:37:26.213448

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = '2daa4db8584c'
down_revision: Union[str, None] = 'fd797b1cc023'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute('ALTER TABLE sessions ALTER COLUMN revoked TYPE boolean USING revoked::boolean;')


def downgrade() -> None:
    pass
