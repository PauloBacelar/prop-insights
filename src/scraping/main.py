from random import randint, choice
from time import sleep
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
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
    sleep(sleep_time)
    driver.quit()


# Mock variables, get from ./districts.py later
districts = {
    "zona-norte": ["tucuruvi", "jacana"],
    "zona-leste": ["mooca", "tatuape"],
    "zona-sul": ["grajau", "vl-mariana"],
    "zona-oeste": ["butanta", "vl-sonia"],
    "centro": ["se", "liberdade"]
}
zones = list(districts.keys())

sleep_time = randint(30, 60)
for zone in zones:
    for district in districts[zone]:
        launch_browser(zone, district)
        sleep_time += randint(5, 15)
