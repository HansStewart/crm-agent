import requests
import os
import time
from dotenv import load_dotenv

load_dotenv()

HUBSPOT_API_KEY = os.getenv("HUBSPOT_API_KEY")
BASE_URL = "https://api.hubapi.com"
HEADERS = {
    "Authorization": f"Bearer {HUBSPOT_API_KEY}",
    "Content-Type": "application/json"
}

# Hans Stewart - Real Estate Agent Clients (Nationwide)
REAL_ESTATE_COMPANIES = [
    {"name": "Coastal Realty Group", "industry": "REAL_ESTATE", "annualrevenue": "850000", "numberofemployees": "8", "city": "Jacksonville", "state": "FL"},
    {"name": "Skyline Properties", "industry": "REAL_ESTATE", "annualrevenue": "1200000", "numberofemployees": "12", "city": "Chicago", "state": "IL"},
    {"name": "Premier Homes Realty", "industry": "REAL_ESTATE", "annualrevenue": "650000", "numberofemployees": "5", "city": "Austin", "state": "TX"},
    {"name": "Elite Property Group", "industry": "REAL_ESTATE", "annualrevenue": "2100000", "numberofemployees": "18", "city": "Los Angeles", "state": "CA"},
    {"name": "Landmark Real Estate", "industry": "REAL_ESTATE", "annualrevenue": "950000", "numberofemployees": "9", "city": "Atlanta", "state": "GA"},
]

# Hans Stewart - Fitness & Wellness Clients (Nationwide)
FITNESS_COMPANIES = [
    {"name": "Iron & Soul Fitness Studio", "annualrevenue": "380000", "numberofemployees": "6", "city": "Nashville", "state": "TN"},
    {"name": "Bloom Wellness Collective", "annualrevenue": "290000", "numberofemployees": "4", "city": "Denver", "state": "CO"},
    {"name": "Peak Performance Training", "annualrevenue": "520000", "numberofemployees": "8", "city": "Phoenix", "state": "AZ"},
    {"name": "Zen Flow Yoga & Wellness", "annualrevenue": "210000", "numberofemployees": "3", "city": "Portland", "state": "OR"},
    {"name": "Elevate Fitness Collective", "annualrevenue": "450000", "numberofemployees": "7", "city": "Charlotte", "state": "NC"},
]

ALL_COMPANIES = REAL_ESTATE_COMPANIES + FITNESS_COMPANIES

# Real Estate Agent Contacts (Nationwide)
REAL_ESTATE_CONTACTS = [
    {"firstname": "Marcus", "lastname": "Williams", "email": "marcus@coastalrealtygroup.com", "jobtitle": "Founder & Lead Agent", "phone": "904-555-0101", "company": "Coastal Realty Group", "hs_lead_status": "IN_PROGRESS"},
    {"firstname": "Brittany", "lastname": "Hayes", "email": "brittany@skylineproperties.com", "jobtitle": "Broker/Owner", "phone": "312-555-0102", "company": "Skyline Properties", "hs_lead_status": "NEW"},
    {"firstname": "Jordan", "lastname": "Mitchell", "email": "jordan@premierhomes.com", "jobtitle": "Independent Realtor", "phone": "512-555-0103", "company": "Premier Homes Realty", "hs_lead_status": "OPEN"},
    {"firstname": "Tanya", "lastname": "Brooks", "email": "tanya@elitepropertygroup.com", "jobtitle": "Team Lead Agent", "phone": "310-555-0104", "company": "Elite Property Group", "hs_lead_status": "IN_PROGRESS"},
    {"firstname": "Derek", "lastname": "Simmons", "email": "derek@landmarkrealestate.com", "jobtitle": "Realtor & Business Owner", "phone": "404-555-0105", "company": "Landmark Real Estate", "hs_lead_status": "NEW"},
    {"firstname": "Camille", "lastname": "Foster", "email": "camille@coastalrealtygroup.com", "jobtitle": "Luxury Property Specialist", "phone": "904-555-0106", "company": "Coastal Realty Group", "hs_lead_status": "OPEN"},
    {"firstname": "Andre", "lastname": "Washington", "email": "andre@elitepropertygroup.com", "jobtitle": "Commercial Real Estate Agent", "phone": "310-555-0107", "company": "Elite Property Group", "hs_lead_status": "IN_PROGRESS"},
    {"firstname": "Natasha", "lastname": "Coleman", "email": "natasha@skylineproperties.com", "jobtitle": "Residential Sales Agent", "phone": "312-555-0108", "company": "Skyline Properties", "hs_lead_status": "NEW"},
    {"firstname": "Tyler", "lastname": "Grant", "email": "tyler@premierhomes.com", "jobtitle": "Buyer's Agent", "phone": "512-555-0109", "company": "Premier Homes Realty", "hs_lead_status": "OPEN"},
    {"firstname": "Jasmine", "lastname": "Reed", "email": "jasmine@landmarkrealestate.com", "jobtitle": "Realtor", "phone": "404-555-0110", "company": "Landmark Real Estate", "hs_lead_status": "NEW"},
]

