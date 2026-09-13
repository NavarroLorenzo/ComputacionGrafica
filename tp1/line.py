def draw_line_fixed():
  return [(0,0), (1,1), (2,2)] #tupla/vector: es una pos x y en y

def draw_lineal_function(x0, y0, x1, y1):
   points = []
   deltaX = x1 - x0
   deltaY = y1 - y0 #pasos en y
   step = max(abs(deltaX), abs(deltaY)) 

   #pendiente
   if step !=0: 
      #slopeM = deltaY / deltaX #por formula de funcion lineal
      #print(f"pendiente: {slopeM} DeltaX: {deltaX} DeltaY: {deltaY}")
      stepX = deltaX / step #-1 o 1... derecha o izquierda
      stepY = deltaY / step #-1 o 1... arriba o abajo

      for i in range(step + 1): #recorrer horizontalmente 
       # points.append((round(x0+i*stepX), round(y0+i*stepY))) #redondeo para que sea entero
       points.append((round(x0+i*stepX), round(y0+i*stepY))) #redondeo para que sea entero

   return points 

def line_bresenham(x0, y0, x1, y1):
   points = []
   deltaX = abs(x1 - x0)
   deltaY = abs(y1 - y0)
   stepX = 1 if x0 < x1 else -1
   stepY = 1 if y0 < y1 else -1
   err = deltaX - deltaY

   while True:
      points.append((x0, y0))
      if x0 == x1 and y0 == y1:
          break
      err2 = err * 2
      if err2 > -deltaY:
         err = err -deltaY
         x0 += stepX
      if err2 < deltaX:
         err = err + deltaX
         y0 += stepY
   
   return points



  