from pypdf import PdfReader
import chromadb

reader = PdfReader("TFG_AlbertoDebenFernandez.pdf")
PAGINA_INICIO_CONTENIDO = 20
texto_completo = ""
for i, pagina in enumerate(reader.pages):
    if i < PAGINA_INICIO_CONTENIDO:
        continue
    texto_completo += pagina.extract_text() + "\n"

def trocear_texto(texto, tamano_fragmento=1200, solapamiento=300):
    fragmentos = []
    inicio = 0
    while inicio < len(texto):
        fin = inicio + tamano_fragmento
        fragmentos.append(texto[inicio:fin])
        inicio += tamano_fragmento - solapamiento
    return fragmentos

fragmentos = trocear_texto(texto_completo)

# Buscamos a mano en qué fragmento está la palabra clave
for idx, f in enumerate(fragmentos):
    if "Arquitectura de la Aplicaci" in f:
        print(f"El contenido de arquitectura está en el fragmento numero {idx}")
        break

# Usamos la base que ya creaste (base_tfg_v2)
chroma_client = chromadb.PersistentClient(path="./base_tfg_v2")
coleccion = chroma_client.get_or_create_collection(name="tfg_alberto_v2")

pregunta = "¿Qué arquitectura usa la aplicación?"
resultados = coleccion.query(query_texts=[pregunta], n_results=10)
ids_devueltos = resultados["ids"][0]
print("\nIDs que Chroma considera más relevantes:", ids_devueltos)

id_buscado = f"fragmento_{idx}"
print(f"\n¿Está el fragmento {idx} (el de arquitectura) entre los 10 más relevantes?", id_buscado in ids_devueltos)