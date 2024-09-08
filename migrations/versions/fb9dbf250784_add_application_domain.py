"""add application domain

Revision ID: fb9dbf250784
Revises: f49eb0d3e125
Create Date: 2024-09-07 21:33:43.607721

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = "fb9dbf250784"
down_revision: Union[str, None] = "f49eb0d3e125"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "domain",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("description", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.add_column("application", sa.Column("domain_id", sa.Uuid()))
    op.create_index(
        op.f("ix_application_domain_id"), "application", ["domain_id"], unique=False
    )
    op.create_foreign_key(
        "application_domain_id_fkey", "application", "domain", ["domain_id"], ["id"]
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("application_domain_id_fkey", "application", type_="foreignkey")
    op.drop_index(op.f("ix_application_domain_id"), table_name="application")
    op.drop_column("application", "domain_id")
    op.drop_table("domain")
    # ### end Alembic commands ###
