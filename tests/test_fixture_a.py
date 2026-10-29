import pytest


    # Фикстуру со scope="module" (с print и yield).
    # Фикстуру с autouse=True (с print).
    # Два теста (def test_...), которые принимают в скобках
    # твой browser (из conftest.py) и твою модульную фикстуру,
    # и проверяют их через assert.

@pytest.fixture(scope="module")
def open_db():
    print("\n[SETUP] Соединение с бд")
    yield "Соединение подготовлено и открыто"
    print("\n[TEARDOWN] Закрытие соединение и очистка за собой")

@pytest.fixture(autouse=True)
def ping_inthernet():
    print("\n[SETUP] Первичная проверка инета")
    yield "Проверка подготовлена"
    print("\n[TEARDOWN] Очищение за собой после проверки")


def test_ping_inet(ping_inthernet, open_db, browser):
    assert ping_inthernet == "Проверка подготовлена"
    assert open_db == "Соединение подготовлено и открыто"
    assert browser == "Браузер открыт"

def test_open_db(open_db, browser):
   assert open_db == "Соединение подготовлено и открыто"
   assert browser == "Браузер открыт"

