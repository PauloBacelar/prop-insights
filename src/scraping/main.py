import math

import undetected_chromedriver as uc
import csv
from random import randint
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem


def get_links():
    links = []
    with open("utils/links.txt", mode="r", encoding="utf-8") as file:
        for line in file:
            links.append(line.replace('\n', ''))

    return links


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
    district = url.replace('https://www.zapimoveis.com.br/', '').split('/')[2].split('+')[-1]
    for i in range(total_pages):
        sleep(randint(5, 10))
        load_all_page_ads(driver)
        sleep(randint(15, 45))
        get_properties_data(driver, district)
        sleep(randint(15, 45))
        go_to_next_page(driver)

    driver.quit()


def load_all_page_ads(driver):
    scroll_banner_loader = driver.find_element(By.CLASS_NAME, "campaign")
    driver.execute_script("arguments[0].scrollIntoView();", scroll_banner_loader)


def go_to_next_page(driver):
    button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="next-page"]')
    button.click()


def handle_hyphenated_range(value):
    if isinstance(value, str) and "-" in value and all(val.isnumeric() for val in value.split("-")):
        parts = value.split("-")
        return str((int(parts[0]) + int(parts[1])) / 2)
    return value


def convert_to_numeric(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return value


def get_properties_data(driver, district):
    properties_list_container = driver.find_element(By.CLASS_NAME, "listing-wrapper__content")
    properties_elements = properties_list_container.find_elements(By.XPATH, "./*")

    properties = []
    for elem in properties_elements:
        if (("planta" or "construção") in elem.text.lower()) or ("R$" not in elem.text):
            continue

        property_divs = get_property_card_divs(elem)
        property_data = {
            "property_id": property_divs["id"],
            "district": district,
            "property_type": 1 if "casa" in property_divs["location"].lower() else 2,
            "total_price": property_divs["prices"].split("\n")[0].replace("R$ ", "").replace(".", "").replace("A partir de ", ""),
            "condo_fee": 0 if "Cond" not in property_divs["prices"] else
            property_divs["prices"].replace("\nPreço abaixo do mercado", "").split("R$")[2].split(" ")[1].replace(".", ""),
            "area": property_divs["area"].split(" ")[0],
            "bedroom_qnt": property_divs["bedrooms"],
            "bathroom_qnt": property_divs["bathrooms"],
            "parking_spaces_qnt": 0 if not property_divs["parking_spaces"] else property_divs["parking_spaces"],
            "sq_m_price": None
        }

        for prop in list(property_data.keys()):
            property_data[prop] = handle_hyphenated_range(property_data[prop])
            if prop in ["total_price", "condo_fee", "area", "bedroom_qnt", "bathroom_qnt", "parking_spaces_qnt"]:
                property_data[prop] = convert_to_numeric(property_data[prop])

        property_data["sq_m_price"] = round(property_data["total_price"] / property_data["area"])

        write_property_info_on_csv(list(property_data.values()))
        properties.append(property_data)

    return properties


def get_property_card_divs(card):
    id = card.find_element(By.XPATH, "./*[1]").find_element(By.XPATH, "./*[1]").get_attribute("data-id")
    prices_div = safe_find_property_div(card, 'div[data-cy="rp-cardProperty-price-txt"]')
    location_div = safe_find_property_div(card, 'section[data-testid="card-address"]')
    area_div = safe_find_property_div(card, 'li[data-cy="rp-cardProperty-propertyArea-txt"]')
    bedroom_quant_div = safe_find_property_div(card, 'li[data-cy="rp-cardProperty-bedroomQuantity-txt"]')
    bathroom_quant_div = safe_find_property_div(card, 'li[data-cy="rp-cardProperty-bathroomQuantity-txt"]')
    parking_space_quant_div = safe_find_property_div(card, 'li[data-cy="rp-cardProperty-parkingSpacesQuantity-txt"]')

    return {
        "id": id,
        "prices": prices_div,
        "location": location_div,
        "area": area_div,
        "bedrooms": bedroom_quant_div,
        "bathrooms": bathroom_quant_div,
        "parking_spaces": parking_space_quant_div
    }


def safe_find_property_div(card, selector):
    try:
        return card.find_element(By.CSS_SELECTOR, selector).text
    except:
        return None


def write_property_info_on_csv(row):
    with open("../data/properties_data.csv", 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(row)


property_types = [
    "apartamento_residencial",
    "studio_residencial",
    "kitnet_residencial",
    "casa_residencial",
    "sobrado_residencial",
    "condominio_residencial",
    "casa-vila_residencial",
    "cobertura_residencial",
    "flat_residencial",
    "loft_residencial"
]

links = get_links()
for link in links:
    website = f"{link}?tipos={",".join(property_types)}" if property_types else link
    launch_browser(website)
    sleep(randint(5, 15))
