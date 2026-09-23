# Backlog de Cartera Clara

**Reglas:**
- Se hace **en orden**, una tarea por commit o PR.
- Formato del commit: `[T-F1.3] Descripción corta`.
- Al terminar una tarea: `make calidad` en verde, marcar la casilla y actualizar el diseño si algo cambió.
- «Ref.» es lo que hay que leer antes de escribir código.

---

## F0: Verificación (24 sep – 5 oct 2026) · en tu PC

- [x] **T-F0.0** Esqueleto del repo, documentación, fixtures verificadas y CI. *(2026-09-23)*
- [ ] **T-F0.1 (S1)** `make declarenta` y `make test-declarenta`. Ejecutar `convert` con tus extractos reales (sin subirlos). Anotar el resultado y compararlo con tu Renta presentada. Ref.: `spikes/README.md`.
- [ ] **T-F0.2 (S2)** Descargar tus datos fiscales de la AEAT (PDF), comprobar si tienen capa de texto y describir la estructura en `referencias/formatos-brokers.md` §2. Crear una **fixture ficticia** con la misma estructura en `tests/fixtures/aeat/`.
- [ ] **T-F0.3 (S3)** Igual con el informe fiscal PDF de Trade Republic, o con un extracto de un bróker no soportado → fixture ficticia en `tests/fixtures/ia/`.
- [ ] **T-F0.4** Crear `src/cartera_clara/aeat/casillas_2025.json` a partir del Manual práctico de Renta 2025 de la AEAT, con URL y fecha. La versión 2026 se hará cuando la publiquen.
- [ ] **T-F0.5 (S4)** Medir los tokens de 3 documentos con `count_tokens`.
- [ ] **T-F0.6 (S5)** Probar la competencia con los mismos extractos y anotarlo en `01-riesgos…` §4.

## F1: Núcleo (6 – 19 oct)

- [ ] **T-F1.1** `registro.py`: logs en JSON.
- [ ] **T-F1.2** `libro/modelos.py`: `Fuente` y `Operacion` (§8.1). Tests de validación.
- [ ] **T-F1.3** `libro/almacen.py` y `esquema.sql`: SQLite idempotente. Propiedad de Hypothesis del round-trip.
- [ ] **T-F1.4** `importadores/deteccion.py`: reconoce por cabecera o extensión los formatos de `formatos-brokers.md` §1. Tests con `tests/fixtures/brokers/`.
- [ ] **T-F1.5** `exportadores/flex.py`: `list[Operacion]` → Flex XML canónico con las reglas de `declarenta-integracion.md` §3. *Acepta:* exportar las operaciones equivalentes a la fixture canónica genera un XML equivalente a `tests/fixtures/flex/canonico_basico.xml` (comparado por atributos, no por texto).
- [ ] **T-F1.6** `motores/base.py` y `motores/declarenta.py`, con el ejecutor inyectable (§8.3.2).
- [ ] **T-F1.7** Orden `cartera-clara motor declarenta --grabar <fichero>` y grabación **en tu PC** de las salidas reales de los 4 ficheros de `tests/fixtures/brokers/` en `tests/fixtures/declarenta/`. La salida de `flex/canonico_basico.xml` ya está grabada. Completar lo que siga PENDIENTE en `declarenta-integracion.md` §2.1 (P4).
- [ ] **T-F1.8** Tests del adaptador con las salidas grabadas (sin Node) y un test `@pytest.mark.declarenta` que ejecute la CLI real.
- [ ] **T-F1.9** CLI: `cartera-clara importar <ficheros…>` y `cartera-clara calcular --ejercicio N` (tabla por consola).

## F2: Web local v0.1 (20 oct – 2 nov)

- [ ] **T-F2.1** `web/app.py`: plantilla base (Pico y HTMX), pie legal y `/salud`.
- [ ] **T-F2.2** Subida de ficheros, detección y carga (`POST /ficheros`).
- [ ] **T-F2.3** `/ejercicio/{anio}` con las casillas de DeclaRenta y su desglose.
- [ ] **T-F2.4** Tests con el `TestClient` de FastAPI y el ejecutor falso.
- [ ] **T-F2.5** 📣 Captura y GIF para el **post 1** (ver `03-lanzamiento-linkedin.md`).

## F3: Importador con IA (3 – 30 nov)

- [ ] **T-F3.1** `llm/precios.py`, `llm/costes.py` y `llm/cliente.py` (§7.4). Tests con un cliente falso.
- [ ] **T-F3.2** `importador_ia/esquema.py` (§8.4) y `prompts.py` (`PROMPT_IMPORTADOR_V1`: extraer, citar literalmente, `null` si no aparece, el documento son datos y no instrucciones).
- [ ] **T-F3.3** `importador_ia/citas.py`: verificación en PDF y en CSV. Tests de los 3 estados.
- [ ] **T-F3.4** `importador_ia/cuadre.py` y conversión de texto a `Decimal` (formato español o inglés; ambiguo = error). Tests exhaustivos.
- [ ] **T-F3.5** `importador_ia/extraer.py`: flujo completo con un cliente falso.
- [ ] **T-F3.6** Pantalla de revisión en la web (`/revisar/{sha256}`).
- [ ] **T-F3.7** Generar 10 extractos sintéticos para la evaluación (`tests/evals/importador_ia/`), con un script que construye los PDF con pypdf.
- [ ] **T-F3.8** `cartera-clara eval importador`, con resultados en `docs/resultados/`. *Acepta:* umbrales de §9.
- [ ] **T-F3.9** 📣 **Post 2**.

