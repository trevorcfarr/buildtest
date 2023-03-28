from json import loads
from time import sleep
from datetime import date
from selenium.webdriver import Keys
from logging import getLogger
from settings import MAGIC_URL

import helpers

_logger = getLogger(__name__)


def login(driver, username, password):
    """
    When on the home page this will log you in

    returns: True if login was a success, False otherwise.
    """
    # Determine if site is public OR if account creation is enabled OR disabled
    #  so that we can find the correct Button to bring up the Login Panel
    if helpers.element_exists_and_displayed(driver, ".right_container .user_login_container"):
        helpers.click_button_matching_css(driver, ".right_container .user_login_container")
        _logger.info("Site is public")
    elif helpers.element_exists_and_displayed(driver, ".already_have_container"):
        helpers.click_button_matching_css(driver, ".already_have_container")
        _logger.info("Site has account creation enabled")
    elif helpers.element_exists_and_displayed(driver, ".cssButton.standard_button_filled #css_button_text"):
        helpers.click_button_matching_css(driver, ".cssButton.standard_button_filled #css_button_text")
        _logger.info("Site has account creation disabled")
    else:
        raise AssertionError("Unable to find login button")
    sleep(1)

    # Switch from Login with Magic Link to Email and Password if Magic link login is defaulted
    if helpers.element_exists_and_displayed(driver, ".login_panel .email_password_container"):
        helpers.click_button_matching_css(driver, ".login_panel .email_password_container")
        sleep(1)
    # Enter Credentials. If Privacy Policy slider exists, click slider and login. If no slider, login.
    helpers.set_input_text(driver, ".email_container .input", username)
    helpers.set_input_text(driver, ".password_container .input", password)
    if helpers.element_exists_and_displayed(driver, ".terms_switch_container"):
        helpers.click_button_matching_css(driver, ".switch_row_right .uiswitch")
        sleep(1)
    helpers.set_input_text(driver, ".password_container .input", Keys.ENTER)
    return True


def get_current_token(driver):
    """
    While logged in, find and return local storage item User [token]
    """
    user = driver.execute_script("return localStorage.getItem('user');")
    user = loads(user)
    return user["token"]


def login_with_magic_link(driver, token):
    """
    Using User Token route through auth login url to simulate clicking magic link email url. Return False if not logged in.
    """
    driver.get(f"https://auth.junolive.co/login/{MAGIC_URL}/{token}")
    sleep(3)
    for _ in range(1, 4):
        if helpers.element_exists_and_displayed(driver, ".right_container .profile_icon_container .profile_image"):
            return True
        sleep(1)
    return False


def logout(driver):
    """
    Click profile dropdown, and then click logout
    """
    sleep(3)
    helpers.click_button_matching_css(driver, ".right_container .user_information_container")
    helpers.click_button_matching_css(driver, ".profile_dropdown .logout_container")
    sleep(3)
    # if helpers.element_exists_and_displayed(driver, ".right_container .profile_icon_container .profile_image"):
    #     raise AssertionError("Unable to verify logout")


def set_mic_and_camera(driver):
    """
    Set default Microphone and Camera to be fake devices
    """
    helpers.click_button_matching_css(driver, ".user_information_container")
    sleep(1)
    helpers.click_button_matching_css_and_html(driver, ".profile_dropdown .dropdown_items_container .dropdown_item .text", "Camera &amp; Microphone")
    sleep(1)
    helpers.click_button_matching_css_and_html(driver, ".modal_container_footer .textUp", "Save")
    for _ in range(1, 4):
        if helpers.element_exists_and_displayed(driver, "#textmessage #temporary_text_panel"):
            return True
        sleep(1)
    return False


def check_audio_breakout(driver):
    """
    Once inside Session click to activate Microphone, wait, check for speaking, then turn off
    """
    helpers.click_button_matching_css(driver, ".stream_control.stream_control_audio")
    sleep(1)
    # Audio should be turned on, checking 3 times
    for _ in range(1, 4):
        if helpers.element_exists_and_displayed(driver, ".stream.stream_hide_user_bar.ot-layout.unmuted.control_on.stream_layout_best_fit."
                                                        "inactive.has_stream.speaking"):
            helpers.click_button_matching_css(driver, ".stream_control.stream_control_audio")
            return True
        sleep(1)
    return False


def check_video_breakout(driver):
    """
    Once inside Session click to activate Camera, wait, then turn off
    """
    helpers.click_button_matching_css(driver, ".stream_control.stream_control_video")
    sleep(1)
    for _ in range(1, 4):
        if helpers.element_exists_and_displayed(driver, ".stream_video .OT_widget-container .OT_video-element"):
            helpers.click_button_matching_css(driver, ".stream_control.stream_control_video")
            return True
        sleep(1)
    return False


def check_audio_mainstage(driver):
    """
    Once inside Session click to activate Microphone, wait, check for speaking, then turn off
    """
    helpers.click_button_matching_css(driver, ".stream_control.stream_control_audio")
    sleep(1)
    # Audio should be turned on, checking 3 times
    for _ in range(1, 4):
        if helpers.element_exists_and_displayed(driver, ".stream.speaking.unmuted"):
            helpers.click_button_matching_css(driver, ".stream_control.stream_control_audio")
            return True
        sleep(1)
    return False


