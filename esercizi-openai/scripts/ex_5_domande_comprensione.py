import os, openai
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv('.env')

openai.api_key = os.environ['OPENAI_API_KEY']

client = OpenAI()

input_text = input("Enter text: ")

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Sei un assistente educativo. Dato un testo, genera 5 domande di comprensione che verifichino se il lettore ha capito i punti principali. Le domande devono essere chiare e pertinenti al contenuto del testo."},
        {"role": "user", "content": input_text},
    ],
)

print(completion.choices[0].message.content)