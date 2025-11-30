import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options

from .xpaths_and_css_selectors import *
from .github_user import GithubUser

driver = None # Initialize driver as a global variable

def scrape_all_followers():
    user_links = []
    while True:
        user_links.extend(scrape_curr_page())
        try:
            # Wait for the "Next" button to be clickable and then click it.
            wait = WebDriverWait(driver, 5)
            next_button = wait.until(ec.element_to_be_clickable((By.LINK_TEXT, "Next")))
            next_button.click()
            time.sleep(1)  # Wait for the next page to load
        except (NoSuchElementException, TimeoutException):
            # This means we're on the last page.
            break

    followers_list = []
    for link in list(set(user_links)):
        user = scrape_user(link)
        if user:
            followers_list.append(user)

    return followers_list

def scrape_curr_page():
    user_links = []
    link_elements = driver.find_elements(By.CSS_SELECTOR, "#user-profile-frame > div > div > div.d-table-cell > a")
    for element in link_elements:
        user_links.append(element.get_attribute('href'))
    return list(set(user_links))

def next_page_exists():
    try:
        driver.find_element(By.LINK_TEXT, "Next")
        return True
    except:
        return False

def scrape_user(user_link):
    driver.get(user_link)
    while "Too many requests" in driver.page_source:
        print("Rate limit exceeded. Waiting 5 seconds and retrying...")
        time.sleep(5)
        driver.refresh()
        time.sleep(2) # Wait a bit for the page to load after refresh

    try:
        wait = WebDriverWait(driver, 10)
        name = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, username_selector))).text
        followers_text = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, followers_selector))).text.lower()
        
        if 'k' in followers_text:
            followers = int(float(followers_text.replace('k', '')) * 1000)
        elif 'm' in followers_text:
            followers = int(float(followers_text.replace('m', '')) * 1000000)
        else:
            followers = int(followers_text.replace(',', ''))
            
        profile_image_link = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, profile_image_selector))).get_attribute("src")
        return GithubUser(name=name, followers=followers, profile_image_link=profile_image_link, link=user_link)
    except TimeoutException:
        print(f"Failed to load user data for {user_link}. Skipping user.")
        return None

def get_most_followed(link, num):
    setup(link)
    all_followers = scrape_all_followers()
    all_followers.sort(key=lambda user: user.followers, reverse=True)
    return all_followers[:num]

def setup(link):
    """
    Declares and initializes the chrome driver
    :param link: the link the Chrome tab opens to
    :return: the chrome driver
    """
    global driver
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)
    driver.get(link)
    driver.implicitly_wait(1)

def close_driver():
    """
    Closes the chrome driver if it's running.
    """
    global driver
    if driver:
        driver.quit()
        driver = None # Set to None to indicate it's closed
