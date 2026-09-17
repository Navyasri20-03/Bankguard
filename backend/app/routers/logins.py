from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import LoginEvent
from ..schemas import LoginCreate

router = APIRouter(
    prefix="/logins",
    tags=["Login Security"]
)


@router.post("/")
def create_login(
    login: LoginCreate,
    db: Session = Depends(get_db)
):

    score = 0
    reasons = []

    if not login.success:

        score += 30

        reasons.append(
            "Failed login attempt"
        )

    if login.device_id == "UNKNOWN":

        score += 30

        reasons.append(
            "Unknown device"
        )

    if score >= 61:

        level = "HIGH"

    elif score >= 31:

        level = "MEDIUM"

    else:

        level = "LOW"

    event = LoginEvent(

        customer_id=login.customer_id,

        ip_address=login.ip_address,

        location=login.location,

        device_id=login.device_id,

        success=login.success,

        risk_score=score,

        risk_level=level,

        suspicious=score >= 61,

        reason=", ".join(reasons)
    )

    db.add(event)

    db.commit()

    db.refresh(event)

    return event


@router.get("/")
def get_logins(
    db: Session = Depends(get_db)
):

    return db.query(LoginEvent).order_by(
        LoginEvent.timestamp.desc()
    ).all()