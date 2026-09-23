# Backlog de Baremo

**Reglas:**
- Se ejecuta **en orden**. Una tarea por commit (o por PR). No se empieza una tarea si la anterior no cumple sus criterios.
- Formato del commit: `[T-F1.3] Parser de lotes y criterios`.
- Al terminar: `make calidad` en verde → marcar la casilla → actualizar el documento de diseño si algo cambió.
- «Referencias» indica qué leer **antes** de escribir código.

---

## F0: Verificación (23 sep – 4 oct 2026)

- [x] **T-F0.0** Esqueleto del repo, `pyproject.toml`, CI y documentación. *(Hecho el 2026-09-23.)*
- [ ] **T-F0.1 (S1)** Ejecutar `make spikes-s1 MES=202605` y guardar el resumen en `docs/resultados/spikes_<fecha>.md`. Si sobra tiempo, repetir con `MES=202601` para comparar meses.
  *Acepta:* JSON con porcentajes; decisiones D1, D2 y D2b anotadas en `01-riesgos…` §4.
- [ ] **T-F0.2 (S1-c)** Copiar 2 entradas reales de `spikes/resultados/s1_ejemplos/` a `tests/fixtures/codice/entry_adjudicada_real_<n>.xml`, borrar `entry_adjudicada_SINTETICA.xml` y actualizar `tests/fixtures/README.md`, `test_estructura.py` y `referencias/codice-placsp.md` §6 (cambiar PENDIENTE por VERIFICADO).
- [ ] **T-F0.3 (S2)** `make spikes-s2`. *Acepta:* regla D3 aplicada.
- [ ] **T-F0.4 (S3)** `make spikes-s3`. Versionar `docs/referencias/codelists/*.json` y los `.gc`. Resolver P1, P2 y P3 de `01-riesgos…` §5.
- [ ] **T-F0.5 (S4)** `make spikes-s4`. *Acepta:* regla D4 aplicada y §10 del diseño actualizado con el coste real.

## F1: Ingesta y datos (5 – 18 oct)

- [ ] **T-F1.1** `baremo/registro.py`: logs en JSON (nivel, módulo, mensaje y campos extra). *Referencias:* diseño §10.
- [ ] **T-F1.2** `ingesta/modelos.py`: `LicitacionFeed`, `LoteFeed`, `CriterioFeed`, `DocumentoFeed`, `ResultadoFeed`. *Referencias:* `referencias/codice-placsp.md` §3-6.
- [ ] **T-F1.3** `ingesta/codice.py`: `iterar_entradas` y `parsear_entrada`, con las reglas de negocio 1-4. *Acepta:* criterios de §8.1 sobre las dos fixtures; un test por regla de negocio.
- [ ] **T-F1.4** `ingesta/codelists.py`: `etiqueta()`. *Acepta:* devuelve la etiqueta real de `TypeCode=1` según el JSON de S3; con un código desconocido devuelve `desconocido:X`.
- [ ] **T-F1.5** `datos/esquema.sql` y `datos/conexion.py` (`conectar(ruta) -> duckdb.DuckDBPyConnection`, que aplica el esquema). *Referencias:* §8.2.
- [ ] **T-F1.6** `datos/carga.py`: `cargar_entradas(conn, entradas)`, con upsert transaccional y hash del NIF. *Acepta:* cargar dos veces la misma fixture no duplica filas; cargar una versión con `actualizado_en` más antiguo no sobrescribe.
- [ ] **T-F1.7** `ingesta/descarga.py` y las órdenes `baremo ingesta historico|incremental`. Test de descarga con `httpx.MockTransport` (sin red).
- [ ] **T-F1.8** `datos/consultas.py`: `buscar_licitaciones`, `ficha`, `lotes_de`, `criterios_de_lote` (propios + comunes) y `resultados_de`.
- [ ] **T-F1.9** Carga real **en tu PC**, de 2024-01 a 2026-08. Anotar en `docs/resultados/ingesta_<fecha>.md`: filas por tabla, tamaño del `.duckdb`, tiempo y memoria. *Acepta:* criterio de rendimiento de §8.1.

## F2: Motor determinista (19 – 25 oct)

- [ ] **T-F2.0** Contrastar el art. 85 RGLCAP con el BOE consolidado (P5) y anotar la fuente y la fecha en el docstring de `motor/temeridad.py`.
- [ ] **T-F2.1** `motor/modelos.py`: `ResultadoTemeridad`, `ParametrosTemeridadPliego` y `FormulaEconomica` (unión discriminada), más la conversión entre `Decimal` y `float`.
- [ ] **T-F2.2** `motor/temeridad.py`. *Acepta:* **T1-T15** como tests parametrizados, todos en verde.
- [ ] **T-F2.3** `motor/expresiones.py`, el evaluador AST seguro. *Acepta:* F4 y F6, más tests de cada nodo prohibido (`Attribute`, `Subscript`, `Lambda`, `Call` a una función no permitida, `Pow` con exponente no constante).
- [ ] **T-F2.4** `motor/formulas.py`: `puntos_precio`, `simular_puntuacion_precio` y `curva_puntos`. *Acepta:* F1, F2, F3 y F5.
- [ ] **T-F2.5** `motor/solvencia.py` y `PerfilEmpresa`; fixture `tests/fixtures/perfiles/pyme_tic.json`. *Acepta:* un test por fila de la tabla de reglas de §8.3, y los tres veredictos.

## F3: Extracción de pliegos (26 oct – 15 nov)

