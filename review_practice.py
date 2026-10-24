def check_titan_threat(titan_type: str) -> str:
    match titan_type:
        case "colossal":
            return "Колоссальный: опасность критическая"
        case "armored":
            return "Бронированный: держите ворота"
        case "beast":
            return "Звероподобный: обстрел камнями"
        case _:
            return "Обычный чистый титан"


if __name__ == "__main__" :
    print(check_titan_threat("colossal"))
    print(check_titan_threat("armored"))
    print(check_titan_threat("beast"))
    print(check_titan_threat("normal"))


speeds = [240, 310, 180, 420, 290, 380]
max_speed = speeds[0]

for speed in speeds:
    if speed > max_speed:
        max_speed = speed

print(f"Максимальная скорость: {max_speed} км/ч")


size = [1, 2, 3, 6, 9, 19,-2, -1839]

min_size = min(size)
print(f"минимальный размер {min_size}")

negatives = [x for x in size if x < 0]
print(negatives)


statuses = [200, 404, 500, 201, 400, 204, 502, 200]
errors = [code for code in statuses if code >= 400]
print(errors)


response_times = [120, 450, 80, 1200, 310, 950, 50]
slow_requests = [r for r in response_times if r > 300]
print(slow_requests)