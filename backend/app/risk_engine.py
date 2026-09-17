def calculate_transaction_risk(
    amount,
    new_device=False,
    unusual_location=False,
    unusual_merchant=False
):

    score = 0
    reasons = []

    if amount > 50000:
        score += 30
        reasons.append("Unusually high transaction amount")

    elif amount > 20000:
        score += 15
        reasons.append("Higher than normal transaction amount")

    if new_device:
        score += 25
        reasons.append("New device detected")

    if unusual_location:
        score += 25
        reasons.append("Unusual transaction location")

    if unusual_merchant:
        score += 20
        reasons.append("Unusual merchant")

    score = min(score, 100)

    if score >= 61:
        level = "HIGH"

    elif score >= 31:
        level = "MEDIUM"

    else:
        level = "LOW"

    return score, level, reasons