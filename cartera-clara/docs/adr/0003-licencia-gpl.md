# ADR 0003: Licencia GPL-3.0-or-later

**Fecha:** 2026-09-23 · **Estado:** Aceptado

## Contexto
DeclaRenta es GPL-3.0. Reutilizamos algunas de sus fixtures de test y lo distribuimos junto a Cartera Clara en la imagen Docker de la F8.

## Decisión
Cartera Clara se publica bajo **GPL-3.0-or-later**. El fichero `LICENSE` es el texto oficial, copiado del repositorio de DeclaRenta. Los reconocimientos van en el README y en `tests/fixtures/README.md`.

## Consecuencias
Quien redistribuya versiones modificadas tiene que publicar su código, algo coherente con un proyecto open source. MIT no es posible sin renunciar a las fixtures y a la imagen conjunta.
