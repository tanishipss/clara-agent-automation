import requests
import json


def llm_extract(transcript):

    prompt = f"""
Extract structured information from the transcript.

Return JSON with fields:
services_supported
business_hours
emergency_definition
integration_constraints

Transcript:
{transcript}

Return ONLY JSON.
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()["response"]

    return result