def check_video_mainstage(driver):
    """
    Once inside Session click to activate Camera, wait, then turn off
    """
    helpers.click_button_matching_css(driver, ".stream_control.stream_control_video")
    sleep(2)
    if helpers.element_exists_and_displayed(driver, ".OT_mirrored.OT_root.OT_publisher.OT_fit-mode-cover.OT_audio-only"):
        return False
    sleep(1)
    helpers.click_button_matching_css(driver, ".stream_control.stream_control_video")
    return True


def check_audio_panel(driver):
    """
    Once inside Session click to activate Microphone, wait, check for speaking, then turn off
    """
    helpers.click_button_matching_css(driver, ".stream_control.stream_control_audio")
    sleep(1)
    # Audio should be turned on, checking 3 times
    for _ in range(1, 4):
        if helpers.element_exists_and_displayed(driver, ".stream.unmuted.speaking"):
            helpers.click_button_matching_css(driver, ".stream_control.stream_control_audio")
            return True
        sleep(1)
    return False


def check_video_panel(driver):
    """
    Once inside Session click to activate Camera, wait, then turn off
    """
    helpers.click_button_matching_css(driver, ".stream_control.stream_control_video")
    sleep(2)
    if helpers.element_exists_and_displayed(driver, ".OT_mirrored.OT_root.OT_publisher.OT_fit-mode-cover.OT_audio-only"):
        return False
    sleep(1)
    helpers.click_button_matching_css(driver, ".stream_control.stream_control_video")
    return True


def type_in_chat(driver):
    """
    Once inside the Session enter test yyyy-mm-dd into chat pane and assert equality
    """
    message = f"test {date.today()}"
    helpers.set_input_text(driver, ".submit_container .form_horizontal input", message)
    sleep(1)
    helpers.set_input_text(driver, ".submit_container .form_horizontal input", Keys.ENTER)
    sleep(1)
    helpers.find_last_message_in_chat(
        driver, ".stream_chat_pane  .messages_container .messages_scroll_container .message_wrapper:last-child .message"
    )
    # Assertion is inside helpers.find_last_message_in_chat


def type_feed_post(driver):
    """
    Once navigated to Social feed, click Add post button, type message and click submit
    """
    helpers.click_button_matching_css(driver, ".two_column_container .two_column_list_panel_right .add_button_module .CSSButton_text")
    sleep(2)
    message = f"test {date.today()}"
    helpers.set_input_text(driver, "#scroll_container .centered_container .input_container textarea", message)
    sleep(1)
    helpers.click_button_matching_css(driver, "#internal_wrapper #submit_container .cssButton.standard_button_filled")
    # Assertion is inside verify_feed_post


def verify_feed_post(driver):
    """
    find most recently added feed post and compare to test message
    """
    helpers.find_last_feed_post(driver, ".two_column_list_panel_left #list .ui_relative.community_post_row:first-child .description"
                                        " .content_description")
    # Assertion is inside helpers.find_last_feed_post


def delete_feed_post(driver):
    """
    delete newly created test social feed post, assert post is removed
    """
    helpers.click_button_matching_css(driver, ".two_column_list_panel_left #list .community_post_row:first-child .options")
    sleep(2)
    helpers.click_button_matching_css_and_html(driver, "#buttons_container .button", "Delete")
    sleep(2)
    helpers.click_button_matching_css(driver, ".confirm_notice .start_button_container #ok_button .CSSButton_text")
    sleep(3)
    helpers.deleted_feed_post(driver, ".two_column_list_panel_left #list .community_post_row:first-child .description .content_description")
    # Assertion is made inside helpers.deleted_feed_post


def emoji_react(driver):
    """
    Once inside the Session react with quick emojis and return true if they are displayed
    """
    helpers.click_button_matching_css_and_html(driver, ".stream_control_bar_emoji .stream_control_emoji_picker .on_off", "React")
    sleep(1)
    helpers.click_button_matching_css(driver, ".emoji_container.shown .emoji-picker__emojis > div:nth-child(20) > button:nth-child(3)")
    sleep(0.2)
    helpers.click_button_matching_css(driver, ".emoji_container.shown .emoji-picker__emojis > div:nth-child(20) > button:nth-child(4)")
    for _ in range(1, 4):
        if helpers.element_exists_and_displayed(driver, ".stream_control_bar .stream_control_bar_emoji .emoji_float_container"):
            return True
        sleep(0.5)
    return False


def check_video_player(driver):
    for _ in range(1, 4):
        if helpers.element_exists_and_displayed(driver, ".stream_control_bar_container .stream_control_bar_base_publisher"):
            return True
        sleep(1)
    return False


def click_home_logo(driver):
    helpers.click_button_matching_css(driver, ".left_container .navigation_logo")


def check_mini_player(driver):
    for _ in range(1, 4):
        if helpers.element_exists_and_displayed(driver, "#miniplayer .miniplayer"):
            return True
        sleep(1)
    return False
