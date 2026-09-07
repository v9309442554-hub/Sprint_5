import random
import string

def generate_login():
    
    first_name = "test"
    last_name = "testov"
    cohort = "19"

    random_digits = ''.join(random.choices(string.digits, k=3))

    
    # Генерируем уникальный email
    local_part = f"{first_name}{last_name}{cohort}{random_digits}"
    return f"{local_part}@yandex.ru"

def generate_password():

    length = random.randint(6, 12)
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))