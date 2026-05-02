import os, openai
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv('.env')

openai.api_key = os.environ['OPENAI_API_KEY']

client = OpenAI()

input_text = input("Enter text: ")
data = {"name": "Giovanni", "age": 30, "city": "Roma", "profession": "Ingegnere"}

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Sei un assistente che trasforma dati strutturati in descrizioni testuali fluide e naturali. Riceverai un dizionario Python e dovrai scrivere un paragrafo descrittivo che includa tutte le informazioni contenute nei dati."},
        {"role": "user", "content": input_text + "\n" + str(data)},
    ],
)

print(completion.choices[0].message.content)