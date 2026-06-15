
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
import time

def create_driver():
    caps = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "deviceName": "Android Emulator",
        "browserName": "Chrome"
    }

    return webdriver.Remote("http://localhost:4723/wd/hub", caps)


def test_mobile_wikipedia_swipe():
    driver = create_driver()
    driver.get("https://www.wikipedia.org/")

    time.sleep(3)

    # W3C swipe (modern approach)
    actions = ActionChains(driver)
    pointer = PointerInput(PointerInput.TOUCH, "finger")

    actions.w3c_actions = ActionBuilder(driver, mouse=pointer)

    actions.w3c_actions.pointer_action.move_to_location(500, 1200)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(500, 400)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

    assert "wikipedia" in driver.current_url.lower()

    driver.quit()


def test_mobile_search():
    driver = create_driver()
    driver.get("https://www.wikipedia.org/")

    time.sleep(2)

    search = driver.find_element(AppiumBy.ID, "searchInput")
    search.send_keys("Python programming")
    search.submit()

    time.sleep(3)

    assert "Python" in driver.page_source

    driver.quit()
