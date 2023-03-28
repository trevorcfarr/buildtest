from logging import getLogger

import helpers
from actions import nav, interact
from driver import driver
from settings import FEED_URL
from time import sleep

_logger = getLogger(__name__)


def test_social_feed():
    """
    test social feed page by creating a post, verifying latest post, deleting created post, and verifying deletion.
    """
    nav.navigate_to(driver, FEED_URL)
    sleep(3)
    assert helpers.element_exists_and_displayed(driver, ".two_column_container")
    interact.type_feed_post(driver)
    sleep(5)
    interact.verify_feed_post(driver)
    sleep(2)
    interact.delete_feed_post(driver)
    driver.quit()

