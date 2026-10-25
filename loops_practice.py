import random
import time


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

    for t in all_times:
        if t < min_time:
            min_time = t

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


order_statuses = ["PENDING", "PENDING", "PROCESSING",
                  "SUCCESS", "FAILED", "TIMEOUT"]

for status in order_statuses:
    print(f"Проверяем заказ: {status}")
    if status == "SUCCESS":
        print("Заказ оплачен! Прерываем опрос.")
        break


# # Карточка 2.1.4: Генерация списка через List Comprehension
words = [f"str{i}" for i in range(10)]
print(words)

test_emails = [f"qa_users_{x}@tochka.com" for x in range(1, 6)]
print(test_emails)

# Задача:
# Одной строкой через comprehension создать
# список clean_endpoints, где каждый элемент:
# Очищен от лишних пробелов по краям (метод .strip()).
# Переведён в нижний регистр (метод .lower()).
raw_endpoints = [
    "  /api/v1/USERS ",
    "/API/V1/LOGIN",
    "  /api/v1/orders  ",
    "/API/V1/PAYMENTS ",
]
clean_endpoints = [api.strip().lower() for api in raw_endpoints]
print(clean_endpoints)


# Как отфильтровать список logs через comprehension,
# чтобы в новый список попали только строки со словом "ERROR"?
logs = [
    "INFO: User 102 logged in",
    "ERROR: DB Connection timeout",
    "DEBUG: Cache hit for key 45",
    "ERROR: 500 Internal Server Error at /checkout",
    "INFO: Order 992 created",
]
results = [log for log in logs if "ERROR" in log]
print(results)
print()


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
        print(f"шаг {step}: Нагрузка {current_load}% "
              f"ПРЕВЫСИЛА порог {ALERT}")
    else:
        print(f"Шаг {step}: Нагрузка {current_load}% "
              f"не превысила порог {ALERT}")
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


# 2.2 - Дальше КЛАССЫ


class TestUser:
    def __init__(self, email, role, is_active=True):
        self.email = email
        self.role = role
        self.is_active = is_active

    def summary(self):
        return (f"User: {self.email}, "
                f"Role: {self.role}, "
                f"Active: {self.is_active}")


u1 = TestUser("266@mail.ru", "test1", True)
u2 = TestUser("228@gmail.com", "test2", False)
u3 = TestUser("client@mail.com", "test3")

print(u1.summary())
print(u2.summary())
print(u3.summary())
print()


class ApiResponse:
    def __init__(self, endpoint, status, body):
        self.endpoint = endpoint
        self.status = status
        self.body = body

    def is_success(self) -> bool:
        return self.status == 200


resp_ok = ApiResponse("/api/v1/credits", 200, "OK")
resp_fail = ApiResponse("https://example.com", 404, "Not Found")

print(resp_ok.is_success())
print(resp_fail.is_success())
print()


class House:
    def __init__(self, name, size):
        self.name = name
        self.size = size


def update_house(house, new_size):
    house.size = new_size


h1 = House("Домик", 100)
print("До ремонта:", h1.size)

update_house(h1, 200)
print("После ремонта:", h1.size)


class BankCard:
    def __init__(self, balance):
        self.balance = balance


def deposit(card, amount):
    card.balance = card.balance + amount


card = BankCard(1000)
print("Изначальный баланс:", card.balance)
deposit(card, 500)
print("Пополненный баланс:", card.balance)


class Player:
    def __init__(self, hp):
        self.hp = hp


def take_player(player, damage):
    player.hp = player.hp - damage


PLAYER1 = Player(100)
print(PLAYER1.hp)
take_player(PLAYER1, 35)
print(PLAYER1.hp)


class AuthToken:
    def __init__(self, value):
        self.value = value


def refresh_token(token, new_value):
    token.value = new_value


token1 = AuthToken(143890293)
print("Первый токен:", token1.value)
refresh_token(token1, 2374384593478537548)
print("Обновленный токен:", token1.value)
# Изменился оригинальный токен на обновленный, потому что мы
# написали функцию, которая берет объект "token" и переменную "value"
# и заменяет "value" на наш новый токен
# В Python объекты передаются по ссылке (на тот же адрес в памяти),
# а не копируются.


PASSING_GRADE = 4.1

students = [
    {"name": "Алексей", "grade": 4.8},
    {"name": "Мария", "grade": 3.9},
    {"name": "Иван", "grade": 4.5},
    {"name": "Елена", "grade": 4.0},
]

names = [s["name"] for s in students if s["grade"] > PASSING_GRADE]
print(names)
print()


LIMIT_AMOUNT = 50000

transfers = [
    {"id": "tx_101", "amount": 12000},
    {"id": "tx_102", "amount": 85000},
    {"id": "tx_103", "amount": 140000},
    {"id": "tx_104", "amount": 4500},
]

list_id = [i["id"] for i in transfers if i["amount"] > LIMIT_AMOUNT]
print(list_id)
