from time import sleep

import helpers
from actions import nav, interact
from driver import driver
from settings import USERNAME, PASSWORD, BASE_URL


def test_login_and_out():
    """
    Ensure Login and Logout process is successful
    """
    nav.navigate_to(driver, BASE_URL)
    assert interact.login(driver, USERNAME, PASSWORD), "Failed to login"
    sleep(6)
    interact.logout(driver)
    sleep(7)


def test_login_with_magic_link():
    """
    Ensure token is obtained from local storage, route through auth/tokenLogin using MAGIC_URL and obtained token
    """
    # Must log in once again in order to grab user token
    nav.navigate_to(driver, BASE_URL)
    assert interact.login(driver, USERNAME, PASSWORD), "Failed to login with Username and Password"
    sleep(4)
    token = interact.get_current_token(driver)
    assert token is not None, "Failed to get user token"
    sleep(3)
    interact.logout(driver)
    sleep(4)
    assert interact.login_with_magic_link(driver, token), "Failed to login with Magic Link"
    sleep(4)
