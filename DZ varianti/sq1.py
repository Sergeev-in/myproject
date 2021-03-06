# Задача - Написать программу для вычисления корней квадратного уравнения

# Квадратное уравнение имеет вид 'ax2 + bx + c = 0'
# При его решении сначала вычисляют дискриминант по формуле 'D = b2 - 4ac'
# Если D > 0, то КУ имеет два корня; если D = 0, то 1 корень; и если D < 0, то делают вывод, что корней нет.
print("Программа вычисления корней квадратного уравнения ")
print("")
print("Введите коэффициенты квадратного уравнения") # у нас их 3
a = input("Введите коэффициент a:") # Считывает и возвращает строку входных данных
a = int(a)
b = input("Введите коэффициент b:") # Считывает и возвращает строку входных данных
b = int(b)
c = input("Введите коэффициент c:") # Считывает и возвращает строку входных данных
c = int(c)

D = b**2 - 4*a*c # вычисляют дискриминант по формуле
print("Дискриминант D = ", D)

if D > 0:
    x1 = (-b + pow(D, 0.5)) / (2 * a)
    x2 = (-b - pow(D, 0.5)) / (2 * a)
    print('x1=',x1, 'x2=', x2)

if D==0:
    x = -b/(2*a)
    print('x=', x)
    
