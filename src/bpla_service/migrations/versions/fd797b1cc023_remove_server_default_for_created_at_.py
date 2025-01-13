"""remove server_default for created_at fields

Revision ID: fd797b1cc023
Revises: 88d66d8a7a4c
Create Date: 2024-12-02 23:56:16.983075

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fd797b1cc023'
down_revision: Union[str, None] = '88d66d8a7a4c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('users', 'created_at', nullable=False, server_default=None)
    op.alter_column('sessions', 'created_at', nullable=False, server_default=None)


def downgrade() -> None:
    op.alter_column('users', 'created_at', nullable=False, server_default=sa.text('now()'))
    op.alter_column('sessions', 'created_at', nullable=False, server_default=sa.text('now()'))