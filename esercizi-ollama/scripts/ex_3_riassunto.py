from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

input_text = input("Enter text: ")

completion = client.chat.completions.create(
    model="llama3.2",
    messages=[
        {"role": "system", "content": "Sei un assistente che riassume articoli di notizie. Devi creare un riassunto in un singolo paragrafo di massimo 255 caratteri. Sii conciso e cattura solo i punti essenziali."},
        {"role": "user", "content": input_text},
    ],
)

print(completion.choices[0].message.content)