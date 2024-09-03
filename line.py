def line():
   def calcular_recta(A, B, X1, X2):

    resultado = []

    resultado.append(f"El coeficiente A de su ecuación de la recta es: {A}")
    resultado.append(f"El coeficiente B de su ecuación de la recta es: {B}")
    resultado.append(f"El coeficiente X1 de su ecuación de la recta es: {X1}")
    resultado.append(f"El coeficiente X2 de su ecuación de la recta es: {X2}")

    Y1 = A * X1 + B
    Y2 = A * X2 + B

    
    resultado.append(f"\nPara la siguiente ecuación:")
    resultado.append(f"\tY = {A}X + {B}")
    resultado.append(f"\nDados los siguientes puntos:")
    resultado.append(f"\tP1 ({X1}, {Y1})")
    resultado.append(f"\tP2 ({X2}, {Y2})")


    deltax = X2 - X1
    deltay = Y2 - Y1
    distancia = math.sqrt(deltax ** 2 + deltay ** 2)


    resultado.append(f"\nLa distancia entre ellos es: {distancia}")

    return "\n".join(resultado)


A = 2.3
B = -4.0
X1 = 50.0
X2 = -32.9


salida = calcular_recta(A, B, X1, X2)


print(salida)
