import math

import undetected_chromedriver as uc
import csv
from districts import districts_list
from random import randint
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem


def get_user_agent():
    user_agent_rotator = UserAgent(
        software_names=[SoftwareName.CHROME.value],
        operating_systems=[OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value],
        limit=100
    )
    return user_agent_rotator.get_random_user_agent()


def get_chrome_options():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(f"user-agent={get_user_agent()}")
    return options


def get_ads_quantity(driver):
    try:
        return int(driver.find_element(By.TAG_NAME, "h1").text.split()[0].replace('.', ''))
    except:
        return 0


def launch_browser(url):
    driver = uc.Chrome(options=get_chrome_options())
    driver.get(url)

    total_pages = math.ceil(get_ads_quantity(driver) / 105)
    for i in range(total_pages):
        load_all_page_ads(driver)
        sleep(randint(15, 45))
        properties_data = get_properties_data(driver)
        # go_to_next_page(driver)
        sleep(99999)


    driver.quit()


def load_all_page_ads(driver):
    scroll_banner_loader = driver.find_element(By.CLASS_NAME, "campaign")
    driver.execute_script("arguments[0].scrollIntoView();", scroll_banner_loader)


def go_to_next_page(driver):
    button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="next-page"]')
    button.click()


def get_properties_data(driver):
    properties_list_container = driver.find_element(By.CLASS_NAME, "listing-wrapper__content")
    properties_elements = properties_list_container.find_elements(By.XPATH, "./*")

    for elem in properties_elements:
        if ("Na planta" or "Em construção") in elem.text:
            continue

        print(elem.text.split('\n'))
        print("--------------------------")

    return 0


def write_property_info_on_csv(row):
    pass
    """""
    with open("./utils/data.csv", 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(row)
    """""


for zone, districts in districts_list.items():
    for district in districts:
        website = f"https://www.zapimoveis.com.br/venda/imoveis/sp+sao-paulo+{zone}+{district}"
        launch_browser(website)
        sleep(randint(5, 15))
