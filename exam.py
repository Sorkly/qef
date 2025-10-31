import random
import string
import logging
import datetime
import os

LOG_FILE = "Exam.log"

logging.basicConfig(
    filename=LOG_FILE,
    filemode="a",
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

print("Для авторизації на сайті вам буде надано приватний код. Збережіть його для подальшої авторизації.")

def user_id(count: int) -> str:
    return ''.join(random.choice(string.digits) for _ in range(count))

def random_let(count: int) -> str:
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(count))

user_id_code = user_id(6)
private_code = random_let(9)
today = datetime.datetime.now().strftime("%Y-%m-%d")

print("Ваш user_id:", user_id_code)
print("Ваш приватний код:", private_code)

logging.info(f"date - {today}, user_id - {user_id_code}, private code - {private_code}")

def find_by_private_code(log_path: str, code: str):
    if not os.path.exists(log_path):
        return None

    with open(log_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if f"private code - {code}" in line:
                parts = line.split(",")
                for part in parts:
                    part = part.strip()
                    if part.startswith("user_id - "):
                        return part.replace("user_id - ", "").strip()
    return None

entered_code = input("Для авторизації введіть ваш приватний код: ").strip()

found_user_id = find_by_private_code(LOG_FILE, entered_code)

if found_user_id:
    print("Авторизація успішна! Ваш user_id:", found_user_id)
else:
    print("Код не знайдено. Перевірте правильність введення.")
