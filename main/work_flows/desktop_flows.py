import allure
from main.extensions.ui_actions import UIActions
from main.extensions.verifications import Verifications
from main.utilities import base


class CalculatorFlows:

    @staticmethod
    @allure.step("Get calculation result.")
    def get_calc_result():
        return UIActions.get_element_text(base.calc_page.get_calc_result_field()).replace('Display is', '').strip()

    @staticmethod
    @allure.step("Calculating an arithmetic exercise.")
    def calc_it(exercise):
        for ch in exercise:
            CalculatorFlows.number_detection(int(ch)) if ch.isdigit() else CalculatorFlows.char_detection(ch)
        UIActions.click(base.calc_page.get_equals_btn())

    @staticmethod
    @allure.step("Identify a number and send for click")
    def number_detection(num):
        if num == 1: UIActions.click(base.calc_page.get_one_btn())
        elif num == 2: UIActions.click(base.calc_page.get_two_btn())
        elif num == 3: UIActions.click(base.calc_page.get_three_btn())
        elif num == 4: UIActions.click(base.calc_page.get_four_btn())
        elif num == 5: UIActions.click(base.calc_page.get_five_btn())
        elif num == 6: UIActions.click(base.calc_page.get_six_btn())
        elif num == 7: UIActions.click(base.calc_page.get_seven_btn())
        elif num == 8: UIActions.click(base.calc_page.get_eight_btn())
        elif num == 9: UIActions.click(base.calc_page.get_nine_btn())
        elif num == 0: UIActions.click(base.calc_page.get_zero_btn())
        else: raise Exception('An unexpected error occurred.')

    @staticmethod
    @allure.step("Identify a arithmetic action and send for click")
    def char_detection(ch):
        if ch == '+': UIActions.click(base.calc_page.get_plus_btn())
        elif ch == '-': UIActions.click(base.calc_page.get_minus_btn())
        elif ch == '/': UIActions.click(base.calc_page.get_divide_btn())
        elif ch == '*': UIActions.click(base.calc_page.get_multiply_btn())
        elif ch == '=': UIActions.click(base.calc_page.get_equals_btn())
        else: raise Exception('An unexpected error occurred.')

    @staticmethod
    @allure.step("Verify calc result")
    def verify_calc_result(excepted_result, action):
        Verifications.verify_equals(CalculatorFlows.get_calc_result(), excepted_result,
                                   f'The {action} operation did not work as expected.')

    @staticmethod
    @allure.step('Clear calculator')
    def clear_calculator():
        UIActions.click(base.calc_page.get_clear_btn())