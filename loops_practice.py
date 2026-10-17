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
