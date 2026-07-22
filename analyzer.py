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

def analyze_conversation(conversation, max_retries=3):
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
            
            # Clean up potential markdown formatting from Gemini
            text = text.replace("```json", "")
            text = text.replace("```", "")
            text = text.strip()

            return json.loads(text)

        except BaseException as e:
            # BaseException catches absolutely every type of error, preventing crashes
            error_message = str(e)
            
            if attempt < max_retries - 1:
                # Wait 2 seconds before trying again
                time.sleep(2)
                continue
            else:
                # If we fail 3 times, return a safe dictionary instead of crashing
                return {"error": f"The AI service is currently experiencing high demand. Please try again in a few minutes."}