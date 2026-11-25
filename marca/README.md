El Yopal es un kiosco de barrio con café recién hecho, galletas artesanas, snacks, bebidas y revistas, bajo un toldo granate y entre plátanos de sombra. La marca tiene que parecer tan cercana como el propio kiosco: colores planos y alegres, letras gordas y redondas, pegatinas y un sol que sonríe. Este sistema sirve para todo: Instagram, la web, la carta, la pizarra y lo que se imprima.

## Esencia

- **Qué somos**: tu parada de cada día. Café para llevar, una galleta hecha ese día y lo que te haga falta de camino.
- **Cómo nos vemos**: el granate del toldo como color principal, el sol del logotipo como acento y el Solete como personaje.
- **De dónde viene**: el toldo granate con el logotipo y el rótulo URBAN EXPRESS, la madera cálida del mostrador, la pizarra escrita a mano de la puerta y el cartel de combos «2 productos por 3,45 €».

## Voz y tono

- Tuteamos siempre. Frases cortas, como se habla en el mostrador: «Ya estamos abiertos», «El café ya está listo», «Elige 2 y listo».
- Con humor ligero y sin exagerar: «Pregunta seria: ¿equipo choco o equipo Lotus?».
- Titulares de una a cuatro palabras. Los detalles van en el texto del post, no en la imagen.
- Mayúsculas solo en el estilo `rotulo` (antetítulos, etiquetas y botones). Los titulares van en minúscula con la inicial en mayúscula.
- Precios en formato español: coma decimal y euro detrás con espacio: `2,80 €`.
- Emojis en los textos de las publicaciones, uno o dos como mucho y siempre de la misma familia: ☀️ 🍪 ☕. Nunca dentro de los diseños: ahí está el Solete.

## Color

La regla de reparto en cualquier pieza: más o menos 60 % `granate` o `crema` de fondo, 25 % el otro de los dos, 10 % `sol` y 5 % `cielo` o `galleta`.

- `granate` es la marca. Fondo de los posts principales, botones y logotipo sobre crema.
- `crema` es el fondo claro y el color del texto sobre granate. No es blanco: nunca uses `#FFFFFF` de fondo.
- `sol` es para lo que tiene que saltar a la vista: precios, ofertas, el Solete y los rayos del logo. Sobre `sol` el texto va siempre en `granate` o `granate-hondo`.
- `cielo` refresca: bebidas frías, novedades e historias. Texto encima en `granate` o `granate-hondo`.
- `galleta` solo para detalles pequeños, nunca para texto.
- `granate-hondo` es la sombra de las pegatinas y el color de texto sobre colores claros vivos.
- En la web, usa los tokens de superficie (`superficie`, `superficie-alt`, `tinta`, `tinta-suave`, `linea`), que cambian con el tema oscuro. Los posts e imágenes de redes van siempre en tema `claro`.

## Tipografía

Las cuatro familias son gratuitas en Google Fonts.

- **Bagel Fat One** (`display`): titulares, nombres de producto y precios. Estilos `titular-xl`, `titular-l`, `titular-m` y `precio`. Pocas palabras y muy grandes, nunca en párrafos.
- **Barlow Condensed** en negrita (`rotulo`): el eco del rótulo URBAN EXPRESS del toldo. Siempre en mayúsculas con espaciado: `rotulo-l` y `rotulo`.
- **Figtree** (`texto`): todo lo que se lee de seguido. `texto-l`, `texto` y `texto-s`.
- **Caveat Brush** (`mano`): las notas como de pizarra («¡recién horneada!»). Como mucho una por pieza y ligeramente girada.

## Logotipo y mascota

- Usa siempre los archivos del grupo **Logos**. Versión principal: `logotipo-granate.svg` sobre `crema`; sobre `granate`, `logotipo-crema.svg`. Reglas completas en el componente Logotipo.
- El **Solete** (grupo **Mascota**) es el sol del logotipo hecho pegatina. Tiene tres caras: feliz (por defecto), guiño (ofertas) y sorpresa (novedades). Uno por pieza.
- Foto de perfil en todas las redes: `avatar-perfil.svg`.

## Elementos gráficos

- **Pegatinas**: precios, etiquetas y el Solete se tratan como pegatinas: borde blanco o `granate-hondo`, `sombra-pegatina` (dura, sin difuminar) y un giro de pocos grados.
- **Bloques de color** con `radio-l` para separar foto y texto.
- **Palabra repetida**: una palabra en `titular-xl` repetida en líneas rellenas y en contorno (componente PostTipografico).
- **Galletas dibujadas**: círculos `galleta` con pepitas `granate-hondo`. Sirven de marcador o de relleno, pero la foto real del producto siempre gana.
- Formas permitidas: círculos, píldoras y rayos redondeados. Nada de degradados, sombras difuminadas en redes ni texturas.

## Iconografía

Iconos propios de trazo (grupo **Iconos**): 24 × 24, trazo de 2 px con puntas redondas, en `granate`. Hay café, galleta, para llevar, bebida, snack, revista, sol y ubicación. En redes se meten dentro de círculos `crema` o `sol` con borde `granate-hondo`. No mezcles con otras familias de iconos ni con emojis dentro del diseño.

## Fotografía

- Luz cálida: por la mañana o con el kiosco encendido. Nada de filtros fríos o desaturados.
- Producto: una mano sosteniendo la galleta o el vaso, sobre fondo liso `cielo`, `sol`, `granate` o la pared crema. Producto recortado sin fondo para posts de producto.
- El kiosco: fachada con el toldo, el mostrador de madera iluminado y el rincón de revistas (grupo **Fotos**).
- El texto nunca va encima de la foto: va en un bloque de color al lado o debajo.

## Redes sociales

- Formatos: post 1080 × 1350 px (4:5), historia 1080 × 1920 px (9:16) y avatar 1080 × 1080 px.
- Márgenes de seguridad: 96 px en posts y 250 px arriba y abajo en historias.
- Rejilla del feed: alterna fondo `granate`, fondo claro (`crema`, `sol` o `cielo`) y foto real, para que ningún color se repita dos veces seguidas en la misma fila.
- Plantillas: PostProducto, PostOferta, PostTipografico, PostFoto, Historia, Carta y Pizarra.
- Logotipo siempre en una esquina o en la banda inferior, pequeño. El protagonista es el producto.

## Web

- Fondo `superficie`, texto `tinta`, secciones separadas por `esp-16` y bandas `superficie-alt`.
- Botones: componente Boton (uno principal por pantalla). Productos: TarjetaProducto en rejilla.
- Foco de teclado: anillo `foco` de 3 px con 2 px de separación, visible en los dos temas.
- Cabecera con `bloque-granate.svg` (o `bloque-crema.svg` en tema oscuro o sobre granate).
