
def calcular_area(base, altura):

    if base <= 0:
        raise ValueError("La base debe ser un valor positivo")

    if altura <= 0:
        raise ValueError("La altura debe ser un valor positivo")

    area = base * altura

    return area


if __name__ == "__main__":

    print("CALCULADORA DEL AREA DE UN RECTANGULO")

    base = float(input("Ingrese la base: "))
    altura = float(input("Ingrese la altura: "))

    area = calcular_area(base, altura)

    print(f"El area del rectangulo es: {area:.2f}")
