import os, openai
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv('.env')

openai.api_key = os.environ['OPENAI_API_KEY']

client = OpenAI()

input_text = input("Scrivi qui: ")

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Sei un assistente che riassume articoli di notizie. Devi creare un riassunto in un singolo paragrafo di massimo 255 caratteri. Sii conciso e cattura solo i punti essenziali."},
        {"role": "user", "content": input_text},
    ],
)

print(completion.choices[0].message.content)