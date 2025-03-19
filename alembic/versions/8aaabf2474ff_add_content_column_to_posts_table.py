"""add content column to posts table

Revision ID: 8aaabf2474ff
Revises: 1c08a467ecb7
Create Date: 2025-03-17 20:58:15.637563

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8aaabf2474ff'
down_revision: Union[str, None] = '1c08a467ecb7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts", sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts", 'content')
    pass
