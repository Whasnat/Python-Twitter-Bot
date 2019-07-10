from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com')
        time.sleep(3)
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        bot.find_element_by_class_name("EdgeButton").click()

    def like_tweet(self, hashtag):
        bot = self.bot
        bot.get("https://twitter.com/search?q="+hashtag+"&src=typd")
        time.sleep(3)
        for i in range(1, 5):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(3)
            twts = bot.find_elements_by_class_name('tweet')
            links = [elem.get_attribute('data-permalink-path')for elem in twts]
            print(links)
            for link in links:
                bot.get("https://twitter.com" + link)
                try:
                    bot.find_element_by_class_name("HeartAnimation").click()
                    time.sleep(20)
                except Exception as ex:
                    time.sleep(120)


ed = TwitterBot('waliul9000@gmail.com', 'coding14LOL')
ed.login()
ed.like_tweet("Dhaka")