from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from datetime import date


def click_button_matching_css(driver, css_selector):
    """
    Locates an element by specific CSS selector and clicks
    """
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, css_selector))).click()


def element_exists(driver, css_selector):
    """
    grabs element if it exists
    """
    try:
        return driver.find_element(By.CSS_SELECTOR, css_selector)
    except NoSuchElementException:
        return None


def element_exists_and_displayed(driver, css_selector):
    """
    uses element_exists function above and checks to see if the element exists AND is displayed
    """
    element = element_exists(driver, css_selector)
    if not element:
        return False
    return element.is_displayed()


def click_button_matching_css_and_html(driver, css_selector, inner_html):
    """
    Locates an element by specific CSS selector AND attribute innerHTML and clicks, useful for vague class names
    """
    for element in driver.find_elements(By.CSS_SELECTOR, css_selector):
        if element.get_attribute("innerHTML") == inner_html:
            element.click()
            return True
    return False


def find_last_message_in_chat(driver, css_selector):
    """
    Locates most recent chat pane message by specific CSS selector and asserts equality to message input by script
    """
    element = driver.find_element(By.CSS_SELECTOR, css_selector)
    assert element.get_attribute("innerHTML") == f"test {date.today()}", "Validation of chat message failed"


def find_last_feed_post(driver, css_selector):
    """
    Locates most recent social feed post by specific CSS selector and asserts equality to message input by script
    """
    element = driver.find_element(By.CSS_SELECTOR, css_selector)
    assert element.get_attribute("innerHTML") == f"test {date.today()}", "Validation of feed post failed"


def deleted_feed_post(driver, css_selector):
    """
    Locates most recent social feed post by specific CSS selector and asserts equality to message input by script
    """
    element = driver.find_element(By.CSS_SELECTOR, css_selector)
    assert element.get_attribute("innerHTML") is not f"test {date.today()}", "Validation of feed post failed"


def set_input_text(driver, css_selector, text_value):
    """
    Uses CSS Selector to find available input field and types text
    """
    elements = driver.find_elements(By.CSS_SELECTOR, css_selector)
    if not elements:
        return False
    elements[0].send_keys(text_value)

# Not currently using, but could be useful

# def click_button_matching_xpath(driver, xpath):
#     """
#     Locates an element by specific XPATH and clicks
#     """
#     for element in driver.find_elements(By.XPATH, xpath):
#         element.click()
#         return True
#     return False
#
#
# def click_button_matching_css_and_title(driver, css_selector, title):
#     """
#     Locates an element by specific CSS selector AND attribute title and clicks, useful for items with attribute titles and vague class names
#     """
#     for element in driver.find_elements(By.CSS_SELECTOR, css_selector):
#         if element.get_attribute("title") == title:
#             element.click()
#             return True
#     return False
