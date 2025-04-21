from sqlalchemy import Boolean, Column, DateTime, Enum, ForeignKey, MetaData, Numeric, String, Table, UUID

from bpla_service.domain.uav_flight.enums.status_type import UavFlightStatusType
from bpla_service.domain.user.enums.gender_type import UserGenderType


metadata = MetaData()
users = Table(
    "users",
    metadata,
    Column("id", UUID, primary_key=True),
    Column("email", String, unique=True, nullable=False),
    Column("hashed_password", String, nullable=False),
    Column("deleted_at", DateTime(timezone=True)),
    Column("created_at", DateTime(timezone=True), nullable=False),
    Column("issued_by", String, nullable=False),
    Column("date_of_issue", DateTime(timezone=True), nullable=False),
    Column("subdivision_code", String, nullable=False),
    Column("gender", Enum(*map(str, UserGenderType), name="user_gender_type"), nullable=False),
    Column("year_of_birth", DateTime(timezone=True), nullable=False),
    Column("place_of_birth", String, nullable=False),
    Column("serial_number", String, nullable=False),
    Column("number", String, nullable=False),
    Column("snils", String, nullable=False),
    Column('fio', String, nullable=False),
)
sessions = Table(
    "sessions",
    metadata,
    Column("id", UUID, primary_key=True),
    Column("user_id", UUID, ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
    Column("revoked", Boolean, nullable=False),
    Column("expires_in", DateTime(timezone=True), nullable=False),
    Column("deleted_at", DateTime(timezone=True)),
    Column("created_at", DateTime(timezone=True), nullable=False),
)
uav = Table(
    "uav",
    metadata,
    Column("id", UUID, primary_key=True),
    Column("user_id", UUID, ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
    Column("model", String, nullable=False),
    Column("serial_number", String, nullable=False),
    Column("deleted_at", DateTime(timezone=True)),
    Column("created_at", DateTime(timezone=True), nullable=False),
    Column("noise_characteristics", Numeric, nullable=False),
    Column("reference_number", String, nullable=False),
)
uav_flight = Table(
    "uav_flight",
    metadata,
    Column("id", UUID, primary_key=True),
    Column("user_id", UUID, ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
    Column("uav_id", UUID, ForeignKey("uav.id", ondelete="CASCADE"), nullable=False),
    Column("location", String, nullable=False),
    Column("status", Enum(*map(str, UavFlightStatusType), name="uav_flight_status_type"), nullable=False),
    Column("start_at", DateTime(timezone=True), nullable=False),
    Column("end_at", DateTime(timezone=True), nullable=False),
    Column("deleted_at", DateTime(timezone=True)),
    Column("created_at", DateTime(timezone=True), nullable=False),
)
