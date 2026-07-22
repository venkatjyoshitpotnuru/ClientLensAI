import json
import os
import time

from dotenv import load_dotenv
from google import genai

from prompts import SYSTEM_PROMPT

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def analyze_conversation(conversation, max_retries=3, backoff_factor=2):
    prompt = f"""
{SYSTEM_PROMPT}

Conversation:

{conversation}

Return ONLY valid JSON.
"""

    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model="gemini-3.5-flash",
                contents=prompt
            )

            text = response.text.strip()

            # Remove markdown if Gemini returns it
            text = text.replace("```json", "")
            text = text.replace("```", "")
            text = text.strip()

            return json.loads(text)

        except Exception as e:
            error_message = str(e)
            
            # Check if it is a 503 / UNAVAILABLE error
            if "503" in error_message or "UNAVAILABLE" in error_message:
                if attempt < max_retries - 1:
                    # Calculate wait time (e.g., 1s, 2s, 4s...)
                    sleep_time = backoff_factor ** attempt
                    print(f"Model overloaded. Retrying in {sleep_time} seconds... (Attempt {attempt + 1}/{max_retries})")
                    time.sleep(sleep_time)
                else:
                    # Max retries reached, return a safe error JSON
                    return {"error": "The AI service is currently experiencing high demand. Please try again later."}
            else:
                # For any other unexpected errors (e.g., API key issues, JSON parsing errors)
                return {"error": f"An unexpected error occurred: {error_message}"}