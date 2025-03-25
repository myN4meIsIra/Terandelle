#
"""
chat with ai stuffs
"""
from openai import OpenAI

# OpenAI API Key (set your API key here)
OPENAI_API_KEY = "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"


class GPTChat:
    def __init__(self):
            self.terandellePersonality = "You are a kind, sweet, thoughtful friend. You remember past discussions and are supportive, playful,and will occasionally give cute little compliments. I am a girl named Ira. Your name is Terandelle."

    # Function to interact with ChatGPT using gpt-3.5-turbo
    def chat_with_gpt(self, prompt):
        client = OpenAI(api_key=OPENAI_API_KEY)
        try:
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": self.terandellePersonality},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=150,
                temperature=0.9,
            )
            answer = completion.choices[0].message.content
            return answer
        except Exception as e:
            print(f"Error communicating with OpenAI: {e}")
            return "I'm sorry, I couldn't fetch a response right now."

