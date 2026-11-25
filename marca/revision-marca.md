# Revisión de la identidad de El Yopal

Hecha con la skill `brand-identity` (`.claude/skills/brand-identity`): auditoría de fuentes (`brand.py critique`), auditoría de paleta (`palette_audit.py`) y comparación con su lista de recursos que más repiten las herramientas de IA (`assets/ai-defaults.json`).

## Comprobaciones obligatorias
- Contraste: pasa. Texto 16,3:1, crema sobre granate 8,3:1, granate hondo sobre sol 9,9:1 y sobre azul 4,8:1.
- Idioma: las tres fuentes cubren el español completo.
- Licencias: Sansita, Figtree y Caveat Brush, OFL (uso libre en logo, web e impresión).
- Logo: vectorial, una tinta, legible desde 90 px. A 32 y 16 px no se lee, por eso se añade `icono-pequeno.svg`.

## Cambios
| Antes | Medición | Después |
|---|---|---|
| Fraunces (titulares) | Letra de titulares más repetida por las IA | Sansita 900: 0 avisos, cifras tabulares |
| Barlow Condensed (rótulos) | Fuente «por defecto de sector»; I/l iguales | Figtree en mayúsculas |
| Color galleta #D99148 | Zona de acento dorado típico | Retirado de la paleta |
| Iconos de línea 2 px | Cliché de juego de iconos genérico | Ilustraciones a mano en línea |
| Avatar con logotipo en todos los tamaños | Ilegible a 32 y 16 px | Icono: Solete sobre granate por debajo de 48 px |
| Sol sobre crema o kraft | 1,42:1 y 1,64:1 | Prohibido; ahí, granate |

## Lo que se mantiene a propósito
- Crema #FFF4E2: cae en la zona de «fondo crema típico», pero viene de los referentes del cliente y de la celosía del kiosco, y va siempre con granate.
- Avisos menores: Figtree tiene I/l parecidas a 48 px (no se usa en códigos ni cifras sueltas) y Caveat Brush tiene un solo peso (solo para notas cortas).
