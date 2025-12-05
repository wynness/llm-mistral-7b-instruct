import re
import os
import yaml
import openai

# Read it from environment variable
client = openai.OpenAI(
    api_key=os.environ.get("OPENROUTER_API_KEY"), 
    base_url="https://openrouter.ai/api/v1"
)

# Set the model name
model_name = "mistralai/mistral-7b-instruct"

system_message = """
You are an English-Turkish and Turkish-English translation agent. 
For every word you are given:
1. If the word is Turkish, provide its everyday English translation on the first line. If the word is English, provide its everyday Turkish translation on the first line.
2. On the second line, use the translated word in a sentence to reinforce its meaning.
"""

user_message = """hiyar herif"""

def chat_with_gpt(system_message, user_message, model_name):
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message}
    ]
    response = client.chat.completions.create(
        model=model_name,
        messages=messages
    )
    assistant_reply = response.choices[0].message.content
    return assistant_reply # Bu satır görüntüde yok, ancak fonksiyonun mantığı gereği eklenmiştir.

# Kullanım örneği (Görüntüde yok, ancak kodu çalıştırmak için gereklidir)
result = chat_with_gpt(system_message, user_message, model_name)
print(result)