- [ ] **T-F3.1** `llm/precios.py` (tabla de precios con fecha), `llm/costes.py` (inserta en `llamadas_llm`) y `llm/cliente.py`. El cliente expone `extraer_estructurado(modelo, pdf_bytes, prompt, esquema) -> (objeto, uso)`. Usa `client.beta.messages.parse` con fallbacks para Opus 5 y maneja los errores como en §7.4. Los tests usan un cliente falso (protocolo) y no llaman a la API.
- [ ] **T-F3.2** `pliegos/descarga.py` y `pliegos/texto.py`. *Acepta:* un PDF con texto y otro sin capa de texto, construidos en `tests/fixtures/pliegos/` con pypdf o a mano, se clasifican bien.
- [ ] **T-F3.3** `pliegos/esquema_extraccion.py` (exacto al §8.4.3) y `pliegos/prompts.py` (`PROMPT_EXTRACCION_V1`, §8.4.4).
- [ ] **T-F3.4** `pliegos/verificar_citas.py`. *Acepta:* los cuatro resultados, con casos de guion de corte de línea, tildes, tabla desordenada y página ±1.
- [ ] **T-F3.5** `pliegos/extraer.py` y `pliegos/analisis.py`: la máquina de estados completa. Test con un cliente falso que devuelve una `ExtraccionPliego` fija.
- [ ] **T-F3.6** Test manual `@pytest.mark.llm`: 1 pliego real de extremo a extremo. Comprobar `cache_read_input_tokens > 0` en la segunda llamada.
- [ ] **T-F3.7** Golden set: elegir 25 PCAP (§9), anotarlos a mano en `tests/golden/pliegos/` y documentar los criterios de selección.
- [ ] **T-F3.8** `baremo eval extraccion [--modelo] [--batch]`, que genera `docs/resultados/eval_extraccion_<fecha>_<modelo>.md`. *Acepta:* los umbrales de §8.4.
- [ ] **T-F3.9** Escribir `docs/adr/0007-seguridad-llm.md`, con el análisis de la tríada letal y la lista de lo que tiene o no acceso cada llamada.

## F4: Recomendador (16 – 29 nov)

- [ ] **T-F4.1** `recomendador/dataset.py`: filtros, objetivos y variables con corte temporal estricto. *Acepta:* un test que demuestra que una adjudicación posterior a `fecha_publicacion` **no** entra en las variables históricas.
- [ ] **T-F4.2** `recomendador/modelos.py`: B0, B1 y M.
- [ ] **T-F4.3** `recomendador/backtest.py` y `baremo backtest`, que generan `docs/resultados/backtest_<fecha>.md` y `data/backtest_predicciones.parquet`. *Acepta:* criterio de éxito de §8.5.3 evaluado **y publicado, salga como salga**.
- [ ] **T-F4.4** `recomendador/recomendar.py`: `Recomendacion` y el umbral de temeridad estimado.
- [ ] **T-F4.5** `recomendador/comparables.py` y `historico_competencia()`, que usarán la web y el MCP.

## F5: Borradores (30 nov – 6 dic)

- [ ] **T-F5.1** `borradores/crear_plantillas.py` y `declaracion.py`.
- [ ] **T-F5.2** `borradores/deuc.py`: la guía de respuestas.
- [ ] **T-F5.3** `borradores/memoria.py`: índice más preguntas guía generadas por el LLM (con un cliente falso en los tests).
- [ ] *Acepta F5:* tres DOCX generados a partir de la fixture de Oviedo, una extracción fija y `pyme_tic.json`, todos con el pie de IA. Los tests abren los DOCX con python-docx y comprueban los textos clave.

## F6: Web (7 – 27 dic)

- [ ] **T-F6.1** `web/app.py`, la plantilla base (Pico CSS y HTMX desde jsDelivr, pie con la fuente de los datos y el aviso de IA) y `/salud`.
- [ ] **T-F6.2** Buscador y ficha, con `TestClient` de FastAPI sobre una DuckDB de test creada con las fixtures.
- [ ] **T-F6.3** Análisis en segundo plano con consulta periódica por HTMX.
- [ ] **T-F6.4** Estrategia por lote: curva SVG generada en el servidor, `/simular` y recomendación.
- [ ] **T-F6.5** Perfil de empresa.
- [ ] **T-F6.6** «¿Habrías ganado?».
- [ ] **T-F6.7** Descarga de borradores.
- [ ] **T-F6.8** (Opcional) «Pregunta al pliego» con la Citations API (§8.4.7).

## F7: MCP, despliegue y cierre (28 dic – 10 ene 2027)

- [ ] **T-F7.1** `mcp_server/`: las 6 herramientas. *Acepta:* el test de §8.8.
- [ ] **T-F7.2** `Dockerfile` (python:3.12-slim, uv) y `docker-compose.yml`, con `data/` como volumen.
- [ ] **T-F7.3** `baremo exportar-demo`: una DuckDB reducida (24 meses, columnas necesarias, < 300 MB) para desplegar.
- [ ] **T-F7.4** README final: GIF de la demo, resultados del backtest y del golden set, arquitectura, límites conocidos y reconocimientos (Compass, PLACSP).
- [ ] **T-F7.5** Ensayo del guion de demo (§13) y grabación.

## Después de la v1 (no empezar sin aprobación)

- Subir pliegos a mano.
- Importar el perfil desde Holded vía MCP.
- XML oficial del DEUC (ESPD-EDM).
- Plataformas autonómicas (sindicación 1044).
- Simulación Monte Carlo de rivales.
- Alertas.
