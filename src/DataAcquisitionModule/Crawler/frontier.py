"""
frontier.py

Módulo encargado de manejar:

- frontier.csv
- visited.csv

Responsabilidades:

- Cargar frontier
- Guardar frontier
- Cargar visited
- Guardar visited
- Obtener siguiente URL
- Agregar nuevas URLs
"""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FRONTIER_FILE = os.path.join(BASE_DIR, "frontier.csv")
VISITED_FILE = os.path.join(BASE_DIR, "visited.csv")
SEEDS_FILE = os.path.join(BASE_DIR, "seeds.csv")

# SEEDS

def load_seeds():

    try:
        with open(SEEDS_FILE, "r", encoding="utf-8") as f:
            return [
                line.strip()
                for line in f
                if line.strip()
            ]

    except FileNotFoundError:
        return []


# FRONTIER
def load_frontier():
    try:
        with open(FRONTIER_FILE, "r", encoding="utf-8") as f:
            urls = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        urls = []

    if not urls:
        urls = load_seeds()

    frontier_list = [(url, 0) for url in urls]
    frontier_set = set(urls)
    return frontier_list, frontier_set


def save_frontier(frontier_list):
    with open(FRONTIER_FILE, "w", encoding="utf-8") as f:
        for url in frontier_list:
            f.write(url + "\n")



def add_to_frontier(frontier_list, frontier_set, url, depth):
    if url not in frontier_set:
        frontier_list.append((url, depth))
        frontier_set.add(url)


def get_next_url(frontier_list, frontier_set):
    if frontier_list:
        url, depth = frontier_list.pop(0)
        frontier_set.remove(url)
        return url, depth
    return None


# VISITED

def load_visited():
    try:
        with open(VISITED_FILE, "r", encoding="utf-8") as f:
            return set(
                line.strip()
                for line in f
                if line.strip()
            )

    except FileNotFoundError:
        return set()


def save_visited(visited):
    with open(VISITED_FILE, "w", encoding="utf-8") as f:
        for url in visited:
            f.write(url + "\n")


def add_to_visited(visited, url):
    visited.add(url)


# UTILIDADES

def already_seen(url, frontier_set, visited):
    if url in frontier_set:
        return True

    if url in visited:
        return True

    return False