from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Transaction
from ..schemas import TransactionCreate
from ..risk_engine import calculate_transaction_risk

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)


@router.post("/")
def create_transaction(
    transaction: TransactionCreate,
    db: Session = Depends(get_db)
):

    score, level, reasons = calculate_transaction_risk(
        amount=transaction.amount,
        new_device=False,
        unusual_location=False,
        unusual_merchant=False
    )

    new_transaction = Transaction(
        transaction_id=transaction.transaction_id,
        customer_id=transaction.customer_id,
        amount=transaction.amount,
        location=transaction.location,
        device_id=transaction.device_id,
        merchant=transaction.merchant,
        transaction_type=transaction.transaction_type,
        risk_score=score,
        risk_level=level,
        suspicious=score >= 61,
        reason=", ".join(reasons)
    )

    db.add(new_transaction)

    db.commit()

    db.refresh(new_transaction)

    return new_transaction


@router.get("/")
def get_transactions(
    db: Session = Depends(get_db)
):

    return db.query(Transaction).order_by(
        Transaction.timestamp.desc()
    ).all()


@router.get("/alerts")
def get_alerts(
    db: Session = Depends(get_db)
):

    return db.query(Transaction).filter(
        Transaction.suspicious == True
    ).order_by(
        Transaction.timestamp.desc()
    ).all()