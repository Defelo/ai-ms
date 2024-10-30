import openai
from typing import Any


class AIHandler:
    def __init__(self, provider="openai", model_name="gpt-4o-2024-08-06") -> None:
        self.provider = provider
        self.model_name = model_name

    def get_ai_response(self, system_prompt: str, user_prompt: str) -> str:
        if self.provider == "openai":
            return self._call_openai(system_prompt, user_prompt)
        else:
            raise NotImplementedError(f"Provider '{self.provider}' is not supported.")

    def _call_openai(self, system_prompt: str, user_prompt: str) -> Any:
        response = openai.ChatCompletion.create(
            model=self.model_name,
            messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}],
        )
        return response.choices[0].message["content"]
