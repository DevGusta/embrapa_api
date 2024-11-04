from sqlalchemy import Column,String, Boolean
from src.database.database import Base

class User(Base):
    __tablename__ = "users"

    username: str = Column(String(50), primary_key=True, unique=True, index=True, nullable=False)
    email: str = Column(String(100), unique=True, index=True, nullable=False)
    full_name: str = Column(String(100))
    hashed_password: str = Column(String(255), nullable=False)
    disabled: bool = Column(Boolean, default=False)