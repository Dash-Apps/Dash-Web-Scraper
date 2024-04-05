
from urllib.parse import urlparse
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options

def get_resources(url: str,options: dict):
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=chrome_options)

    resources = []

    driver.get(url)
    # Access requests via the `requests` attribute
    for request in driver.requests:
        if request.response and urlparse(url).netloc not in urlparse(request.url).netloc:
            resources.append(request.url)
    driver.quit()
    return resources
