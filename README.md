# 🎯 CRM Automation Agent

     

An AI-powered CRM automation agent with live HubSpot integration. Scores leads using a deterministic multi-dimensional engine, analyzes contacts with GPT-4o, generates personalized 3-email outreach sequences, and produces full pipeline revenue forecasts.

**Live API:** `https://crm-agent-559169459241.us-east1.run.app`

***

## Architecture

```
HubSpot CRM (Private Apps API)
        │
        ▼
┌─────────────────────────────────┐
│       Lead Scoring Engine       │
│  job title  · 0–25 pts          │
│  lead status · 0–30 pts         │
│  email present · 15 pts         │
│  phone present · 15 pts         │
│  company assoc · 15 pts         │
│  ─────────────────────          │
│  Total: 0–100 · HOT/WARM/COOL   │
└─────────────┬───────────────────┘
              │  scored + sorted contacts
              ▼
┌─────────────────────────────────┐
│         OpenAI GPT-4o           │
│  contact analysis               │
│  email sequence generation      │
│  pipeline revenue forecast      │
└─────────────┬───────────────────┘
              │
              ▼
     JSON · scored leads · email sequences · pipeline report
```

***

## Tech Stack

| Layer | Technology |
|---|---|
| Runtime | Python 3.11 |
| Web Framework | Flask 3.0 + Gunicorn |
| CRM Integration | HubSpot Private Apps API |
| Scoring Engine | Custom rule-based (0–100 pts) |
| AI / LLM | OpenAI GPT-4o |
| Containerization | Docker (python:3.11-slim) |
| Cloud | Google Cloud Run — us-east1 |

***

## Lead Scoring Engine

The scoring engine evaluates every contact across 5 dimensions and returns a priority tier:

| Dimension | Signal | Points |
|---|---|---|
| **Job Title** | Owner / Founder / Broker / CEO / Director / Partner | 25 |
| **Job Title** | Manager / Agent / Realtor / Coach / Instructor | 15 |
| **Lead Status** | IN_PROGRESS | 30 |
| **Lead Status** | NEW | 20 |
| **Lead Status** | OPEN | 15 |
| **Lead Status** | CONNECTED | 10 |
| **Lead Status** | UNQUALIFIED | 2 |
| **Email** | Present | 15 |
| **Phone** | Present | 15 |
| **Company** | Associated | 15 |

**Priority Tiers:**
- 🔥 **HOT** — 75–100 pts
- ⚡ **WARM** — 50–74 pts
- ❄️ **COOL** — 25–49 pts
- 💤 **COLD** — 0–24 pts

***

## API Reference

### `GET /`
Health check.

### `GET /contacts`
Fetch all HubSpot contacts, score each one, and return sorted by score descending.

**Response:**
```json
{
  "contacts": [
    {
      "id": "101",
      "name": "Jane Smith",
      "title": "Real Estate Broker",
      "score": 85,
      "tier": "HOT 🔥",
      "email": "jane@example.com"
    }
  ],
  "total": 47
}
```

### `POST /analyze`
Run GPT-4o analysis on a single contact.

**Request:**
```json
{ "contact_id": "101" }
```

**Response:**
```json
{
  "lead_quality": "High-value prospect",
  "next_action": "Call within 24 hours",
  "outreach_message": "...",
  "follow_up_timing": "Same day",
  "talking_points": ["...", "...", "..."]
}
```

### `POST /email-sequence`
Generate a personalized 3-email outreach sequence for a contact.

**Request:**
```json
{ "contact_id": "101" }
```

**Response:**
```json
{
  "sequence": [
    { "email": 1, "subject": "...", "body": "...", "send_timing": "Day 1" },
    { "email": 2, "subject": "...", "body": "...", "send_timing": "Day 3" },
    { "email": 3, "subject": "...", "body": "...", "send_timing": "Day 7" }
  ]
}
```

### `GET /pipeline-summary`
Score all contacts and return tier breakdown counts.

### `POST /pipeline-report`
GPT-4o-generated full pipeline report using top 10 scored leads + deal data.

### `GET /companies`
Fetch all associated companies from HubSpot.

***

## How It Works

1. **Fetch** — `hubspot_client.py` pulls all contacts via HubSpot Private Apps API
2. **Score** — `lead_scorer.py` evaluates each contact across 5 dimensions and assigns 0–100 pts
3. **Sort** — Contacts are ranked descending by score and tagged with a priority tier
4. **Analyze** — GPT-4o receives a full contact summary and returns: lead quality assessment, recommended next action, personalized outreach message, follow-up timing, and talking points
5. **Generate** — GPT-4o writes a 3-email outreach sequence tailored to the contact's role and context
6. **Report** — Top 10 scored leads + deal pipeline data are sent to GPT-4o for a full revenue forecast and strategic summary

***

## Local Setup

```bash
git clone https://github.com/HansStewart/crm-agent.git
cd crm-agent
pip install -r requirements.txt
```

Create a `.env` file:
```
OPENAI_API_KEY=your_key_here
HUBSPOT_API_KEY=your_hubspot_private_app_token
```

Seed HubSpot with sample data (optional):
```bash
python populate_hubspot.py
```

Run the server:
```bash
python main.py
```

Test the API:
```bash
python test_crm.py
```

***

## Project Structure

```
crm-agent/
├── app/
│   ├── crm_agent.py       # GPT-4o analysis + email gen + pipeline report
│   ├── lead_scorer.py     # Rule-based scoring engine (0–100 pts)
│   ├── hubspot_client.py  # HubSpot API client
│   └── routes.py          # 7 Flask endpoints
├── main.py                # App entry point
├── populate_hubspot.py    # Demo data seeder
├── test_crm.py            # API test suite
├── Dockerfile
└── requirements.txt
```

***

## Deployment

```bash
gcloud run deploy crm-agent \
  --source . \
  --platform managed \
  --region us-east1 \
  --allow-unauthenticated \
  --set-env-vars OPENAI_API_KEY=...,HUBSPOT_API_KEY=...
```

***

## Part of the AI Agent Portfolio

| Agent | Description | Live URL |
|---|---|---|
| AI Data Agent | CSV analysis + GPT-4o insights | [↗](https://ai-data-agent-559169459241.us-east1.run.app) |
| RAG Document Intelligence | FAISS vector search + cited Q&A | [↗](https://rag-agent-559169459241.us-east1.run.app) |
| **CRM Automation Agent** | HubSpot + lead scoring + email gen | [↗](https://crm-agent-559169459241.us-east1.run.app) |
| Multi-Agent BI System | CrewAI 4-agent pipeline | [↗](https://multi-agent-559169459241.us-east1.run.app) |

**Author:** [Hans Stewart](https://github.com/HansStewart)