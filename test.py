from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()

historial = [
    {"role": "user", "content": "Me llamo Alberto y quiero aprender IA."},
]

respuesta1 = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=200,
    messages=historial
)
print("Claude:", respuesta1.content[0].text)

# Añadimos la respuesta de Claude al historial
historial.append({"role": "assistant", "content": respuesta1.content[0].text})

# Añadimos una nueva pregunta del usuario
historial.append({"role": "user", "content": "¿Cómo me llamo?"})

respuesta2 = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=200,
    messages=historial
)
print("Claude:", respuesta2.content[0].text)