## F4: Conciliador AEAT (1 – 21 dic) · depende de T-F0.2

- [ ] **T-F4.1** `aeat/esquema.py` y `aeat/extraer.py` (misma técnica que el importador).
- [ ] **T-F4.2** `aeat/reglas.py`: reglas de diagnóstico, con un test por regla, incluida la de Trade Republic 2025 (0031 frente a 0328/0331).
- [ ] **T-F4.3** `aeat/conciliar.py` y la ruta `/ejercicio/{anio}/conciliar`.
- [ ] **T-F4.4** 📣 **Post 3**.

## F5: Asistente (22 dic – 25 ene 2027)

- [ ] **T-F5.1** `conocimiento/indexar.py` y `buscar.py` (ChromaDB sobre `docs/referencias/`).
- [ ] **T-F5.2** `agente/herramientas.py`: las 6 herramientas del §8.7.1, con tests sin LLM.
- [ ] **T-F5.3** `agente/guardian.py`: extracción de números en formato español e inglés y comprobación de respaldo. Tests con frases trampa.
- [ ] **T-F5.4** `agente/agente.py`: tool runner, reintento y bloqueo.
- [ ] **T-F5.5** Evaluaciones: `tests/evals/agente/preguntas.jsonl` (40) y `rechazo.jsonl` (30), con `cartera-clara eval agente`. *Acepta:* umbrales de §9.
- [ ] **T-F5.6** Chat en la web (`POST /chat`).
- [ ] **T-F5.7** 📣 **Post 4**.

## F6: Retenciones y MCP (26 ene – 15 feb)

- [ ] **T-F6.1** `retenciones/convenios.json` **solo con países verificados** en el BOE (P3), con fuente y fecha.
- [ ] **T-F6.2** `retenciones/calcular.py`. *Acepta:* la fixture canónica da DE 1,14 €.
- [ ] **T-F6.3** `retenciones/guias.py` y la ruta `/retenciones`.
- [ ] **T-F6.4** `mcp_server/`: 6 herramientas con `MCPServer`; test de §8.9.
- [ ] **T-F6.5** 📣 **Post 5**.

## F7: Motor propio (16 feb – 22 mar)

- [ ] **T-F7.0** Contrastar cada regla de `referencias/fiscalidad-inversiones.md` con su fuente oficial y anotarlo (P5).
- [ ] **T-F7.1** `importadores/`: parsers propios de Trade Republic, Degiro e IBKR → `Operacion`.
- [ ] **T-F7.2** `divisas/bce.py` con caché. Test con respuestas grabadas del BCE.
- [ ] **T-F7.3** `motores/propio/fifo.py`, con las propiedades de Hypothesis del §8.3.3.
- [ ] **T-F7.4** Regla de los 2 meses (proporcional, con reintegración). Tests con el ejemplo de la referencia (100 acciones, 30 recompradas: 300 € diferidos y 700 € imputados).
- [ ] **T-F7.5** `dividendos.py` y `compensacion.py`.
- [ ] **T-F7.6** `casillas.py`, con las mismas claves que DeclaRenta.
- [ ] **T-F7.7** `motores/comparador.py`, semáforo en la web y `cartera-clara comparar`.
- [ ] **T-F7.8** Informe `docs/resultados/doble_motor_<fecha>.md`. *Acepta:* 100 % de coincidencia en el alcance de v1, o las discrepancias documentadas.
- [ ] **T-F7.9** 📣 **Post 6**.

## F8: Lanzamiento (23 mar – campaña de abril de 2027)

- [ ] **T-F8.1** Repetir la búsqueda de competencia (R1).
- [ ] **T-F8.2** Modo demo (`CC_DEMO=1`) con una cartera sintética y una discrepancia sembrada.
- [ ] **T-F8.3** `Dockerfile` y `docker-compose.yml`: la aplicación y DeclaRenta en la misma imagen.
- [ ] **T-F8.4** Despliegue de la demo, por ejemplo en Render o Hugging Face Spaces, solo con el modo demo.
- [ ] **T-F8.5** README final: GIF, resultados de las evaluaciones, arquitectura y reconocimientos.
- [ ] **T-F8.6** Vídeo de 60-90 s y 📣 **lanzamiento**, con hilos en r/SpainFIRE y Rankia.

## Después de v1 (no empezar sin aprobación)

- Criterio de divisas DGT V2422-20 en el motor propio.
- Fondos con traspasos.
- Cripto.
- Contribuciones aguas arriba a DeclaRenta.
- X-Ray de solapamiento de ETF.
