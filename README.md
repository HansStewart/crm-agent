# 🤖 AI-Powered CRM Automation Agent

A production-ready AI agent that connects to HubSpot CRM, scores leads using 
a custom AI scoring engine, and generates actionable insights and personalized 
email sequences using OpenAI GPT-4o.

## 🌐 Live API
https://crm-agent-xxxxxxxx-ue.a.run.app (update after deployment)

## 🛠️ Tech Stack
- Python 3.14 — Core language
- Flask — REST API framework
- OpenAI GPT-4o — AI analysis engine
- HubSpot CRM API — Live CRM data source
- Pandas — Data processing
- GCP Cloud Run — Cloud deployment

## 🚀 Features
- Live HubSpot CRM integration via Private Apps API
- AI-powered lead scoring engine (0-100 score)
- Priority ranking (HOT/WARM/COOL/COLD)
- Deep AI analysis of individual contacts
- Personalized 3-email sequence generation
- Full pipeline report with revenue forecast
- Real estate and fitness/wellness industry focus

## 📦 Installation

1. Clone the repository
git clone https://github.com/HansStewart/crm-agent.git
cd crm-agent

2. Create virtual environment
python -m venv venv
venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Add your API keys to .env
OPENAI_API_KEY=your_openai_key
HUBSPOT_API_KEY=your_hubspot_key

5. Populate HubSpot with sample data
python populate_hubspot.py

6. Run the app
python main.py

## 🧪 API Endpoints

GET  /                              - Health check
GET  /contacts                      - All contacts ranked by AI score
GET  /contacts/<id>/analyze         - Deep AI analysis of one contact
GET  /contacts/<id>/email-sequence  - Generate personalized email sequence
GET  /pipeline/report               - Full AI pipeline report
GET  /pipeline/summary              - Quick pipeline stats
GET  /companies                     - All HubSpot companies

## 💡 How It Works
HubSpot CRM (Live Data) → AI Lead Scoring Engine →
GPT-4o Analysis → Ranked Insights + Email Sequences + Pipeline Report

## 🏗️ Project Structure
crm-agent/
├── app/
│   ├── __init__.py          - Flask app factory
│   ├── routes.py            - API endpoints
│   ├── crm_agent.py         - OpenAI GPT-4o integration
│   ├── lead_scorer.py       - Custom lead scoring engine
│   └── hubspot_client.py    - HubSpot API client
├── main.py                  - Entry point
├── populate_hubspot.py      - HubSpot data population script
├── test_crm.py              - API test suite
├── requirements.txt         - Dependencies
├── Dockerfile               - Container config
└── README.md                - Documentation

## 👤 Author
Hans Stewart
GitHub: https://github.com/HansStewart