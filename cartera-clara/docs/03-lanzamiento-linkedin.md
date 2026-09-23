# Plan de lanzamiento: construir en público

Objetivo: que el proyecto llegue a gente que invierte y a recruiters y equipos de IA. **Sin prisas**: un post por fase, cada uno con algo que se pueda enseñar.

## Reglas de formato

Proceden de fuentes de marketing, así que son orientativas; ver el informe 03.

- **Carrusel en PDF** o **vídeo nativo** mejor que texto solo.
- **El enlace va en el primer comentario**: los enlaces en el post reducen el alcance.
- Publicar a una hora en la que puedas **responder durante la primera hora**.
- Estructura: **problema con cifra y fecha → decisión técnica en 3 puntos → demo → qué viene**.
- Usar siempre los números reales del proyecto (evaluaciones y discrepancias). Los fallos que el sistema detecta enganchan más que los éxitos.
- Mencionar a DeclaRenta y a su autor cuando se use su motor.

## Serie

| # | Cuándo | Gancho | Formato | Material |
|---|---|---|---|---|
| 1 | Fin de F2 | «Hacienda aplica el FIFO por valor, no por bróker. Si tienes el mismo ETF en dos brókeres, tu informe está mal por definición.» | Carrusel con el ejemplo numérico | GIF de la web v0.1 |
| 2 | Fin de F3 | «He construido un importador con IA que no se inventa números: cita cada fila y cuadra los totales.» | Vídeo de 45 s | Tabla de la evaluación (campos %, citas %) |
| 3 | Fin de F4 | «El error de Trade Republic en la Renta 2025, detectado automáticamente.» | Carrusel antes/después | Conciliación con la fixture ficticia |
| 4 | Fin de F5 | «Mi asistente intentó darme una cifra que no existía. El guardián la bloqueó.» | Captura del bloqueo + métricas | Evaluación del agente |
| 5 | Fin de F6 | «¿Cuánto te debe Alemania? Si tienes acciones alemanas, probablemente más de lo que crees.» | Carrusel con cálculo | Recuperador + MCP en Claude |
| 6 | Fin de F7 | «Dos motores fiscales independientes que se vigilan: X casillas, 0 discrepancias (o estas N, y por qué).» | Post técnico + diagrama | Informe doble motor |
| 🚀 | Apertura de la campaña (abr 2027) | «Cartera Clara 1.0: tu Renta de inversor, clara. Gratis, open source y local.» | Vídeo de 60-90 s + demo pública | Todo |
| 7 | 3-4 semanas después | Retrospectiva con métricas reales (estrellas, usuarios de la demo, discrepancias encontradas) | Texto + gráfico | — |

## Canales complementarios

- **r/SpainFIRE y Rankia**, en el lanzamiento: un post útil que explique el problema, sin tono comercial.
- **GitHub:** README con GIF, badges de CI y enlace a la demo; `topics`: `irpf`, `fifo`, `spain`, `mcp`, `claude`, `llm-evals`.
- **Hacker News / r/LocalLLaMA** (en inglés): el ángulo del «guardián numérico» y el doble motor, que interesa fuera de España.
