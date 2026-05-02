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
    {"role": "system", "content": "Sei un traduttore. Se il testo è in italiano, traducilo in inglese. Se il testo è in inglese, traducilo in italiano. Rispondi solo con la traduzione, senza aggiungere altro."},
    {"role": "user", "content": input_text},
],
)

print(completion.choices[0].message.content)

