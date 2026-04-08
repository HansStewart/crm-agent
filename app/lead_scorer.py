def score_contact(contact):
    """
    AI-style lead scoring for Hans Stewart's clients
    Scores real estate agents and fitness/wellness entrepreneurs
    """
    props = contact.get("properties", {})
    score = 0
    reasons = []

    # Job title scoring (max 25 points)
    title = (props.get("jobtitle") or "").lower()
    high_value_titles = ["owner", "founder", "broker", "ceo", "director", "partner"]
    mid_value_titles = ["manager", "agent", "realtor", "coach", "instructor"]

    if any(t in title for t in high_value_titles):
        score += 25
        reasons.append("Decision maker title (+25)")
    elif any(t in title for t in mid_value_titles):
        score += 15
        reasons.append("Relevant title (+15)")
    else:
        score += 5
        reasons.append("Standard title (+5)")

    # Lead status scoring (max 30 points)
    status = (props.get("hs_lead_status") or "").upper()
    status_scores = {
        "IN_PROGRESS": 30,
        "OPEN": 20,
        "NEW": 10,
        "UNQUALIFIED": 2
    }
    status_score = status_scores.get(status, 5)
    score += status_score
    reasons.append(f"Lead status: {status} (+{status_score})")

    # Has email (max 15 points)
    if props.get("email"):
        score += 15
        reasons.append("Email available (+15)")

    # Has phone (max 15 points)
    if props.get("phone"):
        score += 15
        reasons.append("Phone available (+15)")

    # Has company (max 15 points)
    if props.get("company"):
        score += 15
        reasons.append("Company associated (+15)")

    # Determine priority
    if score >= 75:
        priority = "🔥 HOT"
    elif score >= 50:
        priority = "⚡ WARM"
    elif score >= 25:
        priority = "❄️ COOL"
    else:
        priority = "💤 COLD"

    return {
        "score": min(score, 100),
        "priority": priority,
        "scoring_reasons": reasons
    }