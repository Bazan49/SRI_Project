"""
url_filter.py

Módulo encargado de validar URLs.
"""

from urllib.parse import urlparse

ALLOWED_DOMAINS = [
    "cubadebate.cu",
    "oncubanews.com",
    "bbc.com/mundo",
    "lanacion.com",
    "telesurtv.net",
    "actualidad.rt.com",
    "presidencia.gob.cu",
    "telemundo.com/noticias"
]


BLOCKED_EXTENSIONS = [

    ".pdf",
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".zip",
    ".rar",
    ".mp4",
    ".mp3",
    ".css",
    ".js"

]


def is_valid_url(url):

    try:
        parsed = urlparse(url)

        if parsed.scheme not in ["http", "https"]:
            return False

        allowed = False

        for domain in ALLOWED_DOMAINS:
            if domain in parsed.netloc:
                allowed = True
                break

        if not allowed:
            return False
        
        for ext in BLOCKED_EXTENSIONS:
            if parsed.path.lower().endswith(ext):
                return False
        return True

    except:
        return False