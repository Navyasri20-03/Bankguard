from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from datetime import datetime

from .database import Base


class Transaction(Base):

    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)

    transaction_id = Column(String, unique=True, index=True)

    customer_id = Column(String, index=True)

    amount = Column(Float)

    location = Column(String)

    device_id = Column(String)

    merchant = Column(String)

    transaction_type = Column(String)

    timestamp = Column(DateTime, default=datetime.utcnow)

    risk_score = Column(Integer, default=0)

    risk_level = Column(String, default="LOW")

    suspicious = Column(Boolean, default=False)

    reason = Column(String, nullable=True)


class LoginEvent(Base):

    __tablename__ = "login_events"

    id = Column(Integer, primary_key=True, index=True)

    customer_id = Column(String, index=True)

    ip_address = Column(String)

    location = Column(String)

    device_id = Column(String)

    timestamp = Column(DateTime, default=datetime.utcnow)

    success = Column(Boolean, default=True)

    risk_score = Column(Integer, default=0)

    risk_level = Column(String, default="LOW")

    suspicious = Column(Boolean, default=False)

    reason = Column(String, nullable=True)