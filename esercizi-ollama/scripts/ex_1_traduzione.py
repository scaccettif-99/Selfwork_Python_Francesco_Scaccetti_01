from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

input_text = input("Enter text: ")

completion = client.chat.completions.create(
    model="llama3.2",
    messages=[
        {"role": "system", "content": "Sei un traduttore. Se il testo è in italiano, traducilo in inglese. Se il testo è in inglese, traducilo in italiano. Rispondi solo con la traduzione, senza aggiungere altro."},
        {"role": "user", "content": input_text},
    ],
)

print(completion.choices[0].message.content)