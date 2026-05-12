from fasthtml.common import *

# Configuramos la app
app, rt = fasthtml_app(
    pico=False, # Desactivamos Pico CSS para que no choque con tus estilos personalizados
    hdrs=(
        Link(rel="preconnect", href="https://fonts.googleapis.com"),
        Link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&family=Syne:wght@700;800&display=swap"),
    )
)

# Aquí pegamos el contenido de tu HTML (puedes leerlo del archivo o pegarlo como string)
with open("paginaweb.html", "r", encoding="utf-8") as f:
    html_content = f.read()

@rt("/")
def get():
    # NotStr permite pasar HTML puro sin que FastHTML lo escape como texto
    return NotStr(html_content)

serve()