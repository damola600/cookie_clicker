from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")
last_action_time = time.time()


def get_granny():
    granny = driver.find_element(By.CSS_SELECTOR, value="#buyGrandma b")
    return granny


def get_money():
    money_available = driver.find_element(By.ID, value="money")
    return money_available


def get_cursor():
    cursor = driver.find_element(By.CSS_SELECTOR, value="#buyCursor b")
    return cursor


def get_factory():
    factory = driver.find_element(By.CSS_SELECTOR, value="#buyFactory b")
    return factory


def get_mine():
    mine = driver.find_element(By.CSS_SELECTOR, value="#buyMine b")
    return mine


def get_shipment():
    shipment = driver.find_element(By.CSS_SELECTOR, value="#buyShipment b")
    return shipment


def get_alchemy_lab():
    alchemy_lab = driver.find_element(By.CSS_SELECTOR, value="#buyAlchemy\ lab b")
    return alchemy_lab


def get_portal():
    portal = driver.find_element(By.CSS_SELECTOR, value="#buyPortal b")
    return portal


def get_time_machine():
    time_machine = driver.find_element(By.CSS_SELECTOR, value="#buyTime\ machine b")
    return time_machine


# def get_elder_pledge():
#     # elder_pledge = int(driver.find_element(By.CSS_SELECTOR, value="#buyElder\ Pledge b").text.split(" ")[1].replace(",", ""))
#     elder_pledge = driver.find_element(By.CSS_SELECTOR, value="#buyElder\ Pledge b").text.split(" ")
#     if elder_pledge == '':
#         return 0
#     else:
#         return int(elder_pledge[1].replace(",", ""))


def get_upgrades():
    money = int(get_money().text.replace(",", ""))
    upgrades = []
    upgrades_amount = []

    if money > int(get_cursor().text.split(" ")[2].replace(",", "")):
        upgrades.append(get_cursor())
        upgrades_amount.append(int(get_cursor().text.split(" ")[2].replace(",", "")))
    if money > int(get_granny().text.split(" ")[2].replace(",", "")):
        upgrades.append(get_granny())
        upgrades_amount.append(int(get_granny().text.split(" ")[2].replace(",", "")))
    if money > int(get_factory().text.split(" ")[2].replace(",", "")):
        upgrades.append(get_factory())
        upgrades_amount.append(int(get_factory().text.split(" ")[2].replace(",", "")))
    if money > int(get_shipment().text.split(" ")[2].replace(",", "")):
        upgrades.append(get_shipment())
        upgrades_amount.append(int(get_shipment().text.split(" ")[2].replace(",", "")))
    if money > int(get_alchemy_lab().text.split(" ")[3].replace(",", "")):
        upgrades.append(get_alchemy_lab())
        upgrades_amount.append(int(get_alchemy_lab().text.split(" ")[3].replace(",", "")))
    if money > int(get_time_machine().text.split(" ")[3].replace(",", "")):
        upgrades.append(get_time_machine())
        upgrades_amount.append(int(get_time_machine().text.split(" ")[3].replace(",", "")))
    if money > int(get_mine().text.split(" ")[2].replace(",", "")):
        upgrades.append(get_mine())
        upgrades_amount.append(int(get_mine().text.split(" ")[2].replace(",", "")))
    if money > int(get_portal().text.split(" ")[2].replace(",", "")):
        upgrades.append(get_portal())
        upgrades_amount.append(int(get_portal().text.split(" ")[2].replace(",", "")))
    if upgrades_amount is not None:
        max_index = upgrades_amount.index(max(upgrades_amount))
        return upgrades[max_index]
    else:
        return None


play_game = True
start_time = time.time()
while play_game:
    cookie.click()
    current_time = time.time()
    if current_time - last_action_time >= 5:
        money = get_money()
        available_upgrades = get_upgrades()
        if available_upgrades is not None:
            available_upgrades.click()

        last_action_time = current_time

    if time.time() - start_time >= 300:
        cookie_per_sec = driver.find_element(By.ID, value="cps").text
        print(cookie_per_sec)
        play_game = False

driver.quit()
