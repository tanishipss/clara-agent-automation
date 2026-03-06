def generate_memo(account_id, extracted):

    memo = {
        "account_id": account_id,
        "company_name": extracted.get("company_name"),
        "business_hours": extracted.get("business_hours"),
        "office_address": None,
        "services_supported": extracted.get("services_supported", []),
        "emergency_definition": extracted.get("emergency_definition", []),
        "emergency_routing_rules": None,
        "non_emergency_routing_rules": None,
        "call_transfer_rules": None,
        "integration_constraints": [],
        "after_hours_flow_summary": "",
        "office_hours_flow_summary": "",
        "questions_or_unknowns": extracted.get("questions_or_unknowns", []),
        "notes": ""
    }

    return memo