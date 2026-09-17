from pydantic import BaseModel
from datetime import datetime


class TransactionCreate(BaseModel):

    transaction_id: str
    customer_id: str
    amount: float
    location: str
    device_id: str
    merchant: str
    transaction_type: str


class TransactionResponse(BaseModel):

    id: int
    transaction_id: str
    customer_id: str
    amount: float
    location: str
    device_id: str
    merchant: str
    transaction_type: str
    timestamp: datetime
    risk_score: int
    risk_level: str
    suspicious: bool
    reason: str | None

    class Config:
        from_attributes = True
        
class LoginCreate(BaseModel):

    customer_id: str
    ip_address: str
    location: str
    device_id: str
    success: bool = True