# Fitness & Wellness Contacts (Nationwide)
FITNESS_CONTACTS = [
    {"firstname": "Alexis", "lastname": "Turner", "email": "alexis@ironandsoul.com", "jobtitle": "Owner & Head Coach", "phone": "615-555-0111", "company": "Iron & Soul Fitness Studio", "hs_lead_status": "IN_PROGRESS"},
    {"firstname": "Dominique", "lastname": "Price", "email": "dominique@bloomwellness.com", "jobtitle": "Founder & Wellness Coach", "phone": "720-555-0112", "company": "Bloom Wellness Collective", "hs_lead_status": "NEW"},
    {"firstname": "Marcus", "lastname": "Johnson", "email": "marcus@peakperformance.com", "jobtitle": "CEO & Head Trainer", "phone": "602-555-0113", "company": "Peak Performance Training", "hs_lead_status": "OPEN"},
    {"firstname": "Serena", "lastname": "Patel", "email": "serena@zenflow.com", "jobtitle": "Studio Owner & Yoga Instructor", "phone": "503-555-0114", "company": "Zen Flow Yoga & Wellness", "hs_lead_status": "IN_PROGRESS"},
    {"firstname": "Brandon", "lastname": "King", "email": "brandon@elevatefitness.com", "jobtitle": "Founder & Performance Coach", "phone": "704-555-0115", "company": "Elevate Fitness Collective", "hs_lead_status": "NEW"},
    {"firstname": "Monique", "lastname": "Davis", "email": "monique@ironandsoul.com", "jobtitle": "Studio Manager", "phone": "615-555-0116", "company": "Iron & Soul Fitness Studio", "hs_lead_status": "OPEN"},
    {"firstname": "Terrence", "lastname": "Hill", "email": "terrence@peakperformance.com", "jobtitle": "Business Development Manager", "phone": "602-555-0117", "company": "Peak Performance Training", "hs_lead_status": "IN_PROGRESS"},
    {"firstname": "Priya", "lastname": "Sharma", "email": "priya@bloomwellness.com", "jobtitle": "Holistic Health Coach", "phone": "720-555-0118", "company": "Bloom Wellness Collective", "hs_lead_status": "NEW"},
    {"firstname": "Darius", "lastname": "Evans", "email": "darius@elevatefitness.com", "jobtitle": "Head of Operations", "phone": "704-555-0119", "company": "Elevate Fitness Collective", "hs_lead_status": "OPEN"},
    {"firstname": "Keisha", "lastname": "Morgan", "email": "keisha@zenflow.com", "jobtitle": "Co-Owner & Pilates Instructor", "phone": "503-555-0120", "company": "Zen Flow Yoga & Wellness", "hs_lead_status": "IN_PROGRESS"},
]

ALL_CONTACTS = REAL_ESTATE_CONTACTS + FITNESS_CONTACTS

# Hans Stewart - Service Deals
DEALS = [
    # Real Estate Deals
    {"dealname": "Coastal Realty - AI Marketing Automation Setup", "amount": "3500", "dealstage": "qualifiedtobuy", "closedate": "2026-04-30"},
    {"dealname": "Skyline Properties - CRM Strategy & HubSpot Onboarding", "amount": "2800", "dealstage": "appointmentscheduled", "closedate": "2026-05-15"},
    {"dealname": "Premier Homes - Lead Generation System", "amount": "1800", "dealstage": "presentationscheduled", "closedate": "2026-05-30"},
    {"dealname": "Elite Property Group - Full Marketing Suite", "amount": "5500", "dealstage": "contractsent", "closedate": "2026-04-20"},
    {"dealname": "Landmark Real Estate - Social Media AI Strategy", "amount": "2200", "dealstage": "qualifiedtobuy", "closedate": "2026-05-01"},
    # Fitness & Wellness Deals
    {"dealname": "Iron & Soul - Client Retention Automation", "amount": "2400", "dealstage": "decisionmakerboughtin", "closedate": "2026-04-25"},
    {"dealname": "Bloom Wellness - Email Marketing & CRM Setup", "amount": "1900", "dealstage": "appointmentscheduled", "closedate": "2026-05-20"},
    {"dealname": "Peak Performance - Full Growth Strategy Package", "amount": "4200", "dealstage": "qualifiedtobuy", "closedate": "2026-05-10"},
    {"dealname": "Zen Flow - Membership Growth Campaign", "amount": "1600", "dealstage": "presentationscheduled", "closedate": "2026-06-01"},
    {"dealname": "Elevate Fitness - AI-Powered Lead Nurturing", "amount": "2900", "dealstage": "contractsent", "closedate": "2026-04-22"},
]

