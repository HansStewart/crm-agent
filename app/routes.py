from flask import Blueprint, request, jsonify
from app.crm_agent import (
    analyze_contact, score_all_contacts,
    generate_pipeline_report, generate_email_sequence
)
from app.hubspot_client import (
    get_all_contacts, get_all_deals,
    get_all_companies, get_contact_by_id,
    get_pipeline_summary
)

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Hans Stewart — AI CRM Automation Agent",
        "status": "healthy",
        "powered_by": "HubSpot CRM + OpenAI GPT-4o",
        "endpoints": {
            "GET  /contacts": "All contacts ranked by AI score",
            "GET  /contacts/<id>/analyze": "Deep AI analysis of one contact",
            "GET  /contacts/<id>/email-sequence": "Generate email sequence",
            "GET  /pipeline/report": "Full AI pipeline report",
            "GET  /pipeline/summary": "Quick pipeline stats",
            "GET  /companies": "All companies"
        }
    })

@main.route('/contacts', methods=['GET'])
def get_contacts():
    """Get all HubSpot contacts ranked by AI score"""
    contacts = get_all_contacts()
    scored = score_all_contacts(contacts)
    return jsonify({
        "status": "success",
        "source": "HubSpot CRM (Live Data)",
        "total_contacts": len(scored),
        "contacts": scored
    })

@main.route('/contacts/<contact_id>/analyze', methods=['GET'])
def analyze_single_contact(contact_id):
    """Deep AI analysis of a single contact"""
    contact = get_contact_by_id(contact_id)
    if not contact:
        return jsonify({"error": "Contact not found"}), 404
    try:
        result = analyze_contact(contact)
        return jsonify({"status": "success", **result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@main.route('/contacts/<contact_id>/email-sequence', methods=['GET'])
def get_email_sequence(contact_id):
    """Generate personalized email sequence"""
    contact = get_contact_by_id(contact_id)
    if not contact:
        return jsonify({"error": "Contact not found"}), 404
    try:
        result = generate_email_sequence(contact)
        return jsonify({"status": "success", **result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@main.route('/pipeline/report', methods=['GET'])
def pipeline_report():
    """Full AI-powered pipeline report"""
    try:
        contacts = get_all_contacts()
        deals_summary = get_pipeline_summary()
        result = generate_pipeline_report(contacts, deals_summary)
        return jsonify({"status": "success", **result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@main.route('/pipeline/summary', methods=['GET'])
def pipeline_summary():
    """Quick pipeline summary"""
    summary = get_pipeline_summary()
    return jsonify({"status": "success", **summary})

@main.route('/companies', methods=['GET'])
def get_companies():
    """Get all HubSpot companies"""
    companies = get_all_companies()
    return jsonify({
        "status": "success",
        "source": "HubSpot CRM (Live Data)",
        "total_companies": len(companies),
        "companies": companies
    })