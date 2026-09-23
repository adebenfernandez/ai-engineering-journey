from dotenv import load_dotenv
from anthropic import Anthropic
import chromadb
from pypdf import PdfReader

load_dotenv()
client = Anthropic()

# 1. Extraer texto del PDF, saltando las páginas de índices iniciales
print("Leyendo el PDF...")
reader = PdfReader("TFG_AlbertoDebenFernandez.pdf")

PAGINA_INICIO_CONTENIDO = 20  # saltamos portada + índices (ajustado a tu TFG)

texto_completo = ""
for i, pagina in enumerate(reader.pages):
    if i < PAGINA_INICIO_CONTENIDO:
        continue
    texto_completo += pagina.extract_text() + "\n"

print(f"PDF leído (desde página {PAGINA_INICIO_CONTENIDO+1}). Total de caracteres: {len(texto_completo)}")

# 2. Trocear en fragmentos de tamaño fijo, con solapamiento
def trocear_texto(texto, tamano_fragmento=1200, solapamiento=300):
    fragmentos = []
    inicio = 0
    while inicio < len(texto):
        fin = inicio + tamano_fragmento
        fragmentos.append(texto[inicio:fin])
        inicio += tamano_fragmento - solapamiento
    return fragmentos

fragmentos = trocear_texto(texto_completo)
print(f"El documento se ha dividido en {len(fragmentos)} fragmentos.")

# 3. Base de datos vectorial (usamos un nombre nuevo para no mezclar con la anterior)
chroma_client = chromadb.PersistentClient(path="./base_tfg_v2")
coleccion = chroma_client.get_or_create_collection(name="tfg_alberto_v2")

# 4. Añadir en lotes
print("Generando embeddings y guardando en la base vectorial...")
tamano_lote = 100
for i in range(0, len(fragmentos), tamano_lote):
    lote = fragmentos[i:i+tamano_lote]
    ids_lote = [f"fragmento_{j}" for j in range(i, i+len(lote))]
    coleccion.add(documents=lote, ids=ids_lote)
    print(f"  Procesados {i+len(lote)}/{len(fragmentos)} fragmentos")

print("¡Listo! Base vectorial creada.\n")

# 5. Modo preguntas interactivo
print("--- Modo preguntas ---")
print("Escribe 'salir' para terminar.\n")

while True:
    pregunta = input("Tu pregunta sobre el TFG: ")
    if pregunta.lower() == "salir":
        break

    resultados = coleccion.query(query_texts=[pregunta], n_results=10)
    fragmentos_relevantes = resultados["documents"][0]
    ids_relevantes = resultados["ids"][0]
    print("Fragmentos usados como contexto:", ids_relevantes)

    contexto = "\n\n---\n\n".join(fragmentos_relevantes)

    respuesta = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=400,
        system="Responde SOLO usando la información del contexto proporcionado, que son fragmentos de un Trabajo de Fin de Grado. Si no está en el contexto, di que no lo sabes.",
        messages=[
            {"role": "user", "content": f"Contexto:\n{contexto}\n\nPregunta: {pregunta}"}
        ]
    )

    print("\nRespuesta:", respuesta.content[0].text, "\n")