def create_company(company_data):
    # Check if company already exists
    check = requests.post(
        f"{BASE_URL}/crm/v3/objects/companies/search",
        headers=HEADERS,
        json={
            "filterGroups": [{
                "filters": [{
                    "propertyName": "name",
                    "operator": "EQ",
                    "value": company_data.get("name", "")
                }]
            }]
        }
    )
    if check.status_code == 200 and check.json().get("total", 0) > 0:
        print(f"  ℹ️ Already exists: {company_data.get('name')}")
        return check.json()["results"][0]["id"]

    response = requests.post(
        f"{BASE_URL}/crm/v3/objects/companies",
        headers=HEADERS,
        json={"properties": company_data}
    )
    if response.status_code == 201:
        return response.json()['id']
    else:
        print(f"  ⚠️ Company error: {response.text[:100]}")
        return None

def create_contact(contact_data):
    # First check if contact already exists
    check = requests.get(
        f"{BASE_URL}/crm/v3/objects/contacts/search",
        headers=HEADERS,
        json={
            "filterGroups": [{
                "filters": [{
                    "propertyName": "email",
                    "operator": "EQ",
                    "value": contact_data.get("email", "")
                }]
            }]
        }
    )
    if check.status_code == 200 and check.json().get("total", 0) > 0:
        print(f"  ℹ️ Already exists: {contact_data.get('firstname')} {contact_data.get('lastname')}")
        return check.json()["results"][0]["id"]

    response = requests.post(
        f"{BASE_URL}/crm/v3/objects/contacts",
        headers=HEADERS,
        json={"properties": contact_data}
    )
    if response.status_code == 201:
        return response.json()['id']
    else:
        print(f"  ⚠️ Contact error: {response.text[:100]}")
        return None

def create_deal(deal_data):
    response = requests.post(
        f"{BASE_URL}/crm/v3/objects/deals",
        headers=HEADERS,
        json={"properties": deal_data}
    )
    if response.status_code == 201:
        return response.json()['id']
    else:
        print(f"  ⚠️ Deal error: {response.text[:100]}")
        return None

def main():
    print("🚀 Populating HubSpot CRM for Hans Stewart...\n")
    print("📋 Client Types: Real Estate Agents + Fitness & Wellness Entrepreneurs")
    print("🌎 Locations: Nationwide across the US\n")

    # Create companies
    print("🏢 Creating client companies...")
    print("   --- Real Estate (Nationwide) ---")
    company_ids = []
    for company in REAL_ESTATE_COMPANIES:
        cid = create_company(company)
        if cid:
            company_ids.append(cid)
            print(f"  ✅ {company['name']} — {company['city']}, {company['state']}")
        time.sleep(0.3)

    print("   --- Fitness & Wellness (Nationwide) ---")
    for company in FITNESS_COMPANIES:
        cid = create_company(company)
        if cid:
            company_ids.append(cid)
            print(f"  ✅ {company['name']} — {company['city']}, {company['state']}")
        time.sleep(0.3)

    # Create contacts
    print(f"\n👥 Creating contacts...")
    print("   --- Real Estate Agents ---")
    contact_ids = []
    for contact in REAL_ESTATE_CONTACTS:
        cid = create_contact(contact)
        if cid:
            contact_ids.append(cid)
            print(f"  ✅ {contact['firstname']} {contact['lastname']} — {contact['jobtitle']}")
        time.sleep(0.3)

    print("   --- Fitness & Wellness Owners ---")
    for contact in FITNESS_CONTACTS:
        cid = create_contact(contact)
        if cid:
            contact_ids.append(cid)
            print(f"  ✅ {contact['firstname']} {contact['lastname']} — {contact['jobtitle']}")
        time.sleep(0.3)

    # Create deals
    print(f"\n💰 Creating service deals...")
    deal_ids = []
    for deal in DEALS:
        did = create_deal(deal)
        if did:
            deal_ids.append(did)
            print(f"  ✅ {deal['dealname']} — ${deal['amount']}")
        time.sleep(0.3)

    print(f"\n🎉 Hans Stewart HubSpot CRM populated successfully!")
    print(f"   ✅ Companies created: {len(company_ids)}/10")
    print(f"   ✅ Contacts created: {len(contact_ids)}/20")
    print(f"   ✅ Deals created: {len(deal_ids)}/10")
    print(f"\n🌐 View your CRM: https://app.hubspot.com")
    print(f"\n📍 Cities covered:")
    print(f"   Jacksonville FL | Chicago IL | Austin TX | Los Angeles CA | Atlanta GA")
    print(f"   Nashville TN | Denver CO | Phoenix AZ | Portland OR | Charlotte NC")

if __name__ == "__main__":
    main()