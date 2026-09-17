from app.database import SessionLocal
from app.models import Transaction, LoginEvent

db = SessionLocal()


transactions = [

    Transaction(
        transaction_id="TX001",
        customer_id="C001",
        amount=500,
        location="Chennai",
        device_id="D001",
        merchant="Amazon",
        transaction_type="Online",
        risk_score=0,
        risk_level="LOW",
        suspicious=False
    ),

    Transaction(
        transaction_id="TX002",
        customer_id="C002",
        amount=75000,
        location="Mumbai",
        device_id="UNKNOWN",
        merchant="Unknown Merchant",
        transaction_type="Online",
        risk_score=80,
        risk_level="HIGH",
        suspicious=True,
        reason="High amount, new device, unusual merchant"
    ),

    Transaction(
        transaction_id="TX003",
        customer_id="C003",
        amount=25000,
        location="Bangalore",
        device_id="D003",
        merchant="Flipkart",
        transaction_type="Online",
        risk_score=15,
        risk_level="LOW",
        suspicious=False
    ),

    Transaction(
        transaction_id="TX004",
        customer_id="C001",
        amount=60000,
        location="Delhi",
        device_id="UNKNOWN",
        merchant="Unknown",
        transaction_type="Online",
        risk_score=90,
        risk_level="HIGH",
        suspicious=True,
        reason="High amount, unusual location, unknown device"
    )

]


for transaction in transactions:

    db.add(transaction)


logins = [

    LoginEvent(
        customer_id="C001",
        ip_address="192.168.1.10",
        location="Chennai",
        device_id="D001",
        success=True,
        risk_score=0,
        risk_level="LOW",
        suspicious=False
    ),

    LoginEvent(
        customer_id="C002",
        ip_address="45.23.11.2",
        location="London",
        device_id="UNKNOWN",
        success=False,
        risk_score=80,
        risk_level="HIGH",
        suspicious=True,
        reason="Failed login and unknown device"
    )

]


for login in logins:

    db.add(login)


db.commit()

db.close()

print("Sample data inserted")