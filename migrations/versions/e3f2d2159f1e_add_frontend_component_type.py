"""add frontend component type

Revision ID: e3f2d2159f1e
Revises: fb9dbf250784
Create Date: 2024-09-08 20:43:36.899480

"""
from typing import Sequence, Union

from alembic import op
from alembic_postgresql_enum import TableReference

# revision identifiers, used by Alembic.
revision: str = "e3f2d2159f1e"
down_revision: Union[str, None] = "fb9dbf250784"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.sync_enum_values(
        "public",
        "type",
        ["batch", "frontend", "library", "service"],
        [
            TableReference(
                table_schema="public", table_name="component", column_name="type"
            )
        ],
        enum_values_to_rename=[],
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.sync_enum_values(
        "public",
        "type",
        ["batch", "library", "service"],
        [
            TableReference(
                table_schema="public", table_name="component", column_name="type"
            )
        ],
        enum_values_to_rename=[],
    )
    # ### end Alembic commands ###
