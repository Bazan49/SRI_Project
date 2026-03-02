"""
crawler.py

Módulo principal del crawler.

Responsabilidades:

- Descargar páginas web
- Extraer enlaces
- Filtrar URLs válidas
- Actualizar frontier
- Actualizar visited
"""

import requests
import time

from bs4 import BeautifulSoup
from urllib.parse import urljoin

MAX_DEPTH = 3 

from frontier import (
    load_frontier,
    save_frontier,
    load_visited,
    save_visited,
    get_next_url,
    add_to_frontier,
    add_to_visited,
    already_seen
)

from url_filter import is_valid_url


# CONFIGURACION

DELAY = 1

def fetch(url, max_retries=3):
    """
    Descarga una página web.
    Devuelve el HTML o None si falla.
    """

    for attempt in range(1, max_retries + 1):

        try:
            print(f"\nDownloading ({attempt}/{max_retries}): {url}")

            response = requests.get(url, timeout=8)

            if response.status_code == 200:
                response.encoding = response.apparent_encoding
                return response.text

            print("Status error:", response.status_code)

        except requests.exceptions.Timeout:
            print("Timeout:", url)

        except requests.exceptions.ConnectionError:
            print("Connection error:", url)

        except Exception as e:
            print("Error downloading:", url, e)

        if attempt < max_retries:
            print("Reintentando...")
            time.sleep(2) 

    print("Fallo al descargar después de", max_retries, "intentos:", url)
    return None


# EXTRACCION DE LINKS

def extract_links(html, base_url):

    soup = BeautifulSoup(html, "html.parser")
    links = set()

    for a in soup.find_all("a", href=True):
        link = urljoin(base_url, a["href"])
        if link.startswith("http"):
            links.add(link)

    return list(links)


# CRAWLER PRINCIPAL

def crawl(max_pages=50):

    frontier_list, frontier_set = load_frontier()

    visited = load_visited()

    print("Crawler iniciado")
    print("Frontier:", len(frontier_set))
    print("Visited:", len(visited))

    pages_crawled = 0

    while frontier_list and pages_crawled < max_pages:

        url, depth = get_next_url(frontier_list, frontier_set)

        if not url:
            break

        if url in visited:
            continue

        html = fetch(url)
        if not html:
            continue

        print(f"Crawling: {url} | Profundidad: {depth}")

        links = extract_links(html, url)
        print("Links encontrados:", len(links))

        # solo agregar enlaces si no superan la profundidad
        if depth < MAX_DEPTH:
            for link in links:
                if not already_seen(link, frontier_set, visited):
                    if is_valid_url(link):
                        add_to_frontier(frontier_list, frontier_set, link, depth + 1)

        add_to_visited(visited, url)

        save_frontier([u for u,_ in frontier_list])  # guardamos solo URLs, no profundidad
        save_visited(visited)

        pages_crawled += 1
        print("Paginas crawleadas:", pages_crawled)
        print("Tamano del frontied:", len(frontier_set))

        time.sleep(DELAY)