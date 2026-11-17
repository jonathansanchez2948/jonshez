import os
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer

# Cambia estos valores, haz commit y push para ver el despliegue continuo en acción
VERSION = "1.0.0"
MENSAJE = "Hola en GitHub"

PAGINA = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Despliegue continuo</title>
  <style>
    body {{ font-family: system-ui, sans-serif; background: #0f172a; color: #e2e8f0;
           display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0; }}
    .tarjeta {{ background: #1e293b; padding: 2rem 3rem; border-radius: 12px; text-align: center; }}
    h1 {{ margin-top: 0; }}
    .version {{ color: #38bdf8; font-weight: bold; }}
    small {{ color: #94a3b8; }}
  </style>
</head>
<body>
  <div class="tarjeta">
    <h1>{mensaje}</h1>
    <p>Versión desplegada: <span class="version">{version}</span></p>
    <small>Servidor iniciado: {hora}</small>
  </div>
</body>
</html>
"""

HORA_INICIO = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class Manejador(BaseHTTPRequestHandler):
    def do_GET(self):
        """Responde con la página HTML a cualquier petición GET."""
        cuerpo = PAGINA.format(mensaje=MENSAJE, version=VERSION, hora=HORA_INICIO).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(cuerpo)))
        self.end_headers()
        self.wfile.write(cuerpo)


if __name__ == "__main__":
    # El puerto se toma de la variable PORT (útil en servicios de hosting)
    puerto = int(os.environ.get("PORT", 8000))
    print(f"Servidor en http://localhost:{puerto} (versión {VERSION})")
    HTTPServer(("0.0.0.0", puerto), Manejador).serve_forever()
