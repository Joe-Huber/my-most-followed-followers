import time

from selenium import webdriver
from xpaths_and_css_selectors import *

from github_user import GithubUser

def scrape_all_followers():
    # code here
    return []
def scrape_curr_page():
    return 0
def scrape_user(user_link):
    driver.get(user_link)
    return GithubUser()
def get_most_followed(link, num):
    setup(link)
    all_followers = scrape_all_followers()
    all_followers.sort(key=lambda user: user.followers, reverse=True)
    return all_followers[:num]
def setup(link):
    """
    Declares and initializes the chrome driver
    :param link: the link the chrome tab opens to
    :return: the chrome driver
    """
    global driver
    driver = webdriver.Chrome()
    driver.get(link)
    driver.implicitly_wait(1)