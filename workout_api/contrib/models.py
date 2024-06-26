# from sqlalchemy import uuid4
import uuid 
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

class BaseModel(DeclarativeBase):
    id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True),default = uuid.uuid4, nullable=False)