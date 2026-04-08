import requests
import os
from dotenv import load_dotenv

load_dotenv()

HUBSPOT_API_KEY = os.getenv("HUBSPOT_API_KEY")
BASE_URL = "https://api.hubapi.com"
HEADERS = {
    "Authorization": f"Bearer {HUBSPOT_API_KEY}",
    "Content-Type": "application/json"
}

def get_all_contacts():
    """Fetch all contacts from HubSpot"""
    response = requests.get(
        f"{BASE_URL}/crm/v3/objects/contacts",
        headers=HEADERS,
        params={
            "limit": 100,
            "properties": [
                "firstname", "lastname", "email",
                "jobtitle", "company", "phone",
                "hs_lead_status", "createdate",
                "lastmodifieddate", "city", "state"
            ]
        }
    )
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        print(f"HubSpot error: {response.text}")
        return []

def get_all_deals():
    """Fetch all deals from HubSpot"""
    response = requests.get(
        f"{BASE_URL}/crm/v3/objects/deals",
        headers=HEADERS,
        params={
            "limit": 100,
            "properties": [
                "dealname", "amount", "dealstage",
                "closedate", "createdate", "pipeline"
            ]
        }
    )
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        print(f"HubSpot error: {response.text}")
        return []

def get_all_companies():
    """Fetch all companies from HubSpot"""
    response = requests.get(
        f"{BASE_URL}/crm/v3/objects/companies",
        headers=HEADERS,
        params={
            "limit": 100,
            "properties": [
                "name", "industry", "annualrevenue",
                "numberofemployees", "city", "state"
            ]
        }
    )
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        print(f"HubSpot error: {response.text}")
        return []

def get_contact_by_id(contact_id):
    """Fetch a single contact by ID"""
    response = requests.get(
        f"{BASE_URL}/crm/v3/objects/contacts/{contact_id}",
        headers=HEADERS,
        params={
            "properties": [
                "firstname", "lastname", "email",
                "jobtitle", "company", "phone",
                "hs_lead_status", "city", "state"
            ]
        }
    )
    if response.status_code == 200:
        return response.json()
    return None

def get_pipeline_summary():
    """Get pipeline summary from deals"""
    deals = get_all_deals()
    total_value = 0
    by_stage = {}

    for deal in deals:
        props = deal.get("properties", {})
        amount = float(props.get("amount") or 0)
        stage = props.get("dealstage", "unknown")
        total_value += amount
        if stage not in by_stage:
            by_stage[stage] = {"count": 0, "value": 0}
        by_stage[stage]["count"] += 1
        by_stage[stage]["value"] += amount

    return {
        "total_deals": len(deals),
        "total_pipeline_value": total_value,
        "by_stage": by_stage
    }