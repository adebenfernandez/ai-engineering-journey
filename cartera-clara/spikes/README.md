# Spikes de la F0 (se ejecutan en tu PC)

Nada de lo que produzcan va al repositorio salvo **fixtures ficticias** escritas a mano. `spikes/resultados/` y `data/` están en `.gitignore`.

## S1: DeclaRenta en local

```bash
cd cartera-clara
node --version                 # tiene que ser >= 22.13 (o 20.19+)
make declarenta                # clona, fija el commit, npm ci y compila
node vendor/declarenta/dist/cli.js convert -i tests/fixtures/flex/canonico_basico.xml -y 2024 -f json
#   → ganancia_neta 78.60 y 0588 = 1.50 (como en tests/fixtures/flex/canonico_basico.esperado.json)
node vendor/declarenta/dist/cli.js convert -i ~/Descargas/<tu_extracto> -y 2025 -f json > spikes/resultados/mi_2025.json
```

Compara las casillas con tu Renta 2025 presentada y anota las diferencias en `docs/01-riesgos-y-verificaciones.md` §4 (**solo** las diferencias, sin importes personales si no quieres).

## S2: tus datos fiscales de la AEAT

1. Renta Web → «Datos fiscales» → descargar el PDF.
2. Comprueba que tiene texto:
   ```bash
   uv run python -c "from pypdf import PdfReader; r=PdfReader('ruta.pdf'); print(len(r.pages)); print(r.pages[0].extract_text()[:1500])"
   ```
3. Describe las secciones (títulos, columnas y dónde aparecen las entidades y los importes) en `docs/referencias/formatos-brokers.md` §2.
4. Escribe a mano `tests/fixtures/aeat/datos_fiscales_ficticio.txt`: la misma estructura con datos inventados.

## S3: informe fiscal de Trade Republic (u otro extracto no soportado)

Mismo procedimiento que en S2 → `tests/fixtures/ia/`.

## S4: tokens por documento

```bash
export ANTHROPIC_API_KEY=...
uv run python - <<'PY'
import base64, sys, anthropic
c = anthropic.Anthropic()
for ruta in sys.argv[1:] or ["datos_fiscales.pdf"]:
    datos = base64.standard_b64encode(open(ruta, "rb").read()).decode()
    r = c.messages.count_tokens(model="claude-opus-5", messages=[{"role": "user", "content": [
        {"type": "document", "source": {"type": "base64", "media_type": "application/pdf", "data": datos}},
        {"type": "text", "text": "Extrae las operaciones."}]}])
    print(ruta, r.input_tokens, "tokens ≈", round(r.input_tokens * 5 / 1e6, 4), "USD de entrada (Opus 5)")
PY
```

## S5: competencia a mano

Sube los **mismos** extractos a declarenta.com, MiCartera (si hay prueba gratuita) y AceleraFiscal. Anota:
- si concilian con la AEAT;
- si calculan el exceso reclamable por país;
- si explican las casillas;
- qué brókeres fallan.

Lee también r/SpainFIRE, buscando "renta", "trade republic", "doble imposición" y "720".
