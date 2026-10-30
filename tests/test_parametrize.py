# import pytest
#
# def describe_status(code: int) -> str:
#     match code:
#         case 200:
#             return "OK"
#         case 400:
#             return "Bad Request"
#         case 404:
#             return "Not Found"
#         case 500:
#             return "Internal Server Error"
#         case _:
#             return f"Неизвестный код: {code}"
#
#
# @pytest.mark.smoke
# @pytest.mark.parametrize(
#     "code, expected",
#     [
#         (200, "OK"),
#         (400, "Bad Request"),
#         (404, "Not Found"),
#         (500, "Internal Server Error"),
#     ],
#     ids=["success_200", "Bad Request_400", "Not Found_404", "Internal Server Error_500"],
# )
# def test_describe_status(code: int, expected: str):
#     assert describe_status(code) == expected
#
# import pytest
#
#
# Условие:
# Функция get_transfer_fee(amount: int) -> int считает комиссию за перевод:
import pytest


# До 10 000 руб включительно (<= 10000) ➔ комиссия 0 руб
# От 10 001 до 50 000 руб включительно (<= 50000) ➔ комиссия 50 руб
# Свыше 50 000 руб ➔ комиссия 100 руб
#
#
#
#
# def get_transfer_fee(amount: int) -> int:
#     if amount <= 10000:
#         return 0
#     elif amount <= 50000:
#         return 50
#     else:
#         return 100
#
#
# @pytest.mark.parametrize(
#     "amount, expected_fee",
#     [
#     (5000, 0),
#     (10000, 0),
#     (15000, 50),
#     (234243545, 100),
#     ],
#     ids=["free_5k", "edge_10k", "mid_15k", "max_23424545"]
# )
# def test_transfer_fee(amount: int, expected_fee: int):
#     assert get_transfer_fee(amount) == expected_fee





def get_soldiers_rank(kills: int):
    if kills == 0:
        return "Новобранец"
    elif kills < 10:
        return "Новичок"
    else:
        return "Главный убийца"


@pytest.mark.parametrize(
    "kill, expected_rank",
    [
        (0, "Новобранец"),
        (1, "Новичок"),
        (9, "Новичок"),
        (10, "Главный убийца"),
        (100, "Главный убийца")
    ],
    ids=
    ["recruit_0", "novice_1", "novice_9", "boss_edge_10", "boss_100"]
)
def test_kills_rank(kill, expected_rank):
    assert get_soldiers_rank(kill) == expected_rank






















