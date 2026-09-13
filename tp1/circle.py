import math

def draw_circle_function(cx, cy, radio):
    points = []
    for x in range(-radio, radio+1):
        y = math.sqrt(radio**2 - x**2) #funcion semi circulo 
        y = round(y) #redondeo para que sea entero
        points.append((cx + x, cy + y)) #coloco punto
        points.append((cx + x, cy - y)) #coloco punto opuesto en y para completar circulo 
    return points

#cuanto vale circlePoint 

def draw_circle_middle_point(cx, cy, radio):
    points = []
    x = 0
    y = -radio
    circlePoint = -radio 

    while x < -y:
        #calcular punto medio
        yMid = y + 0.5 #medio pasito
        #circlePoint = x**2 + yMid**2 - radio**2 #formula de la circunferencia
        if circlePoint > 0: #me fui del circulo
            y += 1 #bajo en y
            circlePoint+= 2*(x+y)+1
        else: #me quede dentro del circulo
            circlePoint+= 2*x+1

        points.append((cx+x, cy+y))
        points.append((cx-x, cy-y))
        points.append((cx+x, cy-y))
        points.append((cx-x, cy+y))
        
        points.append((cx+y, cy+x))
        points.append((cx-y, cy-x))
        points.append((cx+y, cy-x))
        points.append((cx-y, cy+x))
        x+=1  
    return points
         

    

