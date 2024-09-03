def line():
   A = float(input("Ingrese el coeficiente A: "))
   B = float(input("Ingrese el coeficiente B: "))
   X1 = float(input("Ingrese la coordenada X1: "))
   X2 = float(input("Ingrese la coordenada X2: "))

   print(f"\nEl coeficiente A de su ecuación de la recta es: {A}")
   print(f"El coeficiente B de su ecuación de la recta es: {B}")
   print(f"El valor de X1 es: {X1}")
   print(f"El valor de X2 es: {X2}")

   Y1 = A * X1 + B
   Y2 = A * X2 + B

   print(f"\nPara la siguiente ecuación:")
   print(f"Y = {A}X + {B}")
   print(f"\nDados los siguientes puntos:")
   print(f"P1 ({X1}, {Y1})")
   print(f"P2 ({X2}, {Y2})")

   deltax = X2 - X1
   deltay = Y2 - Y1
   distancia = (deltax ** 2 + deltay ** 2) ** 0.5

   print(f"\nLa distancia entre ellos es: {distancia}")
