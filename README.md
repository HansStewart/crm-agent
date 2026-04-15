# CRM Automation Agent

> A lead-scoring and CRM workflow service that evaluates contact quality, writes back structured updates, and supports automated sales follow-up logic inside HubSpot.

**by Hans Stewart &nbsp;·&nbsp; [hansstewart.dev](https://hansstewart.dev)**

[Architecture](https://hansstewart.github.io/ai-architecture) &nbsp;·&nbsp; [Portfolio](https://hansstewart.dev) &nbsp;·&nbsp; [GitHub](https://github.com/HansStewart/crm-agent)

---

## What It Does

Receives lead and contact records from CRM-connected systems or workflow triggers, uses GPT-4o to assess fit, intent, and likelihood of sales progress, translates that evaluation into a structured scoring layer, and writes the result back into HubSpot — updating scores, fields, follow-up metadata, and triggering downstream workflows.

**Primary benefit:** automated lead triage without forcing sales reps to manually assess every incoming record.  
**Operational role:** bridges AI evaluation and CRM-native workflow execution.  
**Use cases:** lead routing, prioritization, enrichment, and nurture automation.

---

## Backend Workflow

**Step 1 — Record intake** `Input: Lead and contact records`
Pulls or receives contact and lead records requiring evaluation. Loads profile attributes, engagement data, and business context. Builds the scoring input object for AI-assisted prioritization.

**Step 2 — Lead evaluation** `Intermediate: Score + action recommendation`
Uses GPT-4o to assess fit, intent, and likelihood of sales progress. Translates contextual signals into a structured scoring layer. Determines whether the lead should be prioritized, nurtured, or routed differently.

**Step 3 — Automation actioning** `Processing: Scoring → CRM workflow logic`
Triggers updates, flags, and downstream follow-up workflows. Supports CRM enrichment and automated sales operations. Ensures output can be consumed by human reps or workflow engines.

**Step 4 — CRM writeback** `Output: CRM updates + score state`
Updates scores, fields, and follow-up metadata on the HubSpot record. Keeps the CRM as the source of truth for sales execution. Returns a structured result confirming what changed.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11 |
| Framework | Flask |
| Server | Gunicorn |
| AI Model | OpenAI GPT-4o |
| CRM | HubSpot API |
| Deployment | Google Cloud Run — us-east1 |

---

## Local Development

```bash
git clone https://github.com/HansStewart/crm-agent.git
cd crm-agent
pip install -r requirements.txt
cp .env.example .env
# Add OPENAI_API_KEY and HUBSPOT_API_KEY to .env
python main.py
```

---

## Environment Variables

| Variable | Required | Purpose |
|---|---|---|
| `OPENAI_API_KEY` | Yes | Lead evaluation and scoring logic |
| `HUBSPOT_API_KEY` | Yes | CRM record read and write access |

---

## Full Agent Ecosystem

| Agent | Repository |
|---|---|
| Website Audit Agent | [github.com/HansStewart/website-audit-agent](https://github.com/HansStewart/website-audit-agent) |
| AI Content Pipeline | [github.com/HansStewart/ai-content-pipeline](https://github.com/HansStewart/ai-content-pipeline) |
| Voice-to-CRM Agent | [github.com/HansStewart/voice-to-crm](https://github.com/HansStewart/voice-to-crm) |
| Pipeline Intelligence Agent | [github.com/HansStewart/pipeline-intelligence-agent](https://github.com/HansStewart/pipeline-intelligence-agent) |
| Multi-Agent BI System | [github.com/HansStewart/multi-agent](https://github.com/HansStewart/multi-agent) |
| AI Data Agent | [github.com/HansStewart/ai-data-agent](https://github.com/HansStewart/ai-data-agent) |
| RAG Document Intelligence | [github.com/HansStewart/rag-agent](https://github.com/HansStewart/rag-agent) |
| AI Architecture | [hansstewart.github.io/ai-architecture](https://hansstewart.github.io/ai-architecture) |

---

**Hans Stewart &nbsp;·&nbsp; Marketing Automation Engineer &nbsp;·&nbsp; [hansstewart.dev](https://hansstewart.dev)**
