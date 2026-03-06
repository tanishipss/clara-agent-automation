def generate_agent_spec(memo, version):

    agent = {
        "agent_name": "Service Company Agent",
        "version": version,
        "company_name": memo.get("company_name"),
        "services_supported": memo.get("services_supported", []),
        "business_hours": memo.get("business_hours"),
        "emergency_definition": memo.get("emergency_definition"),
        "integration_constraints": memo.get("integration_constraints", []),
        "questions_or_unknowns": memo.get("questions_or_unknowns", [])
    }

    return agent