import math


def _validate_polygon(vertices):
    """Valida y normaliza los vertices que se usaran para el relleno."""
    try:
        vertices = list(vertices)
    except TypeError as error:
        raise ValueError("Los vertices deben formar una secuencia de puntos") from error

    # Se permite recibir el primer vertice repetido al final para cerrar el poligono.
    if len(vertices) > 1 and vertices[0] == vertices[-1]:
        vertices.pop()

    if len(vertices) < 3:
        raise ValueError("Un poligono necesita al menos tres vertices")

    normalized_vertices = []
    for vertex in vertices:
        if not isinstance(vertex, (tuple, list)) or len(vertex) != 2:
            raise ValueError("Cada vertice debe ser una tupla (x, y)")

        x, y = vertex
        if isinstance(x, bool) or isinstance(y, bool) or not isinstance(x, int) or not isinstance(y, int):
            raise ValueError("Las coordenadas de los vertices deben ser enteras")
        normalized_vertices.append((x, y))

    if len(set(normalized_vertices)) < 3:
        raise ValueError("Un poligono necesita al menos tres vertices distintos")

    # Un area igual a cero no representa una superficie que se pueda rellenar.
    double_area = 0
    for index, (x0, y0) in enumerate(normalized_vertices):
        x1, y1 = normalized_vertices[(index + 1) % len(normalized_vertices)]
        double_area += x0 * y1 - x1 * y0
    if double_area == 0:
        raise ValueError("Los vertices no forman un poligono con area")

    return normalized_vertices


def fill_polygon_scanline(vertices):
    """Devuelve los pixeles interiores de un poligono usando scanline.

    Cada scanline se toma en el centro de la fila (y + 0.5). Los bordes se
    mantienen activos en el intervalo semiabierto [y_min, y_max): de esta
    manera, en un vertice regular solo participa uno de sus bordes y en un
    minimo/maximo local se aplica la regla correspondiente para un vertice
    critico. Los bordes horizontales no se agregan a la tabla de bordes.
    """
    vertices = _validate_polygon(vertices)

    # Tabla de bordes inactivos. Cada borde pasa a activos en y_start y se
    # elimina antes de y_end. x se actualiza sumando inverse_slope en cada
    # scanline, sin volver a calcular la ecuacion de la recta.
    inactive_edges = {}
    last_scanline = None

    for index, (x0, y0) in enumerate(vertices):
        x1, y1 = vertices[(index + 1) % len(vertices)]

        # Los bordes horizontales no generan intersecciones utiles.
        if y0 == y1:
            continue

        if y0 < y1:
            x_min, y_min, x_max, y_max = x0, y0, x1, y1
        else:
            x_min, y_min, x_max, y_max = x1, y1, x0, y0

        inverse_slope = (x_max - x_min) / (y_max - y_min)
        y_start = math.ceil(y_min - 0.5)
        y_end = math.ceil(y_max - 0.5)

        # Interseccion inicial en el centro de y_start. Las siguientes se
        # obtienen incrementalmente con x += inverse_slope.
        x_start = x_min + ((y_start + 0.5) - y_min) * inverse_slope
        edge = {
            "x": x_start,
            "inverse_slope": inverse_slope,
            "y_end": y_end,
        }
        inactive_edges.setdefault(y_start, []).append(edge)

        if last_scanline is None or y_end > last_scanline:
            last_scanline = y_end

    active_edges = []
    points = []

    if not inactive_edges:
        return points

    first_scanline = min(inactive_edges)

    # Se recorre de arriba hacia abajo: en un canvas, y aumenta hacia abajo.
    for scanline in range(first_scanline, last_scanline):
        # Un borde que termina en esta fila queda inactivo. Esta regla junto
        # con la activacion en y_start reconoce vertices regulares y criticos.
        active_edges = [edge for edge in active_edges if edge["y_end"] > scanline]
        active_edges.extend(inactive_edges.get(scanline, []))
        active_edges.sort(key=lambda edge: edge["x"])

        # Se toman las intersecciones de a pares y se rellena alternadamente.
        for edge_index in range(0, len(active_edges) - 1, 2):
            x_left = active_edges[edge_index]["x"]
            x_right = active_edges[edge_index + 1]["x"]

            # Se pinta todo pixel cuyo centro horizontal esta entre ambas
            # intersecciones. El extremo derecho se deja fuera del intervalo.
            x_start = math.ceil(x_left - 0.5)
            x_end = math.ceil(x_right - 0.5)
            for x in range(x_start, x_end):
                points.append((x, scanline))

        # Analisis incremental: avanzando una fila, cada interseccion cambia
        # solamente por la pendiente inversa del borde.
        for edge in active_edges:
            edge["x"] += edge["inverse_slope"]

    return points


# Alias corto para usar el nombre del algoritmo desde main.py si se prefiere.
scanline = fill_polygon_scanline
