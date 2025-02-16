import undetected_chromedriver as uc
from districts import districts_list
from random import randint
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem


def get_user_agent():
    software_names = [SoftwareName.CHROME.value]
    operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
    user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
    return user_agent_rotator.get_random_user_agent()

def get_chrome_options():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument(f"user-agent=choice{get_user_agent()}")
    return chrome_options

def launch_browser(zone, district):
    driver = uc.Chrome(options=get_chrome_options())
    website = f"https://www.zapimoveis.com.br/venda/imoveis/sp+sao-paulo+{zone}+{district}"
    driver.get(website)
    get_ads_quantity(driver)
    sleep(sleep_time)
    driver.quit()

def get_ads_quantity(driver):
    print(driver.find_element(By.TAG_NAME, "h1").text)


# Mock variables, get from ./districts.py later
zones = list(districts_list.keys())

sleep_time = randint(10000, 10001)
for zone in zones:
    for district in districts_list[zone]:
        launch_browser(zone, district)
        sleep_time += randint(0, 5)
