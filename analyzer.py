import json
import os

from dotenv import load_dotenv
from google import genai

from prompts import SYSTEM_PROMPT

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def analyze_conversation(conversation):

    prompt = f"""
{SYSTEM_PROMPT}

Conversation:

{conversation}

Return ONLY valid JSON.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    text = response.text.strip()

    # Remove markdown if Gemini returns it
    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    return json.loads(text)