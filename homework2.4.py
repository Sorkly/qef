n = int(input("Введіть число n: "))
print(f"Парні числа від {n} до 1:")
for i in range(n, 0, -1):   
    if i % 2 == 0:          
        print(i, end=" ")

#Завдання 5

num = int(input("Введіть число: "))

factorial = 1
for il in range(1, num + 1):
    factorial *= il

print(f"Факторіал числа {num} дорівнює {factorial}")
#Завдання 6
