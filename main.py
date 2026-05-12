from fasthtml.common import *
import os

# 1. Definimos la app. Vercel busca este objeto 'app'.
app, rt = fasthtml_app(
    pico=False,
    hdrs=(
        Link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&family=Syne:wght@700;800&display=swap"),
    )
)

# 2. Ruta absoluta para evitar errores de 'File Not Found' en Vercel
CUR_DIR = os.path.dirname(__file__)
HTML_PATH = os.path.join(CUR_DIR, "index.html")

def get_html_content():
    try:
        with open(HTML_PATH, "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return "<h1>Error: No se pudo cargar paginaweb.html</h1>"

@rt("/")
def get():
    return NotStr(get_html_content())

# Esto permite que Vercel importe 'app' sin ejecutar el servidor local
if __name__ == "__main__":
    serve()