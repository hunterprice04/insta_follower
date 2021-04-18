from time import sleep

from selenium import webdriver
from Credentials import usr, pw


class InstaBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.get('https://instagram.com')
        sleep(2)

        # if the sign in menu comes up switch to log in
        # self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()
        # sleep(2)

        # logs into instagram
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        sleep(4)

        # clicks do not remember credentials
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button") \
            .click()
        sleep(1)

        # click do not turn on notifications
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]") \
            .click()
    def follow_all(self,page):
        # enters the desired page into the search bar
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input") \
            .send_keys(page)
        sleep(1)

        # click the first recommended page
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[3]/div["
                                             "2]/div/a[1]/div/div[2]/div/span")\
            .click()
        sleep(2)

        # click the follower button
        self.driver.find_element_by_xpath("//a[contains(@href, '/following')]") \
            .click()
        sleep(2)

        '''
        # scroll to the bottom of the follower page to load everything in
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;   
                """, scroll_box)
        '''

        # iterate through each person
        for person in self.driver.find_elements_by_xpath("/html/body/div[4]/div/div/div[2]/ul"):
            person.find_element_by_xpath("//button[text()='Follow']").click()

bot = InstaBot(usr, pw)
# bot.follow_all('utk.tce')
bot.follow_all('x.morganprice.x')
