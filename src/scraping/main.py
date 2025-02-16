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


# Testing function - delete later
def write_to_csv_ads(row):
    with open("./utils/ads.csv", 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(row)


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


def launch_browser(zone, district):
    driver = uc.Chrome(options=get_chrome_options())
    driver.get(f"https://www.zapimoveis.com.br/venda/imoveis/sp+sao-paulo+{zone}+{district}")
    ad_quantity = get_ads_quantity(driver)
    write_to_csv_ads([f"https://www.zapimoveis.com.br/venda/imoveis/sp+sao-paulo+{zone}+{district}", ad_quantity])
    sleep(randint(30, 60))
    driver.quit()
    return ad_quantity


for zone, districts in districts_list.items():
    for district in districts:
        print(f"https://www.zapimoveis.com.br/venda/imoveis/sp+sao-paulo+{zone}+{district}")
        #launch_browser(zone, district)
        #sleep(randint(5, 15))
