from selenium import webdriver
from time import sleep
import logging


class OnlineCalc:

    def __init__(self, driver=webdriver.Firefox()):
        """
        Online calc object
        :param driver: webdriver
        """
        logging.info("Initializing OnlineCalc object...")
        self.page = r"http://web2.0calc.com/"
        self.driver = driver

    def open_page(self):
        logging.info("Opening page: {}".format(self.page))
        self.driver.get(self.page)

    def calculator_operation(self, x, y, operation):

        """
        Generic function for calculator operation based on two variables
        :param x: first operation variable
        :param y: second operation variable
        :param operation: add/substract/multiply/divide
        :return: operation result (value)
        """

        self.driver.find_element_by_id("input").clear()

        elem = self.driver.find_element_by_id("Btn{}".format(x))
        elem.click()
        elem = self.driver.find_element_by_id(operation)
        elem.click()
        elem = self.driver.find_element_by_id("Btn{}".format(y))
        elem.click()
        elem = self.driver.find_element_by_id("BtnCalc")
        elem.click()
        result = self.driver.find_element_by_id("input").get_attribute("value")

        return result

    def addition(self, x, y):

        result = self.calculator_operation(x, y, operation="BtnPlus")

        return int(result)

    def substraction(self, x, y):

        result = self.calculator_operation(x, y, operation="BtnMinus")

        return int(result)

    def division(self, x, y):

        result = self.calculator_operation(x, y, operation="BtnDiv")

        return round(float(result), 2)

    def multiplication(self, x, y):

        result = self.calculator_operation(x, y, operation="BtnMult")

        return int(result)

    def close_browser(self, delay=0):

        """
        :param delay: time after browser will be closed
        """

        if delay:
            sleep(delay)
        self.driver.quit()