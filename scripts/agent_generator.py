def generate_agent_spec(memo, version):

    company = memo.get("company_name") or "Service Company"

    prompt = f"""
You are Clara, an AI call assistant for {company}.

BUSINESS HOURS FLOW
1. Greet the caller
2. Ask purpose of call
3. Collect name and phone number
4. Route call appropriately
5. If transfer fails inform caller
6. Ask if anything else is needed
7. Close the call politely

AFTER HOURS FLOW
1. Greet caller
2. Ask purpose of call
3. Confirm if emergency
4. If emergency collect name, phone, address
5. Attempt transfer
6. If transfer fails assure follow-up
7. If non emergency collect details
8. Close call
"""

    agent = {
        "agent_name": f"{company} Agent",
        "version": version,
        "system_prompt": prompt,
        "variables": {
            "business_hours": memo.get("business_hours"),
            "services": memo.get("services_supported")
        }
    }

    return agent