

print("=== CALCULADORA GEOMÉTRICA ===")
print("1. Figuras 2D ")
print("2. Figuras 3D ")
dimension = input("¿Qué tipo de figura quieres calcular? Escribe 1 o 2: ")


PI = 3.14159265358979

# ── Figuras 2D ──
if dimension == "1":
    print("¿Qué figura quieres usar?")
    print("1. Triángulo equilátero ")
    print("2. Triángulo rectángulo ")
    print("3. Círculo")
    print("4. Rectángulo")
    figura = input("Escribe el número de la figura: ")

    print("¿Qué quieres calcular?")
    print("1. Área ")
    print("2. Perímetro ")
    calculo = input("Escribe 1 o 2: ")

    
    if figura == "1":
        lado = float(input("¿Cuánto mide cada lado del triángulo? "))
        if calculo == "1":
            area = (3 ** 0.5 / 4) * lado ** 2   # 3**0.5 es la raíz cuadrada de 3
            print(f"El área del triángulo es: {area:.2f} u²")
        elif calculo == "2":
            perimetro = lado * 3
            print(f"El perímetro del triángulo es: {perimetro:.2f} u")

    
    elif figura == "2":
        lado_corto = float(input("¿Cuánto mide el lado corto ? "))
        lado_largo = float(input("¿Cuánto mide el lado largo ? "))
        hipotenusa = (lado_corto**2 + lado_largo**2) ** 0.5   # raíz cuadrada con **0.5
        if calculo == "1":
            area = (lado_corto * lado_largo) / 2
            print(f"El área del triángulo es: {area:.2f} u²")
        elif calculo == "2":
            perimetro = lado_corto + lado_largo + hipotenusa
            print(f"La hipotenusa mide: {hipotenusa:.2f} u")
            print(f"El perímetro del triángulo es: {perimetro:.2f} u")

    
    elif figura == "3":
        radio = float(input("\n¿Cuánto mide el radio del círculo?  "))
        if calculo == "1":
            area = PI * radio ** 2
            print(f"El área del círculo es: {area:.2f} u²")
        elif calculo == "2":
            circunferencia = 2 * PI * radio
            print(f"La circunferencia del círculo es: {circunferencia:.2f} u")

    
    elif figura == "4":
        base = float(input("¿Cuánto mide el lado de abajo ? "))
        altura = float(input("¿Cuánto mide el lado del costado ? "))
        if calculo == "1":
            area = base * altura
            print(f"El área del rectángulo es: {area:.2f} u²")
        elif calculo == "2":
            perimetro = 2 * (base + altura)
            print(f"El perímetro del rectángulo es: {perimetro:.2f} u")

# ── Figuras 3D ──
elif dimension == "2":
    print("¿Qué figura quieres usar?")
    print("1. Cubo ")
    print("2. Esfera ")
    print("3. Cilindro ")
    print("4. Cono ")
    figura = input("Escribe el número de la figura: ")

    print("¿Qué quieres calcular?")
    print("1. Área superficial ")
    print("2. Volumen ")
    calculo = input("Escribe 1 o 2: ")

    
    if figura == "1":
        lado = float(input("¿Cuánto mide cada arista del cubo? "))
        if calculo == "1":
            area_superficial = 6 * lado ** 2   
            print(f"El área superficial del cubo es: {area_superficial:.2f} u²")
        elif calculo == "2":
            volumen = lado ** 3
            print(f"El volumen del cubo es: {volumen:.2f} u³")

    
    elif figura == "2":
        radio = float(input("¿Cuánto mide el radio de la esfera? "))
        if calculo == "1":
            area_superficial = 4 * PI * radio ** 2
            print(f"El área superficial de la esfera es: {area_superficial:.2f} u²")
        elif calculo == "2":
            volumen = (4 / 3) * PI * radio ** 3
            print(f"El volumen de la esfera es: {volumen:.2f} u³")

    
    elif figura == "3":
        radio = float(input("¿Cuánto mide el radio de la tapa circular? "))
        altura = float(input("¿Cuánto mide la altura de la lata ? "))
        if calculo == "1":
            area_superficial = 2 * PI * radio * (radio + altura)
            print(f"El área superficial del cilindro es: {area_superficial:.2f} u²")
        elif calculo == "2":
            volumen = PI * radio ** 2 * altura
            print(f"El volumen del cilindro es: {volumen:.2f} u³")

    
    elif figura == "4":
        radio = float(input("¿Cuánto mide el radio de la base del cono? "))
        altura = float(input("¿Cuánto mide la altura del cono ? "))
        lado_inclinado = (radio**2 + altura**2) ** 0.5   # raíz cuadrada con **0.5
        if calculo == "1":
            area_superficial = PI * radio * (radio + lado_inclinado)
            print(f"El área superficial del cono es: {area_superficial:.2f} u²")
        elif calculo == "2":
            volumen = (1 / 3) * PI * radio ** 2 * altura
            print(f"El volumen del cono es: {volumen:.2f} u³")