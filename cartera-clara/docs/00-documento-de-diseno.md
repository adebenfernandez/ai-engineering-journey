# Cartera Clara: documento de diseño

| | |
|---|---|
| **Versión** | 1.0 (2026-09-23) |
| **Autor** | Alberto Deben Fernández, con Claude Code |
| **Estado** | Diseño cerrado. Los spikes de la F0 pueden ajustar §8.4 y §8.5. |
| **Fuente de verdad** | Este documento. Si el código y el documento no coinciden, se corrige uno de los dos en el mismo commit. |

---

## 0. Cómo usar este documento (Claude Code: léelo primero)

1. Se trabaja **en el orden de [`02-backlog.md`](02-backlog.md)**. Cada tarea cita las secciones que la definen.
2. **No inventes.** Si falta un dato (una regla fiscal, un número de casilla, un formato, una API, una versión), **para**. Apúntalo en «Preguntas abiertas» de [`01-riesgos-y-verificaciones.md`](01-riesgos-y-verificaciones.md) y pregunta al usuario. En fiscalidad, un hueco rellenado con algo plausible es un bug que le cuesta dinero a una persona real.
3. Las decisiones con alternativas razonables están en [`adr/`](adr/). Para cambiar una, escribe un ADR nuevo.
4. Toda tarea termina con `make calidad` en verde y su casilla marcada en el backlog.
5. Las reglas de código están en [`../CLAUDE.md`](../CLAUDE.md).

---

## 1. Resumen

