# Cartera Clara

> **Tu Renta de inversor, clara.** Todos tus brókeres en un sitio, el cálculo fiscal verificado por **dos motores independientes** y una IA que te lo explica **sin inventarse un solo número**.

**Estado:** diseño cerrado (fase F0). Aún no hay funcionalidad de usuario.

## El problema

- **El FIFO es global por valor, no por bróker.** Si tienes el mismo ETF en dos brókeres, el informe fiscal de cada uno está mal por definición.
- En la Renta 2025, el informe de **Trade Republic** (más de 2 M de clientes en España) descuadró miles de borradores: puso ganancias como rendimientos del capital mobiliario y omitió las pérdidas.
- **Alemania retiene un 26,375 % y Suiza un 35 %**, pero en España solo se deduce hasta el límite del convenio (normalmente un 15 %). El exceso se reclama al país de origen, y casi nadie lo hace.

## Qué hace (todo en uno)

1. **Importa todo.** Los formatos conocidos se leen con parsers deterministas. Los raros (PDF, CSV desconocidos) los lee un **importador con IA** que cita la fila o la página de cada dato y cuadra los totales antes de aceptarlos.
2. **Calcula con dos motores:**
   - [DeclaRenta](https://github.com/GeiserX/DeclaRenta), la referencia open source (FIFO global, tipos del BCE, regla de los 2 meses, doble imposición, 720);
   - un **motor propio en Python**.

   Se comparan en cada cálculo, y si discrepan, te avisa.
3. **Concilia con Hacienda.** Lee tus datos fiscales de la AEAT y te dice qué casilla del borrador está mal y por qué.
4. **Recupera tus retenciones.** Calcula cuánto te debe cada país por exceso de retención y cómo reclamarlo.
5. **Te lo explica.** Un asistente responde «¿por qué me sale esto en la 0328?». Cada cifra sale de una herramienta y un guardián bloquea cualquier número que no esté respaldado.
6. **Servidor MCP**, para preguntar por tu Renta desde Claude.

**Privacidad:** todo se ejecuta en tu ordenador y tus extractos nunca se suben a ningún servidor. Las funciones de IA envían a la API de Anthropic solo el documento que tú decidas analizar.

**Límites:** no es asesoramiento fiscal ni de inversión, y no recomienda qué comprar o vender. Es un borrador que revisas tú.

## Documentación

| Documento | Para qué |
|---|---|
| [docs/00-documento-de-diseno.md](docs/00-documento-de-diseno.md) | **El diseño.** Qué, cómo, con qué datos y en qué orden. Es la fuente de verdad. |
| [docs/01-riesgos-y-verificaciones.md](docs/01-riesgos-y-verificaciones.md) | Riesgos, lo ya verificado y lo que decide cada spike. |
| [docs/02-backlog.md](docs/02-backlog.md) | Tareas en orden, con criterios de aceptación. |
| [docs/03-lanzamiento-linkedin.md](docs/03-lanzamiento-linkedin.md) | Plan de publicación: construir en público y lanzamiento en la campaña de la Renta 2027. |
| [docs/adr/](docs/adr/) | Decisiones de arquitectura. |
| [docs/referencias/](docs/referencias/) | Fiscalidad, integración con DeclaRenta y formatos de los brókeres. |
| [CLAUDE.md](CLAUDE.md) | Reglas para Claude Code. |

## Desarrollo

```bash
cd cartera-clara
uv sync
make calidad          # ruff + mypy --strict + pytest (sin red ni LLM)
make declarenta       # opcional: descarga y compila el motor de referencia (necesita Node >= 22.13)
```

## Licencia y reconocimientos

**GPL-3.0-or-later** (ver [LICENSE](LICENSE) y ADR 0003). El motor de referencia es [DeclaRenta](https://github.com/GeiserX/DeclaRenta) de GeiserX (GPL-3.0). Cartera Clara lo ejecuta como programa externo y reutiliza algunas de sus fixtures de test, reconocidas en `tests/fixtures/README.md`.
