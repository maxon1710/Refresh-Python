from functools import total_ordering


def describe_status(code: int) -> str:
    match code:
        case 200:
            return "OK"
        case 400:
            return "Bad Request"
        case 401:
            return "Unauthorized"
        case 403:
            return "Forbidden"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return f"Unknown status: {code}"


def color_car(color: str) -> str:
    match color:
        case "red":
            return "wolvo"
        case "yellow":
            return "nissan"
        case "orange":
            return "mercedes"


def check_credits_status(status: str) -> str:
    match status:
        case "draft":
            return "Заявка в черновике"
        case "in_review":
            return "На проверке андеррайтера"
        case "approved":
            return "Кредит одобрен"
        case "rejected":
            return "Отказано банком"
        case _:
            return f"Unknown status: {status}"


if __name__ == "__main__":
    print(describe_status(200))
    print(describe_status(400))
    print(describe_status(401))
    print(color_car("yellow"))
    print(check_credits_status("draft"))

    all_numbers = list(range(1, 10))
    max_value = all_numbers[0]

    for number in all_numbers:
        if number > max_value:
            max_value = number

    print(f"Максимальная цифра: {max_value}")

    all_times = [30, 54, 3828, 4455, 34, 344343]
    min_time = all_times[0]

    for time in all_times:
        if time < min_time:
            min_time = time

    print(f"Минимальный тайминг: {min_time}")

    # Вариант 2: через встроенный min()
    print(f"Минимум через min(): {min(all_times)}")

    # Вариант 3: фильтрация через List Comprehension (все замеры быстрее 100 мс)
    fast_times = [t for t in all_times if t < 100]
    print(f"Замеры быстрее 100мс: {fast_times}")

    # Карточка 2.1.3: Прерывание цикла через break
    numbers_break = list(range(1, 8))
    for n in numbers_break:
        print(f"Число до брейка: {n}")
        if n == 5:
            break

print()


order_statuses = ["PENDING", "PENDING", "PROCESSING", "SUCCESS", "FAILED", "TIMEOUT"]

for status in order_statuses:
    print(f"Проверяем заказ: {status}")
    if status == "SUCCESS":
        print(f"Заказ оплачен! Прерываем опрос.")
        break


# Карточка 2.1.4: Генерация списка через List Comprehension
words = [f"str{i}" for i in range(10)]
print(words)

test_emails = [f"qa_users_{x}@tochka.com" for x in range(1, 6)]
print(test_emails)

# Задача:
# Одной строкой через comprehension создать список clean_endpoints, где каждый элемент:
# Очищен от лишних пробелов по краям (метод .strip()).
# Переведён в нижний регистр (метод .lower()).
raw_endpoints = ["  /api/v1/USERS ", "/API/V1/LOGIN", "  /api/v1/orders  ", "/API/V1/PAYMENTS "]
clean_endpoints = [api.strip().lower() for api in raw_endpoints]
print(clean_endpoints)


# Как отфильтровать список logs через comprehension, чтобы в новый список попали только строки со словом "ERROR"?
logs = [
    "INFO: User 102 logged in",
    "ERROR: DB Connection timeout",
    "DEBUG: Cache hit for key 45",
    "ERROR: 500 Internal Server Error at /checkout",
    "INFO: Order 992 created"
]
results = [l for l in logs if "ERROR" in l]
print(results)
print()

import random
import time

TOTAL_STEPS = 10
MIN_LOAD = 0
MAX_LOAD = 100
ALERT = 85
PAUSE_STEPS = 0.2

load_rostics = []
for step in range(1, TOTAL_STEPS + 1):
    current_load = random.randint(MIN_LOAD, MAX_LOAD)
    load_rostics.append(current_load)
    if current_load >= ALERT:
        print(f"шаг {step}: Нагрузка {current_load}% ПРЕВЫСИЛА порог {ALERT}")
    else:
        print(f"Шаг {step}: Нагрузка {current_load}% не превысила порог {ALERT}")
    time.sleep(PAUSE_STEPS)

print(load_rostics)
print()


TOTAL_STEPS = 8
MIN_PING = 50
MAX_PING = 600
BEST_PING = 150
BAD_PING = 400
PAUSE_STEPS = 0.1

size_ping = []
for step in range(1, TOTAL_STEPS + 1):
    random_ping = random.randint(MIN_PING, MAX_PING)
    step_ping = step
    if random_ping <= BEST_PING:
        print(f"Запрос {step}: {random_ping}ms - Быстро")
    elif random_ping <= BAD_PING:
        print(f"Запрос {step}: {random_ping}ms - В пределах нормы")
    else:
        print(f"Запрос {step}: {random_ping}ms - Критически медленно")
    time.sleep(PAUSE_STEPS)