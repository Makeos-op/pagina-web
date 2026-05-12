from fasthtml.common import *
import os

# 1. Definimos la app al inicio para que Vercel la vea primero
app, rt = fasthtml_app(
    pico=False,
    hdrs=(
        Link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&family=Syne:wght@700;800&display=swap"),
    )
)

# 2. Intentamos leer el archivo con una ruta absoluta
path = os.path.join(os.path.dirname(__file__), "paginaweb.html")

try:
    with open(path, "r", encoding="utf-8") as f:
        html_content = f.read()
except FileNotFoundError:
    html_content = "<h1>Error: No se encontró paginaweb.html en el servidor</h1>"

@rt("/")
def get():
    return NotStr(html_content)

# 3. Esto es solo para tu PC, Vercel lo ignora
if __name__ == "__main__":
    serve()