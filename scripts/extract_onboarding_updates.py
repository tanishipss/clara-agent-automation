from scripts.transcript_parser import (
    normalize,
    extract_business_hours,
    extract_emergency
)

from scripts.llm_extractor import llm_extract
from scripts.json_utils import safe_parse_json


def extract_onboarding_updates(transcript):

    text = normalize(transcript)

    updates = {}

    # -------------------------
    # BUSINESS HOURS
    # -------------------------

    hours = extract_business_hours(text)

    if hours:

        updates["business_hours"] = hours

    else:

        try:

            llm_output = llm_extract(transcript)

            data = safe_parse_json(llm_output)

            if "business_hours" in data:

                updates["business_hours"] = {
                    "value": data["business_hours"],
                    "confidence": 0.6,
                    "evidence": "llama extraction",
                    "source": "llm"
                }

        except Exception:
            pass

    # -------------------------
    # EMERGENCY
    # -------------------------

    emergency = extract_emergency(text)

    if emergency:

        updates["emergency_definition"] = emergency

    else:

        try:

            llm_output = llm_extract(transcript)

            data = safe_parse_json(llm_output)

            if "emergency_definition" in data:

                updates["emergency_definition"] = {
                    "value": data["emergency_definition"],
                    "confidence": 0.6,
                    "evidence": "llama extraction",
                    "source": "llm"
                }

        except Exception:
            pass

    # -------------------------
    # INTEGRATIONS
    # -------------------------

    integrations = []

    if "servicetrade" in text:
        integrations.append("ServiceTrade")

    if integrations:
        updates["integration_constraints"] = integrations

    return updates