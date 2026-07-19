# schema.py

OUTPUT_SCHEMA = {
    "weekly_summary": [
        "string"
    ],
    "nutrition": {
        "status": "string",
        "details": "string",
        "classification": "Confirmed Fact | Client-Reported Information | AI-Generated Inference | Missing / Unavailable Information",
        "evidence": [
            "string"
        ]
    },
    "sleep": {
        "status": "string",
        "details": "string",
        "classification": "Confirmed Fact | Client-Reported Information | AI-Generated Inference | Missing / Unavailable Information",
        "evidence": [
            "string"
        ]
    },
    "exercise": {
        "status": "string",
        "details": "string",
        "classification": "Confirmed Fact | Client-Reported Information | AI-Generated Inference | Missing / Unavailable Information",
        "evidence": [
            "string"
        ]
    },
    "water": {
        "status": "string",
        "details": "string",
        "classification": "Confirmed Fact | Client-Reported Information | AI-Generated Inference | Missing / Unavailable Information",
        "evidence": [
            "string"
        ]
    },
    "stress": {
        "status": "string",
        "details": "string",
        "classification": "Confirmed Fact | Client-Reported Information | AI-Generated Inference | Missing / Unavailable Information",
        "evidence": [
            "string"
        ]
    },
    "symptoms": [
        {
            "name": "string",
            "classification": "Confirmed Fact | Client-Reported Information | AI-Generated Inference | Missing / Unavailable Information",
            "evidence": "string"
        }
    ],
    "engagement_level": {
        "status": "string",
        "classification": "AI-Generated Inference",
        "evidence": [
            "string"
        ]
    },
    "key_barriers": [
        {
            "barrier": "string",
            "classification": "AI-Generated Inference",
            "evidence": "string"
        }
    ],
    "risk_flags": [
        "string"
    ],
    "pending_actions": [
        "string"
    ],
    "coach_recommendation": "string"
}