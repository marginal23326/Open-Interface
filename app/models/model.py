import os
from typing import Any

from google.genai import types


class Model:
    def __init__(self, model_name, api_key, context):
        self.model_name = model_name
        self.api_key = api_key
        self.context = context
        if api_key:
            os.environ["GOOGLE_API_KEY"] = api_key

    def get_instructions_for_objective(self, *args) -> dict[str, Any]:
        pass

    def format_user_request_for_llm(self, *args):
        pass

    def send_message_to_llm(self, model, contents, stream=False, safety_settings=None):
        config = {}
        if safety_settings:
            config["safety_settings"] = safety_settings
        gen_config = types.GenerateContentConfig(**config) if config else None

        response = self.client.models.generate_content(
            model=model,
            contents=contents,
            config=gen_config,
        )
        return response

    def cleanup(self, *args):
        pass
