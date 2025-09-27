
points = int(input("Введіть кількість балів (0-100): "))

if 0 <= points <= 49:
    grade = "незадовільно"
elif 50 <= points <= 69:
    grade = "задовільно"
elif 70 <= points <= 89:
    grade = "добре"
elif 90 <= points <= 100:
    grade = "відмінно"
else:
    grade = "Некоректне значення !"

print(f"Оцінка: {grade}")
#Завдання 7
