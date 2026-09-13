from PIL import Image 

#funcion para crear un canvas
def new_canvas(width, height, background = "____"):
    return [[background for _ in range(width)] for _ in range(height)]


#funcion para pintar pixeles
def set_pixel_console(canvas, x, y, color = "X"): #win . para buscar emoji
    height = len(canvas)
    width = len(canvas[0])
    if 0 <= x < width and 0 <= y < height:
        canvas[y][x] = color

#funcion para mostrar el canvas final
def print_canvas(canvas):
    for pixel in canvas:
        print("|".join(pixel))


# Función para guardar en un ppm
def save_to_ppm(filename, canvas):
    height = len(canvas)
    width = len(canvas[0])
    with open(filename, "w", encoding="ascii") as f:
        f.write(f"P3\n{width} {height}\n255\n") # "firma"
        for row in canvas:
            line = []
            for (r,g,b) in row:
                line.append(f"{r}, {g}, {b}")
            f.write(" ".join(line) + "\n")


def save_png(filename, canvas):
    h = len(canvas)
    w = len(canvas[0])
    im = Image.new("RGB", (w, h))
    # Flatten de la lista de listas
    pixels_flat = [pixel for row in canvas for pixel in row] # recorre cada fila de img y dentro de cada fila recorre cada pixel para guardarlo en una sola lista.
    im.putdata(pixels_flat)
    im.save(filename, "PNG")