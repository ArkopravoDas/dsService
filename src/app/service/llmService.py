import os, json, requests, re

class LLMService:
    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        self.url = "https://openrouter.ai/api/v1/chat/completions"
        self.model = "mistralai/mistral-small-3.2-24b-instruct:free"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        self.system_prompt = (
            "You are an extraction API. Extract ONLY these fields from the SMS:\n"
            "- amount (number)\n- currency (3-letter code)\n- merchant (string)\n\n"
            "Return a STRICT JSON object with exactly these lowercase keys:\n"
            '{"amount": <number or null>, "merchant": <string or null>, "currency": <string or null>}\n'
            "If a field is unknown, use null. No explanations, no extra keys, no prose—only JSON."
        )

    def runLLM(self, message: str) -> dict:
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": self.system_prompt},
                {"role": "user",   "content": message},
            ],
            "temperature": 0,
            "response_format": {"type": "json_object"},  # keeps replies as JSON
        }
        resp = requests.post(self.url, headers=self.headers, data=json.dumps(payload), timeout=30)
        resp.raise_for_status()
        content = resp.json()["choices"][0]["message"]["content"]

        if content.startswith(""):
            content = re.sub(r"^(?:json)?\s*|\s*```$", "", content, flags=re.I|re.S).strip()

        return json.loads(content)