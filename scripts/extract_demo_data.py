from scripts.transcript_parser import (
    extract_services,
    extract_business_hours,
    extract_emergency
)

from scripts.missing_data_detector import detect_missing_fields


def extract_demo_data(transcript, account_id):
    """
    Extract structured configuration data from demo call transcript.
    """

    text = transcript.lower()

    memo = {
        "account_id": account_id,
        "company_name": None,
        "business_hours": None,
        "office_address": None,
        "services_supported": [],
        "emergency_definition": [],
        "emergency_routing_rules": None,
        "non_emergency_routing_rules": None,
        "call_transfer_rules": None,
        "integration_constraints": [],
        "after_hours_flow_summary": "",
        "office_hours_flow_summary": "",
        "questions_or_unknowns": [],
        "notes": ""
    }

    # --------------------------------------------------
    # Extract services
    # --------------------------------------------------

    services = extract_services(text)

    if services and services["value"]:
        memo["services_supported"] = services["value"]

    # --------------------------------------------------
    # Extract business hours
    # --------------------------------------------------

    hours = extract_business_hours(text)

    if hours:
        memo["business_hours"] = {
            "value": hours["value"],
            "confidence": hours["confidence"],
            "evidence": hours["evidence"]
        }

    # --------------------------------------------------
    # Extract emergency definitions
    # --------------------------------------------------

    emergency = extract_emergency(text)

    if emergency and emergency["value"]:
        memo["emergency_definition"] = emergency["value"]

    # --------------------------------------------------
    # Detect integration systems
    # --------------------------------------------------

    if "servicetrade" in text:
        memo["integration_constraints"].append("ServiceTrade")

    if "jobber" in text:
        memo["integration_constraints"].append("Jobber")

    # --------------------------------------------------
    # Missing data detection
    # --------------------------------------------------

    missing_fields = detect_missing_fields(memo)

    memo["questions_or_unknowns"] = missing_fields

    return memo