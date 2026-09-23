# Baremo

> **Cuánto ofertar, cuántos puntos sacarás y el borrador de tu oferta**, para cualquier licitación pública española, con cada dato citado del pliego.

**Estado:** diseño cerrado, en la fase F0 (verificación de datos). Aún no hay funcionalidad de usuario.

En 2025 el sector público español contrató unos 180.000 M€. Las pymes firman el 67,5 % de los contratos, pero se llevan solo el 7 % del dinero. Los buscadores de licitaciones ya existen. Lo que le falta a una pyme es saber **cuánta baja ofrecer sin caer en temeridad**, **cuántos puntos sacaría** con la fórmula de ese pliego y **qué hay que presentar**. Baremo responde a eso con los datos abiertos de PLACSP:

1. **Simulador de puntuación.** Extrae del pliego la fórmula económica y los criterios con su peso, y calcula tus puntos para cada baja posible.
2. **Umbral de temeridad.** Calcula a partir de qué baja tu oferta sería anormalmente baja: art. 85 del RGLCAP o los parámetros propios del pliego.
3. **Baja recomendada con backtest.** Estima la baja ganadora con el histórico de adjudicaciones comparables. El modelo se evalúa contra adjudicaciones reales, sin mirar el futuro. Incluye el modo «¿habrías ganado?».
4. **Encaje de solvencia.** Compara tu perfil con los requisitos del pliego. El modelo extrae los requisitos y el código decide.
5. **Borradores.** Genera la declaración responsable o el DEUC y el índice de la memoria técnica, organizado por criterios de juicio de valor.
6. **Servidor MCP** para usar todo lo anterior desde Claude u otro agente.

Baremo nunca presenta nada por ti y no es asesoramiento jurídico.

## Documentación

| Documento | Para qué |
|---|---|
| [docs/00-documento-de-diseno.md](docs/00-documento-de-diseno.md) | **El documento de diseño.** Qué se construye, cómo, con qué datos y en qué orden. Es la fuente de verdad. |
| [docs/01-riesgos-y-verificaciones.md](docs/01-riesgos-y-verificaciones.md) | Riesgos, qué se ha verificado ya y qué decide cada spike. |
| [docs/02-backlog.md](docs/02-backlog.md) | Tareas numeradas, con criterios de aceptación, en orden de ejecución. |
| [docs/adr/](docs/adr/) | Decisiones de arquitectura y por qué se tomaron. |
| [docs/referencias/](docs/referencias/) | Referencia técnica: CODICE/PLACSP, normativa de temeridad y fórmulas, codelists. |
| [CLAUDE.md](CLAUDE.md) | Reglas para Claude Code al trabajar en este proyecto. |

## Arrancar (desarrollo)

Requisitos: [uv](https://docs.astral.sh/uv/) y Python 3.12 o superior.

```bash
cd baremo
uv sync                 # instala dependencias
make calidad            # ruff + mypy --strict + pytest
cp .env.example .env    # solo hace falta ANTHROPIC_API_KEY a partir de la fase F3
```

Primer paso real, desde una red con acceso a PLACSP (fase F0):

```bash
make spikes-s1 MES=202605   # qué campos trae el feed y con qué cobertura
```

## Licencia

MIT. Parte del repositorio [ai-engineering-journey](../README.md).
