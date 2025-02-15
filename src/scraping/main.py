from random import randint, choice
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
]

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

user_agent = choice(USER_AGENTS)
chrome_options.add_argument(f"user-agent={user_agent}")


def launch_browser(zone, district):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

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
