from urllib.robotparser import RobotFileParser
from urllib.parse import urlparse
import time

class RobotsManager:
    """
    Clase para manejar reglas de robots.txt con cache y TTL.
    """

    _parsers = {}  # Cache por dominio
    TTL_SECONDS = 3600  # Tiempo de vida del cache en segundos

    @classmethod
    def can_fetch(cls, url: str, user_agent: str = "*") -> bool:
        """
        Devuelve True si el user-agent puede acceder a la URL según robots.txt.
        Descarga robots.txt una sola vez por dominio.
        """
        parsed = urlparse(url)
        # Validar que la URL tenga esquema y netloc
        if not parsed.scheme or not parsed.netloc:
            # No se puede determinar, permitir por seguridad (o podrías denegar)
            return True
        domain = f"{parsed.scheme}://{parsed.netloc}"
        
        # Verificar si está en caché y no ha expirado
        if domain in cls._parsers:
            parser, timestamp = cls._parsers[domain]
            if time.time() - timestamp < cls.TTL_SECONDS:
                # Caché válida
                if parser is None:
                    # Error previo, permitimos
                    return True
                return parser.can_fetch(user_agent, url)
            else:
                # Caché expirada, eliminar
                del cls._parsers[domain]

        # No está en caché o expiró: descargar robots.txt
        robots_url = f"{domain}/robots.txt"
        rp = RobotFileParser()
        rp.set_url(robots_url)
        try:
            rp.read()
            # Éxito: guardar parser y timestamp
            cls._parsers[domain] = (rp, time.time())
            return rp.can_fetch(user_agent, url)
        except Exception as e:
            # Error: guardamos None para no reintentar hasta que pase el TTL
            print(f"Error al leer robots.txt de {domain}: {e}")
            cls._parsers[domain] = (None, time.time())
            # Por defecto, permitir
            return True