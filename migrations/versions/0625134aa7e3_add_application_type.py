"""add application type

Revision ID: 0625134aa7e3
Revises: 63133f827f17
Create Date: 2024-09-05 19:57:49.519649

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "0625134aa7e3"
down_revision: Union[str, None] = "63133f827f17"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    sa.Enum("batch", "library", "service", name="type").create(op.get_bind())
    op.add_column(
        "application",
        sa.Column(
            "type",
            postgresql.ENUM(
                "batch", "library", "service", name="type", create_type=False
            ),
            nullable=False,
            server_default="service",
        ),
    )
    op.alter_column(
        "application",
        "description",
        existing_type=sa.VARCHAR(length=1000),
        nullable=False,
    )
    op.create_index(op.f("ix_application_type"), "application", ["type"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_application_type"), table_name="application")
    op.alter_column(
        "application",
        "description",
        existing_type=sa.VARCHAR(length=1000),
        nullable=True,
    )
    op.drop_column("application", "type")
    sa.Enum("batch", "library", "service", name="type").drop(op.get_bind())
    # ### end Alembic commands ###
