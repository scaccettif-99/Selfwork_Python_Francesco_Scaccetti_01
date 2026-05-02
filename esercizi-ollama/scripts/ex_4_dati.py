from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

input_text = input("Enter text: ")
data = {"name": "Giovanni", "age": 30, "city": "Roma", "profession": "Ingegnere"}

completion = client.chat.completions.create(
    model="llama3.2",
    messages=[
        {"role": "system", "content": "Sei un assistente che trasforma dati strutturati in descrizioni testuali. Riceverai un dizionario Python. Scrivi 2-3 frasi semplici e corrette in italiano che descrivano la persona. Non usare metafore, sii diretto e chiaro."},
        {"role": "user", "content": input_text + "\n" + str(data)},
    ],
)

print(completion.choices[0].message.content)