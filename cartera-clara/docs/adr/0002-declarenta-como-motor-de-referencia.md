# ADR 0002: DeclaRenta como motor de referencia, ejecutado como programa externo

**Fecha:** 2026-09-23 · **Estado:** Aceptado

## Decisión
- Se usa la CLI de DeclaRenta (`convert --format json`), fijada en el commit `3f88031` (v0.58.24) e instalada con `make declarenta` en `vendor/declarenta` (sin versionar).
- Se llama con `subprocess`, sin importar su código.
- Los tests de CI usan salidas **grabadas**. Los tests con la CLI real llevan `@pytest.mark.declarenta` y se ejecutan en local.
- Lo que el usuario sube en un formato que DeclaRenta ya lee se le pasa **tal cual**. El resto va en un Flex XML canónico (`referencias/declarenta-integracion.md` §3).

## Alternativas descartadas
- **Portar DeclaRenta a Python:** duplica trabajo y pierde las mejoras que publiquen.
- **Importar su librería desde Node con un puente:** su API no exporta el cálculo de casillas (`computeCasillaBlocksWithFx`), así que la CLI es la interfaz estable.
- **La web declarenta.com:** no tiene API.

## Consecuencias
- La CLI descarga tipos del BCE y necesita red; en local no es un problema.
- Para cambiar de commit: nuevo ADR, volver a grabar las salidas y revisar las diferencias.
- Si un día no compila, se evaluará la imagen Docker `drumsergio/declarenta` (P7).
