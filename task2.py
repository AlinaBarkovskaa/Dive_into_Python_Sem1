def check_triangle(a, b, c):
    if a >= b + c or b >= a + c or c >= a + b:
        return "Треугольник не существует"
    
    if a == b == c:
        return "Треугольник равносторонний"
    elif a == b or b == c or a == c:
        return "Треугольник равнобедренный"
    else:
        return "Треугольник разносторонний"

a = float(input("Введите длину a стороны: "))
b = float(input("Введите длину b стороны: "))
c = float(input("Введите длину c стороны: "))

result = check_triangle(a, b, c)
print(result)