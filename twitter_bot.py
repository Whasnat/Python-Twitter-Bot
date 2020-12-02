from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
import time

# Twitter class


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    # LOGIN
    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/login')
        time.sleep(3)
        email = bot.find_element_by_class_name('js-username-field')
        password = bot.find_element_by_class_name('js-password-field')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        time.sleep(3)
        password.send_keys(self.password)
        time.sleep(3)
        bot.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/div/div[1]/form/div[2]/button').click()

    # LIKE TWEET FUNCTION
    def like_tweet(self, hashtag):
        bot = self.bot
        # search HASHTAG
        bot.get("https://twitter.com/search?q="+hashtag+"&src=typd")
        time.sleep(3)
        for i in range(1, 21):
            # SCROLL
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(5)
            print('\n\n##### IN LIKE_TWEET() #####\n\n')

            # GET_TWEETS
            twts = bot.find_elements_by_class_name('css-1dbjc4n.r-1loqt21.r-1udh08x')
            print("TWTS")
            print(twts)

            # GET_SPECIFIC_TWEET_ID
            links = [elem.get_attribute("element")for elem in twts]
            print("LINK")
            print(links)

            # for link in links:
            #     print(link)
            #     bot.get("https://twitter.com/" + link)
            #     try:
            #         bot.find_element_by_class_name("HeartAnimation").click()
            #         time.sleep(10)
            #     except Exception as ex:
            #         time.sleep(120)


 usrname = input("Enter Username:\t")
 pwd = str(getpass.getpass(prompt='Enter Password:\t'))
 ed = TwitterBot(usrname, pwd)


ed.login()
ed.like_tweet("Elon Musk")
