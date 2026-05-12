from fasthtml.common import *

# 1. Definimos la app (Vercel buscará esta variable 'app')
app, rt = fasthtml_app(
    pico=False,
    hdrs=(
        Link(rel="preconnect", href="https://fonts.googleapis.com"),
        Link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&family=Syne:wght@700;800&display=swap"),
    )
)

# 2. Cargamos tu HTML
with open("paginaweb.html", "r", encoding="utf-8") as f:
    html_content = f.read()

@rt("/")
def get():
    return NotStr(html_content)

# 3. IMPORTANTE: Solo ejecutar serve() si estás en tu PC local.
# Vercel ignorará esto, pero ayuda a que no dé error en la nube.
if __name__ == "__main__":
    serve()