import pytest


@pytest.fixture(scope="session")
def browser():
    print("\n[SETUP] Запуск браузера(1 раз на всю сессию)")
    yield "Браузер открыт"
    print("\n [TEARDOWN] Закрытие браузера после тестов")