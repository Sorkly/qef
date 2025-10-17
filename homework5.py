user_value = input("Введіть число:")

try:


    value = float(user_value)
    ready_value = int(value)
    
    print(f"Ви ввели {ready_value}")

except:
    print("Помилка,це не число")