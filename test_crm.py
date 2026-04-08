import requests
import json

BASE_URL = "http://localhost:8080"

print("🚀 Testing Hans Stewart AI CRM Agent\n")
print("=" * 50)

# Test 1: Health check
print("\n✅ Test 1: Health Check")
r = requests.get(f"{BASE_URL}/")
print(f"Status: {r.json()['status']}")
print(f"Message: {r.json()['message']}")

# Test 2: Get all contacts ranked
print("\n✅ Test 2: All Contacts (AI Ranked)")
r = requests.get(f"{BASE_URL}/contacts")
data = r.json()
print(f"Source: {data['source']}")
print(f"Total Contacts: {data['total_contacts']}")
print("\nTop 5 Ranked Contacts:")
for c in data['contacts'][:5]:
    print(f"  {c['priority']} {c['name']} ({c['company']}) - Score: {c['ai_score']}/100")

# Test 3: Get companies
print("\n✅ Test 3: Companies")
r = requests.get(f"{BASE_URL}/companies")
data = r.json()
print(f"Total Companies: {data['total_companies']}")

# Test 4: Pipeline summary
print("\n✅ Test 4: Pipeline Summary")
r = requests.get(f"{BASE_URL}/pipeline/summary")
data = r.json()
print(f"Total Deals: {data['total_deals']}")
print(f"Total Pipeline Value: ${data['total_pipeline_value']:,.2f}")
print("By Stage:")
for stage, info in data['by_stage'].items():
    print(f"  {stage}: {info['count']} deals — ${info['value']:,.2f}")

# Test 5: Analyze top contact
print("\n✅ Test 5: AI Analysis of Top Contact")
r = requests.get(f"{BASE_URL}/contacts")
top_id = r.json()['contacts'][0]['id']
r = requests.get(f"{BASE_URL}/contacts/{top_id}/analyze")
result = r.json()
print(f"Contact: {result['name']}")
print(f"Company: {result['company']}")
print(f"Score: {result['ai_score']}/100 — {result['priority']}")
print(f"Analysis Preview:\n{result['ai_analysis'][:400]}...")

# Test 6: Generate email sequence
print("\n✅ Test 6: Email Sequence Generation")
r = requests.get(f"{BASE_URL}/contacts/{top_id}/email-sequence")
result = r.json()
print(f"Sequence for: {result['contact_name']}")
print(f"Industry: {result['industry']}")
print(f"Preview:\n{result['email_sequence'][:300]}...")

# Test 7: Full pipeline report
print("\n✅ Test 7: Full AI Pipeline Report")
r = requests.get(f"{BASE_URL}/pipeline/report")
result = r.json()
print(f"Total Contacts: {result['total_contacts']}")
print(f"Hot Leads: {len(result['hot_leads'])}")
print(f"Cold Leads: {len(result['cold_leads'])}")
print(f"Top Contact: {result['top_contact']['name']} - Score: {result['top_contact']['ai_score']}/100")
print(f"\nAI Report Preview:\n{result['ai_report'][:400]}...")

print("\n" + "=" * 50)
print("🎉 All tests complete!")
print("=" * 50)