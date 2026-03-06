import re


def normalize(text):
    return text.lower()


def extract_services(text):

    services = []
    evidence = []

    service_patterns = {
        "sprinkler": "sprinkler service",
        "fire alarm": "fire alarm service",
        "inspection": "inspection service",
        "maintenance": "maintenance service"
    }

    for key, value in service_patterns.items():
        if key in text:
            services.append(value)
            evidence.append(key)

    return {
        "value": list(set(services)),
        "confidence": 0.9 if services else 0.0,
        "evidence": evidence
    }


def extract_business_hours(text):

    patterns = [
        r"(\d{1,2})\s?(?:am|pm)?\s*(?:to|-)\s*(\d{1,2})",
        r"open.*?(\d{1,2}).*?(?:to|-).*?(\d{1,2})"
    ]

    for pattern in patterns:
        match = re.search(pattern, text)

        if match:
            start = match.group(1)
            end = match.group(2)

            return {
                "value": f"{start}-{end}",
                "confidence": 0.8,
                "evidence": match.group(0)
            }

    return None


def extract_emergency(text):

    keywords = [
        "sprinkler leak",
        "water leak",
        "alarm going off"
    ]

    found = []

    for k in keywords:
        if k in text:
            found.append(k)

    if found:
        return {
            "value": found,
            "confidence": 0.85,
            "evidence": found
        }

    return None
# scripts/transcript_parser.py

def extract_business_hours(text):

    import re

    pattern = r"(\d{1,2})\s?(?:am|pm)?\s*(?:to|-)\s*(\d{1,2})"

    match = re.search(pattern, text)

    if match:

        evidence = match.group(0)

        return {
            "value": f"{match.group(1)}-{match.group(2)}",
            "confidence": 0.85,
            "evidence": evidence,
            "source": "rule"
        }

    return None