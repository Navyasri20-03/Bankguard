from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from ..database import get_db
from ..models import Transaction, LoginEvent

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/stats")
def dashboard_stats(
    db: Session = Depends(get_db)
):

    total_transactions = db.query(
        Transaction
    ).count()

    suspicious_transactions = db.query(
        Transaction
    ).filter(
        Transaction.suspicious == True
    ).count()

    total_amount = db.query(
        func.sum(Transaction.amount)
    ).scalar() or 0

    failed_logins = db.query(
        LoginEvent
    ).filter(
        LoginEvent.success == False
    ).count()

    high_risk_logins = db.query(
        LoginEvent
    ).filter(
        LoginEvent.risk_level == "HIGH"
    ).count()

    return {

        "total_transactions":
            total_transactions,

        "suspicious_transactions":
            suspicious_transactions,

        "total_amount":
            total_amount,

        "failed_logins":
            failed_logins,

        "high_risk_logins":
            high_risk_logins
    }