from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

input_text = input("Enter text: ")

completion = client.chat.completions.create(
    model="llama3.2",
    messages=[
        {"role": "system", "content": "Sei un assistente che estrae informazioni strutturate da un testo. Dato un testo descrittivo su una persona, estrai: Nome, Età e Professione. Rispondi in questo formato:\nNome: ...\nEtà: ...\nProfessione: ..."},
        {"role": "user", "content": input_text},
    ],
)

print(completion.choices[0].message.content)