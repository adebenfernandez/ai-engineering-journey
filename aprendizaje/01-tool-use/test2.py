from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()

tools = [
    {
        "name": "get_weather",
        "description": "Obtiene el tiempo actual de una ciudad",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "Nombre de la ciudad"}
            },
            "required": ["city"]
        }
    }
]

def get_weather(city):
    datos_falsos = {
        "A Coruña": "18°C, nublado",
        "Madrid": "25°C, soleado",
    }
    return datos_falsos.get(city, "No tengo datos de esa ciudad")

historial = [{"role": "user", "content": "¿Qué tiempo hace en A Coruña?"}]

# Primera llamada
mensaje = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=300,
    tools=tools,
    messages=historial
)

# Añadimos la respuesta de Claude (con su petición de herramienta) al historial
historial.append({"role": "assistant", "content": mensaje.content})

# Buscamos el bloque de tipo tool_use dentro de la respuesta
for bloque in mensaje.content:
    if bloque.type == "tool_use":
        # Ejecutamos la función de verdad, con los parámetros que pidió Claude
        resultado = get_weather(bloque.input["city"])

        # Le devolvemos el resultado a Claude, referenciando el id de esa petición
        historial.append({
            "role": "user",
            "content": [
                {
                    "type": "tool_result",
                    "tool_use_id": bloque.id,
                    "content": resultado
                }
            ]
        })

# Segunda llamada: ahora Claude ya tiene el dato real y puede responder de verdad
respuesta_final = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=300,
    tools=tools,
    messages=historial
)

print(respuesta_final.content[0].text)