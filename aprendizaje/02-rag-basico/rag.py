from dotenv import load_dotenv
from anthropic import Anthropic
import chromadb

load_dotenv()
client = Anthropic()

# 1. Creamos un cliente de Chroma (base de datos vectorial local, se guarda en disco)
chroma_client = chromadb.PersistentClient(path="./mi_base_vectorial")

# 2. Creamos (o recuperamos si ya existe) una "colección" - piensa en ello como una tabla
coleccion = chroma_client.get_or_create_collection(name="documentos_nubeverde")

# 3. Leemos el documento y lo troceamos en fragmentos simples (por párrafos)
with open("documento.txt", "r", encoding="utf-8") as f:
    texto_completo = f.read()

fragmentos = [p.strip() for p in texto_completo.split("\n\n") if p.strip()]

print(f"El documento se ha dividido en {len(fragmentos)} fragmentos.")

# 4. Añadimos los fragmentos a la base vectorial
# Chroma genera los embeddings automáticamente por debajo (usa un modelo por defecto)
coleccion.add(
    documents=fragmentos,
    ids=[f"fragmento_{i}" for i in range(len(fragmentos))]
)

print("Fragmentos guardados en la base vectorial.")

# 5. Hacemos una pregunta de prueba
pregunta = "¿Quién es el CEO de NubeVerde y qué premio ganaron?"

# 6. Buscamos los fragmentos más relevantes para esa pregunta
resultados = coleccion.query(
    query_texts=[pregunta],
    n_results=2  # los 2 fragmentos más relevantes
)

fragmentos_relevantes = resultados["documents"][0]

print("\nFragmentos recuperados como más relevantes:")
for f in fragmentos_relevantes:
    print("-", f)

# 7. Construimos el contexto y se lo pasamos a Claude
contexto = "\n\n".join(fragmentos_relevantes)

respuesta = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=300,
    system="Responde SOLO usando la información del contexto proporcionado. Si no está en el contexto, di que no lo sabes.",
    messages=[
        {
            "role": "user",
            "content": f"Contexto:\n{contexto}\n\nPregunta: {pregunta}"
        }
    ]
)

print("\nRespuesta de Claude:")
print(respuesta.content[0].text)