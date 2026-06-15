
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_wikipedia_homepage():
    driver = webdriver.Chrome()
    driver.get("https://www.wikipedia.org/")

    assert "Wikipedia" in driver.title

    search_input = driver.find_element(By.ID, "searchInput")
    search_input.send_keys("Selenium")

    search_input.submit()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "firstHeading"))
    )

    assert "Selenium" in driver.page_source

    driver.quit()


def test_language_links_visible():
    driver = webdriver.Chrome()
    driver.get("https://www.wikipedia.org/")

    links = driver.find_elements(By.CSS_SELECTOR, ".central-featured-lang")

    assert len(links) > 5

    driver.quit()
