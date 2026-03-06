def detect_missing_fields(memo):

    missing = []

    if not memo.get("business_hours"):
        missing.append("business hours not specified")

    if not memo.get("services_supported"):
        missing.append("services not specified")

    if not memo.get("emergency_definition"):
        missing.append("emergency definition unclear")

    return missing