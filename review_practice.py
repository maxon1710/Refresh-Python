# from unittest import case
#
#
# def check_titan_threat(titan_type: str) -> str:
#     match titan_type:
#         case "colossal":
#             return "Колоссальный: опасность критическая"
#         case "armored":
#             return "Бронированный: держите ворота"
#         case "beast":
#             return "Звероподобный: обстрел камнями"
#         case _:
#             return "Обычный чистый титан"
#
#
# if __name__ == "__main__" :
#     print(check_titan_threat("colossal"))
#     print(check_titan_threat("armored"))
#     print(check_titan_threat("beast"))
#     print(check_titan_threat("normal"))
#
#
# speeds = [240, 310, 180, 420, 290, 380]
# max_speed = speeds[0]
#
# for speed in speeds:
#     if speed > max_speed:
#         max_speed = speed
#
# print(f"Максимальная скорость: {max_speed} км/ч")
#
#
# size = [1, 2, 3, 6, 9, 19,-2, -1839]
#
# min_size = min(size)
# print(f"минимальный размер {min_size}")
#
# negatives = [x for x in size if x < 0]
# print(negatives)
#
#
# statuses = [200, 404, 500, 201, 400, 204, 502, 200]
# errors = [code for code in statuses if code >= 400]
# print(errors)
#
#
# response_times = [120, 450, 80, 1200, 310, 950, 50]
# slow_requests = [r for r in response_times if r > 300]
# print(slow_requests)
#
#
# # TODO: В 19:00 после волейбола — разминка по 3 задачки (match-case,
# #  циклы, return в методах, мутация объекта)
# #  + старт Недели 3 (фикстуры Pytest)
#
#
# #  ⚡ Челнок 1/4: Тройка на match-case
#
# def get_account_type(code: str) -> str:
#     match code:
#         case "FL":
#             return "Физическое лицо"
#         case "IP":
#             return "Инд. предприниматель"
#         case "UL":
#             return "Юр. лицо"
#         case _:
#             return "Неизвестный тип счета"
#
# print(get_account_type("FL"))
# print(get_account_type("IP"))
# print(get_account_type("UL"))
# print(get_account_type("DNCDKJREF"))
#
#
# def get_player_role(position: str) -> str:
#     match position:
#         case "setter":
#             return "Связующий: диспетчер"
#         case "libero":
#             return "Либеро: прием и защита"
#         case "opposite":
#             return "Диагональный: мощная атака"
#         case _:
#             return "Игрок ротации"
#
# print(get_player_role("setter"))
# print(get_player_role("libero"))
# print(get_player_role("opposite"))
# print(get_player_role("sfvmklsfv"))
#
#
#
# #  🏐 Челнок 2/4: Цикл for + if + break
#
# transactions = [15000, 42000, 150000, 8000, 300000]
#
# for t in transactions:
#     if t > 100000:
#         print(f"AML Alert: операция {t} руб")
#         break
#
#
# scores = [19, 21, 23, 24, 25]
#
# for s in scores:
#     if s == 24:
#         print(f"Счет {s}: Матчбол! Прерываем опрос.")
#         break
#
#
#
# #  🏛 Челнок 3/4: Классы и методы с return
#
# class BankCard:
#     def __init__(self, card_number: str, balance: int, is_blocked: bool):
#         self.card_number = card_number
#         self.balance = balance
#         self.is_blocked = is_blocked
#
#     def get_status(self):
#         if self.is_blocked:
#             return "Карта заблокирована"
#         else:
#             return f"Карта активна. Баланс: {self.balance} руб"
#
# card_1 = BankCard("1", 100000, True)
# card_2 = BankCard("2", 50000, False)
# print(card_1.get_status())
# print(card_2.get_status())
#
#
# #  🗡 Челнок 4/4: Свободный полёт (L2 — Имена и архитектуру придумываешь САМ)
#
# HEALTH = 100
#
# class Person:
#     def __init__(self, name: str, health: int):
#         self.name = name
#         self.health = health
#
# def get_damage(person, damage: int):
#     person.health -= damage
#
# person_1 = Person("Max", HEALTH)
# print("До удара:", person_1.health)
#
# get_damage(person_1, 25)
# print("После удара:", person_1.health)
#
# Balance = 50000
#
# class BankAccount:
#     def __init__(self, vladelets: str, balance: int):
#         self.vladelez = vladelets
#         self.balance = balance
#
# def change_balance(new_vladelets, amount):
#     new_vladelets.balance -= amount
#
# vlad_1 = BankAccount("Vlad 1", 100000) # Создаем объект класса BankAccount
# print("Изначальный счет:", vlad_1.balance)
# change_balance(vlad_1, 100) # Назначаем объект класса участником функции изм счета
# print("Измененный баланс:", vlad_1.balance)
#
# # 1. Создали несколько счетов
# max_2 = BankAccount("Max 2", 50000)
#
# # 2. Собрали их в список счетов банка
# accounts = [vlad_1, max_2]
#
# # 3. Вывели всех разом в одну строчку через comprehension:
# print([f"{acc.vladelez}: {acc.balance} руб" for acc in accounts])
# print()
#
#
# # ==============================================================================
# # 🌉 МОСТИК ХЕМИНГУЭЯ НА ЗАВТРА (Старт сессии):
# # 1. 🏐 Разминка (4 микро-задачки на 15 мин):
# #    - 1 задачка: match-case
# #    - 1 задачка: for + if-elif-else
# #    - 2 задачки: классы и мутация объекта по ссылке через внешнюю функцию
# # 2. 📚 Неделя 3: План по теории (выжимка из курса) + Карточка 3.1 & 3.2 (фикстуры)
# # ==============================================================================
#
#
# events = [
#     ("transfer", 150000),
#     ("transfer", 25000),
#     ("transfer", 500),
#     ("deposit", 50000),
#     ("deposit", -1000),
#     ("crypto", 9999),
# ]
#
# for event, amount in events:
#     match event:
#         case "transfer":
#             if amount > 100000:
#                 print("Цена перевозки > 10000")
#             elif amount >= 10000:
#                 print("Цена перевозки >= 10000")
#             else :
#                 print("Микроперевод")
#         case ("deposit"):
#             if amount <=0:
#                 print("Ошибка")
#             else:
#                 print("пополнение")
#         case ("crypto"):
#             if amount == 9999:
#                 print("Крипты на счете: 9999")
#         case _:
#             print("Неизвестная ошибка")
# print()
#
# ACCOUNTS = 1000
#
# class Card:
#     def __init__(self, holder: str, limit: int):
#         self.holder = holder
#         self.limit = limit
#
# def reduce_limit(playerok, amount):
#     playerok.limit -= amount
#
# playerok_1 = Card("Max", 110)
# print(f"Счет игрока {playerok_1.holder}: {playerok_1.limit}")
# reduce_limit(playerok_1, 100)
# print(f"Счет игрока {playerok_1.holder} после снятия из банкомата: {playerok_1.limit}")
# print()
#
#
# class Player:
#     def __init__(self, name: str, stamina: int):
#         self.name = name
#         self.stamina = stamina
#
# def train_jump(p, amount):
#     p.stamina -= amount
#
# player = Player("Махмут", 100)
# print(f"Стамина игрока {player.name}: {player.stamina}")
# train_jump(player, 5)
# print(f"Стамина игрока {player.name} после забега: {player.stamina}")



#  Короткий цикл for + match-case по списку roles = ["admin", "editor", "guest", "hacker"]


roles = [("admin", 10), ("editor", 6), ("quest", 1), ("hacker", 4), ("autor", 999)]

for role in roles:
    match role:
        case ("admin", level) if level > 9:
            print(f"Уровень роли админа: {level}")
        case ("editor", level) if level > 5:
            print(f"Уровень роли редактора: {level}")
        case ("hacker", level) if level > 3:
            print(f"Уровень роли хакера: {level}")
        case ("quest", level) if level == 1:
            print(f"Уровень роли гость: {level}")
        case _:
            print(f"Неизвестная роль и уровень роли {role}")






































