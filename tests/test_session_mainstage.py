from logging import getLogger

from actions import nav, interact
from driver import driver
from settings import USERNAME, PASSWORD, BASE_URL, MAINSTAGE_URL
from time import sleep

_logger = getLogger(__name__)


def test_session_mainstage():
    """
    Ensure Main Stage session build test is successful
    """
    # NEED if not testing full pytest tests / NOT flowing through test_login
    # nav.navigate_to(driver, BASE_URL)
    # interact.login(driver, USERNAME, PASSWORD)
    # sleep(5)
    nav.navigate_to(driver, MAINSTAGE_URL)
    sleep(5)
    assert interact.check_audio_mainstage(driver), "Could not verify Main Stage Audio being produced and heard"
    sleep(3)
    assert interact.check_video_mainstage(driver), "Could not verify Main Stage Video being produced and seen"
    sleep(3)
    interact.type_in_chat(driver)  # assertion inside helpers.find_last_message_in_chat
    sleep(1)
    assert interact.emoji_react(driver), "Could not verify Main Stage Emoji Reaction"
    sleep(3)
    driver.set_window_size(width=800, height=600)
    assert interact.check_video_player(driver), "Video Stream container not visible after resize"
    sleep(3)
    driver.set_window_size(width=1920, height=1080)
    assert interact.check_video_player(driver), "Video Stream container not visible after resize"
    sleep(1)
    driver.set_window_size(width=1050, height=700)
    sleep(1)
    interact.click_home_logo(driver)
    assert interact.check_mini_player(driver), "Could not verify Miniplayer displayed"
    sleep(3)

