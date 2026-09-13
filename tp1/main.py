from utils import new_canvas, set_pixel_console, print_canvas, save_to_ppm, save_png
from line import draw_line_fixed, draw_lineal_function, line_bresenham 
from circle import draw_circle_function, draw_circle_middle_point
from scanline import fill_polygon_scanline

canvas = new_canvas(5, 5) #retorna lista de lista 

line = draw_line_fixed() #retorna lista de tuplas
line1 = draw_lineal_function(0, 0, 0, 4) #retorna lista de tuplas
line2 = line_bresenham(0, 0, 4, 4) #retorna lista de tuplas

#recorrer la linea y pintar el canvas en las pos de la linea
for x, y in line1:
    set_pixel_console(canvas, x, y)

#mostrar
print_canvas(canvas)

#probar ppm
WHITE = (255, 255, 255)
RED = (255, 0, 0)

canvas = new_canvas(5, 5, WHITE) #retorna lista de lista
linePix = line_bresenham(0, 0, 4, 4) #retorna lista de tuplas

for x, y in linePix:
    set_pixel_console(canvas, x, y, RED)

save_to_ppm("test.ppm", canvas)
save_png("linea.png", canvas)

canvasCircle = new_canvas(200, 200, WHITE) #retorna lista de lista
circlePix = draw_circle_function(100, 100, 5) #retorna lista de tuplas
for x,y in circlePix:
    set_pixel_console(canvasCircle, x,y, RED)

save_png("circle.png", canvasCircle)

canvasCircle1 = new_canvas(200, 200, WHITE) #retorna lista de lista
circlePix1 = draw_circle_middle_point(100, 100, 5) #retorna lista de tuplas
for x,y in circlePix1:
    set_pixel_console(canvasCircle1, x,y, RED)

save_png("circleMP.png", canvasCircle1)

# carita

YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

caritaCanvas = new_canvas(200, 200, WHITE) 
Cabeza = draw_circle_middle_point(100, 100, 20)
ojos = line_bresenham(95, 95, 95, 100)
boca = draw_circle_middle_point(100, 110, 3)

for x,y in Cabeza:
    set_pixel_console(caritaCanvas, x,y, YELLOW)

for x,y in ojos:
    set_pixel_console(caritaCanvas, x,y, BLACK)
    set_pixel_console(caritaCanvas, x+10, y, BLACK)

for x,y in boca:
    set_pixel_console(caritaCanvas, x,y, RED)

save_png("carita.png", caritaCanvas)

# relleno de poligono con scanline
scanlineCanvas = new_canvas(200, 200, WHITE)
poligono = [(40, 30), (160, 50), (130, 160), (70, 140)]
polygonPix = fill_polygon_scanline(poligono)

for x, y in polygonPix:
    set_pixel_console(scanlineCanvas, x, y, RED)

save_png("scanline.png", scanlineCanvas)

# computadora construida con lineas, circulos y poligonos scanline
GREEN = (0, 160, 0)
BLUE = (0, 100, 255)
LIGHT_BLUE = (190, 230, 255)
GRAY = (150, 150, 150)
LIGHT_GRAY = (210, 210, 210)
DARK_GRAY = (70, 70, 70)

computerCanvas = new_canvas(420, 300, WHITE)

# carcasa y pantalla: poligonos rellenados con scanline
monitorVertices = [(60, 20), (340, 20), (330, 195), (70, 195)]
screenVertices = [(78, 40), (322, 40), (313, 170), (87, 170)]
standVertices = [(175, 195), (225, 195), (245, 230), (155, 230)]
baseVertices = [(125, 230), (275, 230), (310, 245), (90, 245)]
keyboardVertices = [(95, 255), (305, 255), (330, 285), (70, 285)]

for vertices, color in [
    (monitorVertices, DARK_GRAY),
    (screenVertices, LIGHT_BLUE),
    (standVertices, GRAY),
    (baseVertices, GRAY),
    (keyboardVertices, LIGHT_GRAY),
]:
    for x, y in fill_polygon_scanline(vertices):
        set_pixel_console(computerCanvas, x, y, color)

# Contornos y teclas con Bresenham.
for vertices in [monitorVertices, screenVertices, standVertices, baseVertices, keyboardVertices]:
    for index, (x0, y0) in enumerate(vertices):
        x1, y1 = vertices[(index + 1) % len(vertices)]
        for x, y in line_bresenham(x0, y0, x1, y1):
            set_pixel_console(computerCanvas, x, y, BLACK)

for y in [265, 275]:
    for x, y_pixel in line_bresenham(100, y, 300, y):
        set_pixel_console(computerCanvas, x, y_pixel, GRAY)
for x in range(115, 300, 25):
    for x_pixel, y in line_bresenham(x, 258, x, 282):
        set_pixel_console(computerCanvas, x_pixel, y, GRAY)

# Grafico en la pantalla: funcion lineal y Bresenham.
for x, y in draw_lineal_function(110, 140, 190, 80):
    set_pixel_console(computerCanvas, x, y, GREEN)
for x, y in line_bresenham(190, 80, 285, 120):
    set_pixel_console(computerCanvas, x, y, BLUE)

# Camara web con punto medio y mouse con la funcion del circulo.
for x, y in draw_circle_middle_point(200, 30, 5):
    set_pixel_console(computerCanvas, x, y, BLUE)
for x, y in draw_circle_function(365, 265, 18):
    set_pixel_console(computerCanvas, x, y, RED)
for x, y in line_bresenham(365, 252, 365, 266):
    set_pixel_console(computerCanvas, x, y, BLACK)

save_png("computadora.png", computerCanvas)
