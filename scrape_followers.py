import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from xpaths_and_css_selectors import *

from github_user import GithubUser

def scrape_all_followers():
    # code here
    return []
def scrape_curr_page():
    return 0
def scrape_user(user_link):
    driver.get(user_link)
    name = driver.find_element(By.CSS_SELECTOR, username_selector).text
    followers_text = driver.find_element(By.CSS_SELECTOR, followers_selector).text.lower()
    if 'k' in followers_text:
        followers = int(float(followers_text.replace('k', '')) * 1000)
    elif 'm' in followers_text:
        followers = int(float(followers_text.replace('m', '')) * 1000000)
    else:
        followers = int(followers_text.replace(',', ''))
    profile_image_link = driver.find_element(By.CSS_SELECTOR, profile_image_selector).get_attribute("src")
    return GithubUser(name=name, followers=followers, profile_image_link=profile_image_link, link=user_link)
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