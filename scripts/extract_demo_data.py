from scripts.transcript_parser import (
    normalize,
    extract_services,
    extract_business_hours,
    extract_emergency
)

from scripts.llm_extractor import llm_extract
from scripts.json_utils import safe_parse_json


def extract_demo_data(transcript, account_id):

    text = normalize(transcript)

    memo = {
        "account_id": account_id,
        "services_supported": [],
        "business_hours": None,
        "emergency_definition": None,
        "integration_constraints": [],
        "questions_or_unknowns": [],
        "notes": ""
    }

    # -------------------------
    # SERVICES
    # -------------------------

    services = extract_services(text)

    if services["value"]:
        memo["services_supported"] = services["value"]

    else:

        try:

            llm_output = llm_extract(transcript)

            data = safe_parse_json(llm_output)

            memo["services_supported"] = data.get(
                "services_supported", []
            )

        except Exception:
            memo["questions_or_unknowns"].append(
                "services not specified"
            )

    # -------------------------
    # BUSINESS HOURS
    # -------------------------

    hours = extract_business_hours(text)

    if hours:

        memo["business_hours"] = hours

    else:

        try:

            llm_output = llm_extract(transcript)

            data = safe_parse_json(llm_output)

            if "business_hours" in data:

                memo["business_hours"] = {
                    "value": data["business_hours"],
                    "confidence": 0.6,
                    "evidence": "llama extraction",
                    "source": "llm"
                }

        except Exception:
            memo["questions_or_unknowns"].append(
                "business hours not specified"
            )

    # -------------------------
    # EMERGENCY
    # -------------------------

    emergency = extract_emergency(text)

    if emergency:

        memo["emergency_definition"] = emergency

    else:

        try:

            llm_output = llm_extract(transcript)

            data = safe_parse_json(llm_output)

            if "emergency_definition" in data:

                memo["emergency_definition"] = {
                    "value": data["emergency_definition"],
                    "confidence": 0.6,
                    "evidence": "llama extraction",
                    "source": "llm"
                }

        except Exception:
            memo["questions_or_unknowns"].append(
                "emergency definition unclear"
            )

    return memo