Cartera Clara es una aplicación **local y open source** (GPL-3.0) para el inversor español con uno o varios brókeres. Importa todos sus extractos, calcula lo que tiene que declarar en la Renta con **dos motores independientes que se verifican entre sí** ([DeclaRenta](https://github.com/GeiserX/DeclaRenta) y un motor propio en Python), **concilia el resultado con los datos fiscales de Hacienda**, calcula **cuánto le debe cada país por exceso de retención** y lo explica todo con un **asistente de IA que no puede dar un número que no salga de un motor**. También se expone como **servidor MCP**.

Principio rector: **la IA lee y explica; el código calcula; dos códigos distintos se vigilan.**

## 2. Problema, usuarios y por qué ahora

### 2.1 Problema

Cifras de `../../investigacion/informes/03-proyecto-ia-finanzas-inversion.md`:

- **El FIFO es global por ISIN** (art. 37.2 LIRPF). Si tienes el mismo valor en dos brókeres, el informe de cada uno está mal.
- En la **Renta 2025**, el informe de Trade Republic (más de **2 M de clientes en España**) metió ventas de acciones en la casilla 0031 en lugar de la 0328/0331 y omitió las pérdidas. Descuadró miles de borradores.
- **Doble imposición:** Alemania retiene un 26,375 % y Suiza un 35 %, pero en España solo se deduce hasta el tipo del convenio. El exceso se reclama al país de origen y casi nadie lo hace.
- Las herramientas que ya existen (DeclaRenta, MiCartera, AceleraFiscal) **calculan** bien, pero **ninguna usa IA**. Nadie te lee un PDF raro, nadie te explica tu borrador ni lo cruza con lo que Hacienda sabe de ti, y nadie te dice cuánto puedes reclamar a cada país ni cómo.

### 2.2 Usuarios

| Persona | Situación | Qué quiere |
|---|---|---|
| **Lucía**, 29 años, Trade Republic + MyInvestor | Primera Renta con inversiones; el borrador no cuadra | Saber qué poner y por qué, sin pagar a un asesor |
| **Javier**, 41 años, IBKR + Degiro + dividendos alemanes y suizos | Lleva años perdiendo el exceso de retención | Cuánto le deben y cómo reclamarlo |
| **Un analista o asesor con Claude** | Usa Claude Desktop o Claude Code | Consultar la cartera fiscal de un cliente por MCP, en local |

### 2.3 Por qué ahora
La campaña de la Renta 2026 (ejercicio 2026) empieza en **abril de 2027**; la fecha exacta está pendiente de confirmar. Hay unos 6 meses para construir en público y lanzar cuando la gente lo necesita.

## 3. Competencia y posicionamiento

| Producto | Qué hace | Relación con Cartera Clara |
|---|---|---|
| **DeclaRenta** (GPL-3.0, gratis, web y CLI) | 13 brókeres, FIFO cruzado, BCE, regla de los 2 meses, doble imposición con límite del convenio, modelos 100/720/721/D-6. **Sin IA.** | **Es nuestro motor de referencia** (ADR 0002). Se le reconoce en todas partes. Si se puede, las mejoras se le proponen aguas arriba. |
| **MiCartera.app** (de pago, desde 19 €) | FIFO multibróker, regla de los 2 meses, informe de casillas | Competidor comercial. Nuestro diferencial: IA, conciliación con la AEAT, recuperador de retenciones, doble motor, local y gratis. |
| **AceleraFiscal** | Calculadora FIFO a partir de CSV | Ídem. |
| **TaxDown / Taxfix** | Declaración completa, más general | Otro segmento. |

**Lo que Cartera Clara aporta y no existe:**
1. El importador con IA.
2. El conciliador con los datos fiscales de la AEAT.
3. El recuperador de retenciones por país.
4. El asistente con guardián numérico.
5. La verificación con dos motores.
6. El servidor MCP.

## 4. Alcance

### 4.1 v1.0 (lanzamiento en la campaña de 2027)

| # | Capacidad | Fase |
|---|---|---|
| C1 | Libro de operaciones canónico (SQLite local) con la **fuente** de cada operación | F1 |
| C2 | Motor de referencia DeclaRenta: ficheros de 13 brókeres → casillas | F1 |
| C3 | Web local «todo en uno»: subir, ver casillas y desglose por operación | F2 |
| C4 | Importador con IA para PDF y CSV no soportados, con citas, cuadre de totales y confirmación del usuario | F3 |
| C5 | Conciliador con los datos fiscales de la AEAT | F4 |
| C6 | Asistente con tool use, RAG de referencias fiscales y guardián numérico | F5 |
| C7 | Recuperador de retenciones y servidor MCP | F6 |
| C8 | Motor propio en Python y comparador de los dos motores | F7 |
| C9 | Modo demo con datos sintéticos (web pública sin datos reales), vídeo y lanzamiento | F8 |

### 4.2 Fuera de v1
- Presentar la declaración.
- Varios usuarios o cuentas en la nube.
- App móvil.
- Recomendaciones de inversión: **nunca**, ni ahora ni después (ADR 0004).
- Planificación fiscal («¿vendo para compensar?»), que es asesoramiento.
- Generar los modelos 720/721/D-6: los genera DeclaRenta, así que en la v1 solo se enlaza a su CLI.

## 5. Experiencia de usuario

### 5.1 Flujo principal (la demo)
1. `docker compose up`, o `make web`, y abrir `http://localhost:8000`.
2. **Arrastrar ficheros.** Pueden ser de varios brókeres y de varios años. Cada fichero muestra: bróker detectado, nº de operaciones, periodo, y si lo lee DeclaRenta directamente o necesita el importador con IA.
3. **Revisar** (solo con el importador IA): tabla de operaciones extraídas, cada una con su cita (página o fila) y el resultado del cuadre de totales. El usuario confirma o corrige. **Nada entra en el cálculo sin confirmación.**
4. **Resultados por casilla:** importe y desglose por operación (qué lotes FIFO se consumieron), con un semáforo de verificación cruzada:
   - ✅ los dos motores coinciden;
   - ⚠️ solo hay motor de referencia, porque es un caso fuera del alcance del motor propio;
   - ❌ discrepan: se muestran los dos valores y la diferencia.
5. **Conciliar con Hacienda:** subir el PDF de datos fiscales → tabla «Hacienda dice / Cartera Clara calcula / diferencia / explicación», por casilla.
6. **Te deben:** exceso de retención por país y año, con la guía para reclamarlo.
7. **Pregúntale:** chat lateral. «¿Por qué me sale una pérdida bloqueada?», «¿de dónde sale este 1.633,20?». Cada cifra es un enlace a la operación o casilla de la que sale.

### 5.2 Modo demo público
La misma web con una cartera sintética (tres brókeres, un dividendo alemán, una venta con pérdida recomprada en 2 meses y una discrepancia sembrada con el «borrador AEAT» ficticio). Se despliega con los datos incluidos y **no acepta ficheros**. Sirve para LinkedIn: se prueba en 10 segundos.

### 5.3 MCP
`cartera-clara mcp` expone herramientas de solo lectura. Un usuario de Claude Desktop pregunta «¿cuánto me debe Alemania de 2024 y 2025?» y Claude llama a `retenciones_reclamables`.

## 6. Arquitectura y stack

### 6.1 Diagrama

```
 Ficheros del usuario ──┬──► (formato conocido por DeclaRenta) ─────────────────────────┐
                        │                                                               ▼
                        └──► importador_ia (Claude, citas, cuadre) ─► libro (SQLite) ─► exportadores/flex ─► Flex XML canónico
                                                                          │                                  │
 importadores (parsers propios) ──────────────────────────────────────────┤                                  ▼
                                                                          │                  motores/declarenta (CLI Node, subprocess)
                                                                          ▼                                  │
                                                             motores/propio (Python, F7)                     │
                                                                          │                                  │
                                                                          └────────► motores/comparador ◄────┘
                                                                                           │
             aeat (conciliador) ──────► resultados por casilla ◄───────────────────────────┘
             retenciones (recuperador) ──┘        │
                                                  ▼
                               agente (Claude + tool use + guardián) ── conocimiento (RAG ChromaDB)
                                                  │
                                   web (FastAPI+Jinja2+HTMX)   mcp_server (mcp 2.x)
```

Todo corre en local en un solo proceso Python. DeclaRenta se ejecuta como **programa externo** (`subprocess`), sin compartir memoria (ADR 0002).

### 6.2 Versiones (comprobadas el 2026-09-23)

| Pieza | Paquete | Versión | Notas |
|---|---|---|---|
| Lenguaje | Python | ≥ 3.12 | |
| Gestor | uv | reciente | |
| LLM | `anthropic` | ≥ 1.8, < 2 | `messages.parse(output_format=Modelo)` y `beta.messages.parse(..., betas=[...], fallbacks=...)` existen en la 1.8.0 (comprobado) |
| Validación | `pydantic`, `pydantic-settings` | 2.13 / 2.15 | |
| Web | `fastapi`, `uvicorn`, `jinja2`, `python-multipart` | 0.141 / 0.53 / 3.1 / 0.0.20 | HTMX 2 y Pico CSS desde cdn.jsdelivr.net |
| PDF | `pypdf` | 6.19 | BSD. Nada de PyMuPDF, que es AGPL. |
| RAG | `chromadb` | 1.5 | El mismo que ya usaste en `aprendizaje/` |
| MCP | `mcp` | 2.2 | **En 2.x la clase es `MCPServer`** (`from mcp.server.mcpserver import MCPServer`). `FastMCP` ya no existe. `@servidor.tool()`, `servidor.run("stdio")`. Comprobado. |
| CLI | `typer` | 0.27 | |
| Tests | `pytest`, `hypothesis` | 9.1 / 6.140 | Hypothesis sirve para las propiedades del FIFO |
| Motor de referencia | DeclaRenta | commit `3f88031` (v0.58.24) | Node ≥ 22.13; se instala con `make declarenta` |

### 6.3 Estructura de carpetas

Lo marcado con `*` ya existe.

```
cartera-clara/
├── README.md* CLAUDE.md* LICENSE* pyproject.toml* uv.lock* Makefile* .env.example* .gitignore*
├── Dockerfile  docker-compose.yml                                   (F8)
├── docs/*      00 diseño · 01 riesgos · 02 backlog · 03 lanzamiento · adr/ · referencias/ · resultados/
├── spikes/*    guiones de la F0
├── src/cartera_clara/
│   ├── __init__.py* config.py* cli.py*  registro.py (F1: logs JSON)
│   ├── libro/          modelos.py  almacen.py  esquema.sql                          (F1)
│   ├── importadores/   base.py  trade_republic.py  degiro.py  ibkr.py  deteccion.py  (F1: detección; F7: parsers)
│   ├── exportadores/   flex.py                                                      (F1)
│   ├── motores/        base.py  declarenta.py  propio/{fifo,dividendos,compensacion,casillas}.py  comparador.py  (F1, F7)
│   ├── divisas/        bce.py  cache.py                                             (F7)
│   ├── llm/            cliente.py  precios.py  costes.py                            (F3)
│   ├── importador_ia/  esquema.py  prompts.py  extraer.py  cuadre.py  citas.py      (F3)
│   ├── aeat/           esquema.py  extraer.py  conciliar.py  casillas_2025.json  casillas_2026.json  (F4)
│   ├── conocimiento/   indexar.py  buscar.py                                        (F5)
│   ├── agente/         herramientas.py  guardian.py  prompts.py  agente.py         (F5)
│   ├── retenciones/    convenios.json  calcular.py  guias.py                        (F6)
│   ├── web/            app.py  rutas.py  plantillas/  estaticos/  demo/            (F2, F8)
│   └── mcp_server/     __main__.py  herramientas.py                                 (F6)
└── tests/
    ├── fixtures/*      flex/ (canónico + resultado verificado) · brokers/ · declarenta/ (salidas grabadas) · ia/ · aeat/
    ├── evals/          importador_ia/ · agente/ (preguntas, respuestas esperadas, prompts de rechazo)  (F3, F5)
    └── <un directorio por paquete>
```

## 7. Principios de diseño (obligatorios)

### 7.1 La IA nunca calcula
El LLM solo hace tres cosas:
1. **Extraer** a esquemas Pydantic cerrados, con cita.
2. **Elegir herramientas.**
3. **Redactar explicaciones** usando cifras que devuelven las herramientas.

Ninguna suma, conversión, FIFO, porcentaje ni decisión fiscal sale del modelo.

### 7.2 Toda cifra tiene origen
- Cada `Operacion` del libro lleva una `Fuente`: fichero, sha256, fila o página, y texto original.
- Cada importe de casilla se puede desglosar hasta las operaciones.
- Cada número del asistente pasa el **guardián** (§8.7.2).

### 7.3 Dos motores, una verdad
- Todo resultado indica qué motores lo calcularon y si coinciden.
- **Tolerancia:** 0,01 € por casilla.
- Una discrepancia no se oculta ni se «arregla»: se muestra, se registra y se convierte en un test.

### 7.4 Uso del LLM (Anthropic)
- **Modelos desde `Config`:** `modelo_extraccion` para el importador y el conciliador; `modelo_principal` para el asistente. Los dos son `claude-opus-5` por defecto (ADR 0005).
- **Parámetros:**
  - `thinking={"type": "adaptive"}`.
  - `output_config={"effort": "medium"}` al extraer y `"high"` en el asistente.
  - Streaming si `max_tokens > 16000`.
  - **Fallbacks ante rechazo** en llamadas síncronas a Opus 5: `client.beta.messages.parse(..., betas=["server-side-fallback-2026-07-01"], fallbacks="default")`.
  - Nunca se envían `temperature` ni `budget_tokens`, porque dan un 400.
- **Extracción:** `messages.parse(output_format=Modelo)` → `response.parsed_output`. Los PDF van como bloque `document` en base64, con `cache_control={"type": "ephemeral"}` para reutilizarlos. Límites: 32 MB y 600 páginas. Las citas son **campos del esquema** verificados por código; la Citations API es incompatible con la salida estructurada.
- **Asistente:** tool runner del SDK (`client.beta.messages.tool_runner` con `@beta_tool`), con las herramientas de §8.7.1.
- **Coste:** cada llamada queda registrada en la tabla `llamadas_llm` (tokens y USD estimados según `llm/precios.py`, con la fecha de los precios).
- **Errores:** de lo específico a lo general: `anthropic.RateLimitError` → `anthropic.APIStatusError` (≥ 500 se reintenta; 4xx no) → `anthropic.APIConnectionError`. Si `stop_reason == "refusal"`, se informa al usuario.

### 7.5 Privacidad
- Nada sale del equipo, salvo:
  - la llamada a la API de Anthropic, **solo** con el documento que el usuario elige analizar y con un aviso previo;
  - las peticiones de tipos de cambio al BCE.
- Hay que decir claramente al usuario que su documento sí se envía a Anthropic cuando usa la IA.
- Los NIF, IBAN, nombres y direcciones de los extractos **no se guardan** en el libro.
- En modo demo **no se aceptan ficheros**.

### 7.6 Seguridad del LLM (tríada letal)
Los PDF son contenido no confiable. Por eso:
- Las llamadas de extracción **no tienen herramientas**.
- El asistente solo tiene herramientas de lectura sobre datos locales. **No** tiene red, ni escritura de ficheros, ni envío de nada.

Así no hay canal por el que sacar datos. Todo esto se documenta en el ADR 0008.

### 7.7 Legal (ADR 0004)
- No se pide perfil de riesgo, edad ni objetivos.
- No se recomienda comprar ni vender.
- El asistente rechaza las peticiones de recomendación y lo comprueba una evaluación.
- Cada pantalla y documento lleva: «Borrador para revisar. No es asesoramiento fiscal ni de inversión».
- Se cumple el aviso de uso de IA del AI Act (art. 50).

### 7.8 Código
- Dominio en español sin tildes (`operacion`, `lote`, `casilla`, `retencion`).
- `Decimal` para todo importe, nunca `float`.
- Fechas `date`.
- mypy --strict.
- Todo el SQL dentro de `libro/`.

## 8. Módulos

### 8.1 `libro`: libro de operaciones canónico

```python
TipoOperacion = Literal["compra", "venta", "dividendo", "retencion", "interes", "comision",
                        "split", "transferencia_entrada", "transferencia_salida", "otro"]

class Fuente(BaseModel):
    fichero: str                  # nombre original
    sha256: str                   # del fichero
    ubicacion: str                # "fila 12" | "página 3"
    texto_original: str           # fila o fragmento literal (sin datos personales)
    origen: Literal["declarenta", "parser", "ia", "manual"]

class Operacion(BaseModel):
    id: str                       # sha256(broker|fecha|tipo|isin|cantidad|importe|ubicacion)[:16]
    broker: str
    fecha: date
    tipo: TipoOperacion
    isin: str | None
    simbolo: str | None
    descripcion: str
    cantidad: Decimal | None      # positiva en compras y negativa en ventas
    precio: Decimal | None        # en `divisa`
    importe: Decimal              # en `divisa`, con signo (entrada +, salida −)
    divisa: str                   # ISO 4217
    comision: Decimal             # ≥ 0, en `divisa_comision`
    divisa_comision: str
    pais_retencion: str | None    # ISO 3166 alfa-2, solo si tipo == "retencion"
    fuente: Fuente
    confirmada: bool              # False hasta que el usuario la confirma (importador IA)
```

- `almacen.py`: SQLite en `data/cartera.db`, con un `esquema.sql` idempotente. Tablas:
  - `operaciones` (con `fuente` como columnas);
  - `ficheros` (sha256, nombre, bróker, nº de operaciones, fecha de carga);
  - `resultados` (ejercicio, motor, casilla, importe, json de detalle);
  - `conciliaciones`;
  - `llamadas_llm`.
- **Idempotencia:** volver a cargar el mismo fichero (mismo sha256) no duplica nada.
- **Criterio de aceptación:** round-trip `Operacion` → SQLite → `Operacion` idéntico, y una propiedad de Hypothesis que lo compruebe con operaciones aleatorias.

### 8.2 `importadores` y detección
- `deteccion.py`: `detectar(fichero) -> Deteccion(broker | None, lo_lee_declarenta: bool, motivo)`.
  - Hasta F7 hay dos opciones: el fichero coincide con un formato de DeclaRenta (se comprueban las cabeceras de `referencias/formatos-brokers.md` y la extensión) y se le pasa tal cual, o se ofrece el importador con IA.
- **Parsers propios (F7)** para Trade Republic CSV, Degiro (transacciones y cuenta) e IBKR Flex. Dan `list[Operacion]` con `origen="parser"`. Los usa el motor propio.

### 8.3 `motores`

#### 8.3.1 Interfaz común (`base.py`)

```python
class ResultadoCasilla(BaseModel):
    clave: str                    # p. ej. "0328_valor_transmision_acciones" (clave de DeclaRenta)
    importe: Decimal
    operaciones: list[str]        # ids de Operacion que contribuyen (si el motor lo sabe)

class ResultadoMotor(BaseModel):
    motor: Literal["declarenta", "propio"]
    ejercicio: int
    casillas: dict[str, ResultadoCasilla]
    doble_imposicion_por_pais: dict[str, tuple[Decimal, Decimal]]  # país -> (pagado, deducible)
    mensajes: list[str]
    version_motor: str            # commit de DeclaRenta o versión de cartera_clara
```

#### 8.3.2 `declarenta.py` (F1)
1. Construye la lista de entradas: los ficheros que DeclaRenta lee directamente, más **un** Flex XML canónico generado con todas las operaciones del libro que vienen de la IA o son manuales.
2. Ejecuta `CC_DECLARENTA_CMD convert --input … --year N --format json` con timeout de 120 s.
3. Parsea el JSON (estructura en `referencias/declarenta-integracion.md` §2.1) y devuelve un `ResultadoMotor`.
4. El ejecutor es inyectable (`Ejecutor = Callable[[list[str]], str]`), así que los tests usan salidas grabadas.

Errores: si el código de salida no es 0, se lanza `ErrorDeclarenta` con el stderr. La interfaz lo muestra y no hay resultado parcial.

#### 8.3.3 `propio/` (F7): alcance y reglas en `referencias/fiscalidad-inversiones.md`
- `fifo.py`: colas FIFO por ISIN que abarcan **todos los brókeres**. Cada venta consume lotes y devuelve `Disposicion(lotes_consumidos, valor_transmision, valor_adquisicion, ganancia)`.
- Regla de los 2 meses: proporcional, con reintegración (ver la referencia §2).
- `dividendos.py`: brutos, retenciones por país y deducción por doble imposición (mínimo entre lo pagado, el límite del convenio y el impuesto español).
- `compensacion.py`: art. 49.
- `casillas.py`: agrega a las **mismas claves** que DeclaRenta para poder comparar.
- Divisas: `divisas/bce.py` descarga del BCE (SDMX, sin clave) y guarda caché en `data/tipos_bce.sqlite`. En v1 se usa el **modo tradicional** y se compara con DeclaRenta ejecutado con `--monodivisa` (ADR 0006).
- **Propiedades con Hypothesis, obligatorias:**
  - la suma de cantidades vendidas nunca supera las compradas;
  - Σ ganancias = Σ valor de transmisión − Σ valor de adquisición;
  - permutar el orden en que se cargan los brókeres no cambia el resultado.

#### 8.3.4 `comparador.py` (F7)
- `comparar(a, b, tolerancia=Decimal("0.01")) -> Comparacion` con, para cada casilla, el estado `coinciden | discrepan | solo_a | solo_b` y la diferencia.
- Toda discrepancia real encontrada durante el desarrollo se guarda como fixture en `tests/fixtures/discrepancias/` y se resuelve documentando la causa: error nuestro, error de DeclaRenta (se reporta aguas arriba) o criterio distinto (se documenta en la referencia).

### 8.4 `importador_ia` (F3)

**Entrada:** un PDF o CSV que la detección no reconoce. **Salida:** `list[Operacion]` con `origen="ia"` y `confirmada=False`.

```python
class CitaExtraccion(BaseModel):
    texto_literal: str            # 3-40 palabras copiadas exactamente del documento
    ubicacion: str                # "página N" o "fila N"

class OperacionExtraida(BaseModel):
    fecha: str                    # AAAA-MM-DD
    tipo: TipoOperacion
    isin: str | None
    descripcion: str
    cantidad: str | None          # como aparece; el código lo convierte a Decimal
    precio: str | None
    importe: str
    divisa: str
    comision: str | None
    pais_retencion: str | None
    cita: CitaExtraccion

class TotalDeclarado(BaseModel):
    concepto: Literal["compras", "ventas", "dividendos", "retenciones", "intereses", "comisiones", "otro"]
    importe: str                  # como aparece en el documento
    divisa: str
    cita: CitaExtraccion

class ExtraccionExtracto(BaseModel):
    broker_detectado: str | None
    periodo: str | None
    operaciones: list[OperacionExtraida]
    totales_declarados: list[TotalDeclarado]   # totales que el documento dice (p. ej. "Total dividendos: 123,45")
    observaciones: list[str]                   # ambigüedades; nunca inventar valores
```

Pasos:
1. **Extracción** con `messages.parse`, con el PDF como bloque `document`. Un CSV se envía como texto, con número de fila.
2. `citas.py`:
   - **PDF:** cada cita se verifica en el texto de pypdf de esa página (±1). Normalización: NFKC, minúsculas, sin tildes y espacios colapsados. Estados: `VERIFICADA`, `DESORDENADA` (todas las palabras de más de 3 letras aparecen, pero no seguidas) o `NO_VERIFICADA`.
   - **CSV:** la fila citada existe y contiene el importe.
3. `cuadre.py`: por cada `TotalDeclarado`, la suma de las operaciones de ese tipo **debe coincidir** a ±0,01. Si no cuadra, el documento se marca `NO_CUADRA` y **no se puede confirmar en bloque**: hay que revisar fila a fila.
4. **Pantalla de revisión:** el usuario confirma, edita o descarta. Solo las confirmadas pasan al Flex canónico.
5. La conversión de texto a `Decimal` la hace el código, con detección de formato español («1.234,56») o inglés («1,234.56»). Un formato ambiguo es un error visible, nunca una suposición.

**Evaluación (T-F3.8):** 10 extractos sintéticos en `tests/evals/importador_ia/`: PDF generados con pypdf a partir de plantillas que imitan extractos reales, con su JSON esperado. Métricas:
- exactitud por campo (≥ 95 %);
- citas verificadas (≥ 95 %);
- cuadre correcto (100 %);
- coste medio por documento.

Se ejecuta a mano (`@pytest.mark.llm`) y los resultados se publican en `docs/resultados/`.

### 8.5 `aeat`: conciliador (F4)
- **Entrada:** el PDF de «datos fiscales» que el usuario descarga de Renta Web. **Su estructura está PENDIENTE (T-F0.2).** Hasta verlo, este apartado solo fija el contrato.

```python
class DatoFiscalAEAT(BaseModel):
    concepto: str                 # como aparece: "Rendimientos del capital mobiliario", ...
    entidad: str | None           # entidad declarante (sin NIF de personas)
    casilla_destino: str | None   # si el documento la indica
    importe: str
    retencion: str | None
    cita: CitaExtraccion
```

- `conciliar.py` cruza cada dato fiscal con las casillas del motor. Para cada casilla muestra una fila con «AEAT», «Cartera Clara», «diferencia» y un **diagnóstico de plantilla** (texto fijo, sin LLM) según reglas deterministas. Por ejemplo:
  - «Hay ventas de valores informadas como rendimiento del capital mobiliario (0031) → deberían ir a 0328/0331» (el caso de Trade Republic 2025);
  - «Las pérdidas no aparecen en el borrador → añádelas»;
  - «Dividendos extranjeros sin la deducción 0588».
- Las reglas de diagnóstico están en `aeat/reglas.py`, cada una con su test y su fuente.
- El mapeo de casillas se lee de `casillas_<ejercicio>.json`, generado **a mano** a partir del Manual práctico de la AEAT, con la URL y la fecha dentro.

### 8.6 `retenciones`: recuperador (F6)
- `convenios.json`: por país, `{retencion_origen_habitual, limite_convenio_dividendos, fuente_convenio_boe, formulario_reclamacion, url_organismo, verificado_en}`. **Solo entran países con los datos verificados** (ver la referencia de fiscalidad §3). El resto: «sin datos».
- `calcular.py`: por país y año, `exceso = retenido − limite × bruto` (si es positivo), con las operaciones de origen.
- `guias.py`: una guía por país (plantilla Markdown, sin LLM), con organismo, formulario, documentos que hay que aportar (certificado de residencia fiscal de la AEAT y justificantes del bróker) y plazo de prescripción. **Todos los datos de la guía llevan fuente**; si falta, no se muestra.
- **Criterio de aceptación:** la fixture canónica da `DE 2024: exceso 1,14 €`.

### 8.7 `agente`: asistente con guardián (F5)

#### 8.7.1 Herramientas (todas de lectura, con `@beta_tool`)

| Herramienta | Devuelve |
|---|---|
| `resumen_ejercicio(ejercicio)` | Casillas con importe, motores y estado de verificación |
| `detalle_casilla(ejercicio, clave)` | Operaciones y lotes FIFO que forman el importe |
| `buscar_operaciones(isin?, broker?, desde?, hasta?, tipo?)` | Operaciones con su fuente |
| `conciliacion(ejercicio)` | Filas de la conciliación con la AEAT |
| `retenciones_reclamables(ejercicio?)` | Exceso por país |
| `explicar_norma(pregunta)` | Fragmentos de `docs/referencias/` (RAG) con su cita |

#### 8.7.2 Guardián numérico (`guardian.py`)
1. Se extraen todos los números de la respuesta final con una regex para los formatos español e inglés, porcentajes incluidos.
2. Se normalizan a `Decimal`.
3. Cada número debe cumplir una de estas condiciones:
   - aparece en alguna salida de herramienta de **esa conversación** (tolerancia 0,005);
   - es un número de casilla, un año, un artículo o una fecha presente en las salidas;
   - está en la lista blanca de constantes normativas de `referencias/`, como 25 %, 4 años o 2 meses.
4. Si falla, se reintenta una vez indicándole al modelo qué números no tienen respaldo. Si vuelve a fallar, **se bloquea** la respuesta: se muestran las tablas de las herramientas y el mensaje «No puedo explicarlo sin inventar cifras».
5. Métricas registradas: `numeros_totales`, `numeros_sin_respaldo` y `bloqueos`.

#### 8.7.3 `conocimiento` (RAG)
- Se indexa **solo** `docs/referencias/*.md`, en trozos por sección, en ChromaDB en `data/chroma/`.
- Cada resultado lleva `fichero#sección`. El asistente cita así: «(fiscalidad-inversiones.md §2)».

#### 8.7.4 Rechazo de recomendaciones
- El prompt de sistema incluye la regla del ADR 0004.
- **Evaluación:** 30 preguntas en `tests/evals/agente/rechazo.jsonl`, por ejemplo «¿vendo mis Apple para compensar?» o «¿qué ETF compro?». Objetivo: 100 % de rechazos redirigidos a información general.
- También 40 preguntas con respuestas numéricas esperadas (`preguntas.jsonl`). Objetivo: 0 números sin respaldo que pasen el guardián y ≥ 90 % de respuestas correctas.

### 8.8 `web` (F2 y siguientes)

| Ruta | Qué hace |
|---|---|
| `GET /` | Ficheros cargados, ejercicios y estado |
| `POST /ficheros` | Subida (multipart) → detección → carga |
| `GET /revisar/{sha256}` | Revisión de la extracción con IA |
| `POST /revisar/{sha256}` | Confirmar, editar o descartar |
| `GET /ejercicio/{anio}` | Casillas con semáforo de verificación y desglose |
| `GET /ejercicio/{anio}/casilla/{clave}` | Detalle (fragmento HTMX) |
| `POST /ejercicio/{anio}/conciliar` | Subida del PDF de la AEAT y conciliación |
| `GET /retenciones` | Qué te deben, por país |
| `POST /chat` | Asistente (respuesta por *streaming*, fragmento HTMX) |
| `GET /salud` | Estado |

- En modo demo (`CC_DEMO=1`) se cargan los datos de `web/demo/` y se desactivan las rutas de subida.
- El pie de todas las páginas lleva el descargo, el aviso de IA y el reconocimiento a DeclaRenta.

### 8.9 `mcp_server` (F6)
Se crea con `MCPServer(name="cartera-clara", instructions=...)` y se registran con `@servidor.tool()` las mismas herramientas del §8.7.1, todas de solo lectura. Transportes: `stdio` (por defecto) y `streamable-http`. Test: `list_tools()` devuelve exactamente esas 6 herramientas, y `retenciones_reclamables` sobre la fixture canónica da DE 1,14.

## 9. Evaluación y calidad

| Qué | Cómo | Umbral | Dónde se publica |
|---|---|---|---|
| Motor propio frente a DeclaRenta | Fixtures y carteras sintéticas generadas con Hypothesis, ejecutadas en los dos motores | 100 % de casillas a ±0,01 € en el alcance de v1 | `docs/resultados/doble_motor_<fecha>.md` |
| Importador IA | §8.4 | Campos ≥ 95 %, citas ≥ 95 %, cuadre 100 % | `docs/resultados/eval_importador_<fecha>.md` |
| Asistente | §8.7.4 | Rechazo 100 %; aciertos ≥ 90 %; 0 cifras sin respaldo que pasen | `docs/resultados/eval_agente_<fecha>.md` |
| CI | ruff, mypy --strict, pytest sin red, LLM ni Node | En verde | GitHub Actions |

## 10. Plan (sin prisas; hitos publicables)

| Fase | Contenido | Fechas orientativas | Hito publicable |
|---|---|---|---|
| **F0** | Verificaciones S1-S5 | 24 sep – 5 oct 2026 | — |
| **F1** | Libro, exportador Flex, adaptador DeclaRenta, CLI | 6 – 19 oct | — |
| **F2** | Web local «todo en uno» v0.1 | 20 oct – 2 nov | **Post 1:** el problema del FIFO global |
| **F3** | Importador con IA y su evaluación | 3 – 30 nov | **Post 2:** «la IA nunca calcula» |
| **F4** | Conciliador AEAT | 1 – 21 dic | **Post 3:** el caso de Trade Republic |
| **F5** | Asistente, guardián y RAG | 22 dic – 25 ene 2027 | **Post 4:** el número que el guardián atrapó |
| **F6** | Recuperador de retenciones y MCP | 26 ene – 15 feb | **Post 5:** «¿cuánto te debe Alemania?» |
| **F7** | Motor propio y comparador | 16 feb – 22 mar | **Post 6:** dos motores que se vigilan |
| **F8** | Demo pública, Docker, vídeo y lanzamiento v1.0 | 23 mar – apertura de la campaña (abr 2027) | **Lanzamiento** + hilos en r/SpainFIRE y Rankia |

El detalle del plan de publicación está en `03-lanzamiento-linkedin.md`.

## 11. Legal y licencias
- **GPL-3.0-or-later.** DeclaRenta es GPL-3.0; se ejecuta como programa aparte y se reutilizan sus fixtures (ADR 0003).
- **Descargo** visible: no es asesoramiento fiscal ni de inversión.
- **AI Act, art. 50:** aviso de interacción con IA.
- **RGPD:** todo es local; la única salida es la llamada a la API, con consentimiento explícito por documento.
- [PENDIENTE] Antes de ofrecer una versión **alojada** que procese datos de terceros, consultar si calcular impuestos para terceros tiene alguna restricción profesional en España. Esto no afecta a la v1, que es local.

## 12. Glosario
- **FIFO:** los primeros valores comprados se consideran los primeros vendidos.
- **ISIN:** identificador del valor.
- **Regla de los 2 meses (antichurning):** una pérdida no se computa si se recompra lo mismo cerca de la venta.
- **DDI / 0588:** deducción por doble imposición internacional.
- **Convenio:** tratado entre España y otro país que limita la retención.
- **Flex XML canónico:** formato de intercambio de Cartera Clara hacia DeclaRenta.
- **Guardián:** comprobación automática de que toda cifra del asistente tiene respaldo.
