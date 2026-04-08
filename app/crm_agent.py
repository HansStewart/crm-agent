from openai import OpenAI
from dotenv import load_dotenv
import os
from app.lead_scorer import score_contact

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_contact(contact):
    """AI analysis of a single HubSpot contact"""
    props = contact.get("properties", {})
    scoring = score_contact(contact)

    contact_summary = f"""
    Name: {props.get('firstname', '')} {props.get('lastname', '')}
    Title: {props.get('jobtitle', 'Unknown')}
    Company: {props.get('company', 'Unknown')}
    Email: {props.get('email', 'Unknown')}
    Phone: {props.get('phone', 'Unknown')}
    Lead Status: {props.get('hs_lead_status', 'Unknown')}
    Location: {props.get('city', '')}, {props.get('state', '')}
    AI Score: {scoring['score']}/100
    Priority: {scoring['priority']}
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": """You are an expert sales consultant for Hans Stewart,
                who provides AI-powered marketing and CRM services to real estate agents
                and fitness/wellness entrepreneurs across the US.
                Analyze this contact and provide:
                1. Lead quality assessment
                2. Specific recommended next action
                3. Personalized outreach message (2-3 sentences)
                4. Best follow-up timing
                5. Key talking points for Hans to use
                Be specific, actionable, and tailored to their industry."""
            },
            {
                "role": "user",
                "content": f"Analyze this contact:\n{contact_summary}"
            }
        ],
        max_tokens=600
    )

    return {
        "contact_id": contact.get("id"),
        "name": f"{props.get('firstname', '')} {props.get('lastname', '')}",
        "company": props.get("company", "Unknown"),
        "title": props.get("jobtitle", "Unknown"),
        "email": props.get("email", ""),
        "lead_status": props.get("hs_lead_status", "Unknown"),
        "ai_score": scoring["score"],
        "priority": scoring["priority"],
        "scoring_reasons": scoring["scoring_reasons"],
        "ai_analysis": response.choices[0].message.content
    }

def score_all_contacts(contacts):
    """Score and rank all HubSpot contacts"""
    scored = []
    for contact in contacts:
        props = contact.get("properties", {})
        scoring = score_contact(contact)
        scored.append({
            "id": contact.get("id"),
            "name": f"{props.get('firstname', '')} {props.get('lastname', '')}",
            "company": props.get("company", "Unknown"),
            "title": props.get("jobtitle", "Unknown"),
            "lead_status": props.get("hs_lead_status", "Unknown"),
            "ai_score": scoring["score"],
            "priority": scoring["priority"]
        })
    scored.sort(key=lambda x: x["ai_score"], reverse=True)
    return scored

def generate_pipeline_report(contacts, deals_summary):
    """Generate AI-powered pipeline report for Hans Stewart"""
    scored = score_all_contacts(contacts)

    leads_context = "\n".join([
        f"- {l['name']} ({l['company']}) — {l['title']}: "
        f"Score {l['ai_score']}/100, Status: {l['lead_status']}"
        for l in scored[:10]
    ])

    pipeline_context = f"""
    Hans Stewart's CRM Pipeline Summary:
    Total Contacts: {len(contacts)}
    Total Deals: {deals_summary['total_deals']}
    Total Pipeline Value: ${deals_summary['total_pipeline_value']:,.2f}
    Pipeline by Stage: {deals_summary['by_stage']}

    Top Ranked Contacts:
    {leads_context}
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": """You are an expert sales operations analyst for Hans Stewart,
                who provides AI-powered marketing and CRM services to real estate agents
                and fitness/wellness entrepreneurs nationwide.
                Generate a comprehensive pipeline report including:
                1. Executive Summary
                2. Top Opportunities to pursue this week
                3. Pipeline Health Assessment
                4. Revenue Forecast
                5. Specific action items for Hans
                6. Contacts at risk of going cold
                Be specific, data-driven, and actionable."""
            },
            {
                "role": "user",
                "content": f"Generate pipeline report:\n{pipeline_context}"
            }
        ],
        max_tokens=1500
    )

    return {
        "total_contacts": len(contacts),
        "deals_summary": deals_summary,
        "ranked_contacts": scored,
        "top_contact": scored[0] if scored else None,
        "hot_leads": [c for c in scored if c["ai_score"] >= 75],
        "cold_leads": [c for c in scored if c["ai_score"] < 25],
        "ai_report": response.choices[0].message.content
    }

def generate_email_sequence(contact):
    """Generate personalized email sequence for a HubSpot contact"""
    props = contact.get("properties", {})
    scoring = score_contact(contact)
    title = props.get("jobtitle", "").lower()

    if any(t in title for t in ["realtor", "agent", "broker", "property"]):
        industry = "real estate"
    else:
        industry = "fitness and wellness"

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": f"""You are writing emails on behalf of Hans Stewart,
                an AI-powered marketing and CRM consultant.
                Create a 3-email follow-up sequence for a {industry} professional.
                Each email should be:
                - Personalized to their role and industry
                - Value-focused (what Hans can do for THEM)
                - Professional but warm
                - Under 150 words each
                Format: Email 1, Email 2, Email 3 with Subject and Body."""
            },
            {
                "role": "user",
                "content": f"""Create email sequence for:
                Name: {props.get('firstname', '')} {props.get('lastname', '')}
                Title: {props.get('jobtitle', '')}
                Company: {props.get('company', '')}
                Industry: {industry}
                Lead Score: {scoring['score']}/100
                Lead Status: {props.get('hs_lead_status', '')}"""
            }
        ],
        max_tokens=800
    )

    return {
        "contact_name": f"{props.get('firstname', '')} {props.get('lastname', '')}",
        "contact_email": props.get("email", ""),
        "company": props.get("company", ""),
        "industry": industry,
        "lead_score": scoring["score"],
        "priority": scoring["priority"],
        "email_sequence": response.choices[0].message.content
    }