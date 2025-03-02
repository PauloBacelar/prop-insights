# Real Estate Scraper

This project is a web scraper that extracts real estate data from [ZAP Imóveis](https://www.zapimoveis.com.br/), using Selenium with an undetected Chrome driver. It collects data on property listings, including price, area, number of bedrooms, and other relevant attributes, and stores them in a CSV file for further analysis.

[Fala português? Leia essa documentação em PT-BR!](./README-pt.md)

## Features

- Scrapes real estate listings from Zap Imóveis
- Uses undetected Chrome driver to bypass bot detection
- Rotates user agents to reduce the risk of being blocked
- Extracts property details such as price, area, location, and features
- Stores data in a CSV file for analysis

## Requirements

Ensure you have the following installed:

- Python 3.x
- Google Chrome
- ChromeDriver (compatible with your Chrome version)

Required Python packages:
```sh
pip install undetected-chromedriver selenium random-user-agent
```

## How It Works

1. Reads property listing URLs from `utils/links.txt`.
2. Uses a rotating user-agent for each request.
3. Launches an undetected Chrome instance with necessary options.
4. Extracts property data from each listing.
5. Saves the extracted data to `data/properties_data.csv`.

## Usage

1. Add URLs to `utils/links.txt` (one per line).
2. Modify `url_params` in the script to filter listings based on your needs.
3. Run the script:
   ```sh
   python script.py
   ```

## Configuration

Modify `url_params` in the script to personalize search filters:
```python
url_params = {
    "tipos": ["apartamento_residencial", "casa_residencial"],
    "proximoMetro": True,
    "precoMaximo": 750000,
    "areaMinima": 40,
    # ...
}
```

## Notes

- The scraper automatically handles pagination and extracts all listings from multiple pages.
- It introduces random sleep intervals to mimic human browsing behavior.
- Ensure compliance with the website's terms of service before running the scraper.

## License
This project is for educational purposes only. Use it responsibly.

