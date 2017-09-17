from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pywinauto import keyboard
from time import sleep


class MediaSpam(object):

    def __init__(self, driver):
        self.driver = driver

    def youtube_attack(self, repetitions, video_name, google_query):

        """
        author: artur.itsme@gmail.com

        :param repetitions: no of opened tabs with desired media content from youtube.com
        :param video_name: name of desired media content from youtube.com
        :param google_query: desired google query to be executed in google graphics
        """

        driver = self.driver

        for repetition in range(1, repetitions, 1):

            driver.get("https://www.youtube.com/")
            elem = driver.find_element_by_name("search_query")
            elem.clear()
            elem.send_keys(video_name)
            elem = driver.find_element_by_id("search-icon-legacy")
            elem.click()
            elem = driver.find_element_by_xpath('//*[@class="yt-simple-endpoint style-scope ytd-video-renderer"]')
            elem.click()
            # open a new tab
            keyboard.SendKeys("^t")
            # commented line below is an alternative way to open a new tab
            # driver.execute_script('''window.open("http://google.pl","_blank");''')

            sleep(0.2)
            driver.switch_to.window(driver.window_handles[repetition])

        driver.get("https://www.google.com/imghp?/")
        elem = driver.find_element_by_name("q")
        elem.send_keys(google_query)
        elem.send_keys(Keys.RETURN)

    def close_browser(self, delay):

        """
        :param delay: time after browser will be closed
        """

        if delay:
            sleep(delay)
        self.driver.quit()


def main():

    """
    This function shows how to use MediaSpam class.

    """

    krzysztof = MediaSpam(driver=webdriver.Firefox())
    krzysztof.youtube_attack(repetitions=2,
                   video_name="Krzysztof Krawczyk Chciałem Być",
                   google_query="Krzysztof Krawczyk przejmuje Twój komputer :)")
    krzysztof.close_browser(delay=360)

if __name__ == "__main__":
    main()
