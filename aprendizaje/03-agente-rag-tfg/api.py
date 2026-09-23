from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from anthropic import Anthropic
import chromadb
from datetime import datetime

load_dotenv()
client = Anthropic()

chroma_client = chromadb.PersistentClient(path="./base_tfg_v2")
coleccion = chroma_client.get_or_create_collection(name="tfg_alberto_v2")

tools = [
    {
        "name": "buscar_en_tfg",
        "description": "Busca información relevante dentro del Trabajo de Fin de Grado de Alberto sobre monitorización de suelo agrario. Úsalo para cualquier pregunta sobre el contenido del TFG.",
        "input_schema": {
            "type": "object",
            "properties": {
                "consulta": {"type": "string", "description": "Qué se quiere buscar en el TFG"}
            },
            "required": ["consulta"]
        }
    },
    {
        "name": "calculadora",
        "description": "Realiza operaciones matemáticas simples. Úsalo cuando haya que sumar, restar, multiplicar o dividir.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expresion": {"type": "string", "description": "Expresión matemática, ej: '23 * 4' o '100 / 5'"}
            },
            "required": ["expresion"]
        }
    },
    {
        "name": "fecha_actual",
        "description": "Devuelve la fecha y hora actual. Úsalo si la pregunta depende de saber qué día es hoy.",
        "input_schema": {
            "type": "object",
            "properties": {}
        }
    }
]

def buscar_en_tfg(consulta):
    resultados = coleccion.query(query_texts=[consulta], n_results=8)
    return "\n\n---\n\n".join(resultados["documents"][0])

def calculadora(expresion):
    try:
        resultado = eval(expresion)
        return str(resultado)
    except Exception as e:
        return f"Error al calcular: {e}"

def fecha_actual():
    return datetime.now().strftime("%Y-%m-%d %H:%M")

funciones_disponibles = {
    "buscar_en_tfg": lambda input: buscar_en_tfg(input["consulta"]),
    "calculadora": lambda input: calculadora(input["expresion"]),
    "fecha_actual": lambda input: fecha_actual()
}

def preguntar_al_agente(pregunta_usuario):
    historial = [{"role": "user", "content": pregunta_usuario}]

    while True:
        respuesta = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1000,
            tools=tools,
            messages=historial
        )

        if respuesta.stop_reason != "tool_use":
            texto_final = next((b.text for b in respuesta.content if b.type == "text"), "")
            return texto_final

        historial.append({"role": "assistant", "content": respuesta.content})

        resultados_herramientas = []
        for bloque in respuesta.content:
            if bloque.type == "tool_use":
                funcion = funciones_disponibles[bloque.name]
                resultado = funcion(bloque.input)
                resultados_herramientas.append({
                    "type": "tool_result",
                    "tool_use_id": bloque.id,
                    "content": resultado
                })

        historial.append({"role": "user", "content": resultados_herramientas})


# --- A partir de aquí, la parte nueva: la API ---

app = FastAPI(title="Agente TFG API")

class Pregunta(BaseModel):
    texto: str

@app.get("/")
def inicio():
    return {"mensaje": "API del agente funcionando. Manda POST a /preguntar"}

@app.post("/preguntar")
def preguntar(pregunta: Pregunta):
    respuesta = preguntar_al_agente(pregunta.texto)
    return {"pregunta": pregunta.texto, "respuesta": respuesta}