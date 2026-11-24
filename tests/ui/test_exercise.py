import os

import pytest
from dotenv import load_dotenv

from pages.exercise_checkout_page import ExerciseCheckout
from pages.exercise_login_page import ExerciseLogin
from pages.exercise_main_page import ExercisePage
from pages.exercise_order_placed_page import ExerciseOrderPlaced
from pages.exercise_payment_page import ExercisePayment
from pages.exercise_view_cart_page import ExerciseViewCart

load_dotenv()


def test_add_blue_top(page):
    page.goto("https://automationexercise.com/")
    exercise_page = ExercisePage(page)
    exercise_page.add_blue_top()
    exercise_page.expect_continue_shopping_closed()


def test_add_tshirt_and_view_cart(page):
    page.goto("https://automationexercise.com/")
    exercise_main_page = ExercisePage(page)
    exercise_view_cart_page = ExerciseViewCart(page)
    exercise_main_page.add_menu_tshirt()
    exercise_view_cart_page.expect_proceed_to_checkout()


@pytest.mark.parametrize(
    "email, password",
    [
        ("fake1@test.com", "4t45rgbrtgb"),
        ("fake2@test.com", "456hfhnghnghn"),
        ("fake3@test.com", "54r45f4rffgtybrtgy56t56brgb"),
    ],
    ids=["user1", "user2", "user3"],
)
def test_login(page, email, password):
    page.goto("https://automationexercise.com/login")
    exercise_login = ExerciseLogin(page)
    exercise_login.login(email, password)
    exercise_login.expect_incorrect_alert()


def test_login_correct(page):
    page.goto("https://automationexercise.com/login")
    exercise_main = ExercisePage(page)
    exercise_login = ExerciseLogin(page)
    exercise_view_cart = ExerciseViewCart(page)
    exercise_checkout = ExerciseCheckout(page)
    exercise_payment = ExercisePayment(page)
    exercise_order_placed = ExerciseOrderPlaced(page)
    email = os.getenv("EXERCISE_USER")
    password = os.getenv("EXERCISE_PASSWORD")
    exercise_login.login(email, password)
    exercise_login.expect_logged_in()
    exercise_main.add_menu_tshirt()
    exercise_view_cart.expect_proceed_to_checkout()
    exercise_view_cart.click_home()
    exercise_main.add_blue_top()
    exercise_main.expect_continue_shopping_closed()
    exercise_view_cart.click_cart()
    exercise_view_cart.expect_proceed_to_checkout()
    exercise_view_cart.proceed_checkout()
    exercise_checkout.expect_address_details()
    exercise_checkout.input_comments()
    exercise_checkout.click_place_order()
    exercise_payment.expect_payment_page()
    exercise_payment.input_data_for_payment()
    exercise_payment.click_pay_and_confirm()
    exercise_order_placed.expect_order_placed()
    exercise_order_placed.expect_url_order_placed()
