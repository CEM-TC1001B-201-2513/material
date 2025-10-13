import streamlit as st

st.header("Problemática")

st.write("""

# Lenguaje Markdown (Título/Encabezado)
---
## Uso del lenguaje (Subencabezado)

### Listas ordenadas
1. Primer elemento
    1. Primer subelemento
2. Segundo elemento
3. Tercer elemento

### Listas no ordenadas
- Primer elemento
    - Primer subelemento
- Segundo elemento
- Tercer elemento

Éste es un ejemplo de párrafo.
Este texto sigue siendo parte del párrafo.

Éste es otro *párrafo*.
Se necesitan **dos** saltos de línea para iniciar
otro ***párrafo***.

*Cursivas*
**Negritas (bold)**
***Cursivas y negritas***

### Colores

Este texto es de color :blue[**azul**].
Este texto tiene fondo :red-background[rojo].
:red-background[:blue[Este texto es azul con fondo rojo]]

### Íconos

Emojis (Streamlit emoji shortcodes) :smiling_imp:

Material icons (Google) :material/swipe_right:

### Enlaces a sitios externos

Enlace https://experiencia21.tec.mx/courses/592665

Enlace en un [texto definido](https://experiencia21.tec.mx/courses/592665)

### Tablas

| Matrícula | Nombre |
| --- | --- |
| 74583993 | Pedro |
| 48582845 | Juan |
| 948757503 | Lorena |

### Latex

Ecuaciones: $\sum_{k=1}^{n}k^{2}-5$

""")

st.image("imágenes/pexels-pixabay-416160.jpg")
st.caption("Tomado de: https://www.pexels.com/photo/close-up-photo-of-cute-sleeping-cat-416160/")

tabla = {
    "Matrícula": [53434, 246776, 2434565],
    "Nombre": ["Marta", "Luis", "Ian"]
    }

st.table(tabla)

st.video("https://www.youtube.com/watch?v=UEqTIwRrWvA")

c1, c2 = st.columns(2)

c1.write("Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?")
c2.image("imágenes/pexels-pixabay-208984.jpg")
c2.caption("Imagen tomada de: pexels-pixabay-208984.jpg")

c3, c4 = st.columns([0.7, 0.3])

c3.write("Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?")
c4.image("imágenes/pexels-pixabay-208984.jpg")
c4.caption("Imagen tomada de: pexels-pixabay-208984.jpg")
