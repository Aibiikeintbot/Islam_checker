import os
import json
from core.helpers import get_score_color
from openai import OpenAI
from dotenv import load_dotenv
from .prompts import PROMPTS

load_dotenv()


class AICheckerService:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=self.api_key)

    def check_content(self, content_type: str, text: str):
        prompt = PROMPTS.get(content_type, "Проанализируй текст:")

        try:
            response = self.client.chat.completions.create(
                model="gpt-4-turbo-preview",
                messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": text}
                ],
                response_format={"type": "json_object"}
            )
            result = json.loads(response.choices[0].message.content)
            return result

        except Exception as e:
            print(f"Ошибка при запросе к OpenAI: {e}")
            return {"error": str(e), "score": 0}
