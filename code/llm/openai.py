from openai import OpenAI

from config import CONFIG


class OpenAIComponent:
    client = None

    def __init__(self):
        self.client = OpenAI(
            api_key=CONFIG["openai_api"]["api_key"]
        )

    # 调用openai并，生成响应
    async def generate_response(self, prompt: str, model='gpt-4o-mini'):
        try:
            client = self.client
            response = client.chat.completions.create(
                messages=[{
                    'role': 'user',
                    'content': prompt
                }],
                model=model
            )
            generated_text = response.choices[0].message.content.strip()
            return generated_text
        except Exception as e:
            raise e
