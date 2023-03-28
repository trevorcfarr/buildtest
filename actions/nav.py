from time import sleep


def navigate_to(driver, url, wait=None):
    if wait is not None:
        sleep(wait)
    driver.get(url)
