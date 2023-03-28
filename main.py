# TODO General logging, Django Front End, Testing/assertions.
# TODO remove/rework sleep
# TODO integrate with Slack Webhook to message build passed
# TODO reach out to DevOps and look over scripts to push builds with AWS
# TODO possible drop down front end of AWS environments
# TODO create decorator that says "beginning of test, initialize driver, run test, destroy driver once tests completed" this way each test is fresh

# from selenium.webdriver.common.by import By
# from time import sleep
#
# import helpers
# from actions import interact, nav
# import driver

# logging.basicConfig()
# logging.root.setLevel(logging.INFO)
# _logger = logging.getLogger(__name__)


# def set_audio_video_devices():
#     sleep(3)
#     helpers.click_button_matching_css(driver, '.user_information_container')
#     sleep(1)
#     helpers.click_button_matching_css_and_html(driver,
#                                                '.profile_dropdown .dropdown_items_container .dropdown_item .text',
#                                                "Camera &amp; Microphone")
#     sleep(1)
#     helpers.click_button_matching_css_and_html(driver, '.modal_container_footer .CSSButton_text', "Save")


# Function to Enable Audio inside Session

# def check_audio():
#     sleep(10)
#     helpers.click_button_matching_css_and_html(driver, '.stream_control.stream_control_audio .on_off', "Audio")
#     sleep(10)
#     helpers.click_button_matching_css_and_html(driver, '.stream_control.stream_control_audio .on_off', "Audio")
# x = driver.find_elements(By.CSS_SELECTOR, '.stream_control.stream_control_audio .on_off')
# for button in x:
#     if "Audio" in button.get_attribute("innerHTML"):
#         button.click()
#         sleep(10)
#         button.click()
#         break


# Function to Enable Video inside Session
# TODO assert video is being produced and seen

# def check_video():
#     sleep(5)
#     helpers.click_button_matching_css_and_html(driver, '.stream_control.stream_control_video .on_off', "Video")
#     sleep(10)
#     helpers.click_button_matching_css_and_html(driver, '.stream_control.stream_control_video .on_off', "Video")
# x = driver.find_elements(By.CSS_SELECTOR, '.stream_control.stream_control_video .on_off')
# for button in x:
#     if "Video" in button.get_attribute("innerHTML"):
#         button.click()
#         sleep(10)
#         button.click()
#         break


# def emoji_react():
#     sleep(5)
#     x = driver.find_elements(By.CSS_SELECTOR, '.stream_control_bar_emoji .stream_control_emoji_picker .on_off')
#     for button in x:
#         if "React" in button.get_attribute("innerHTML"):
#             button.click()
#             break
#     emlaugh = driver.find_elements(By.CSS_SELECTOR, '.emoji-picker__container .emoji-picker__emoji')
#     for emojilaugh in emlaugh:
#         if "Laugh" in emojilaugh.get_attribute("title"):
#             sleep(2)
#             emojilaugh.click()
#             break
#     emwow = driver.find_elements(By.CSS_SELECTOR, '.emoji-picker__container .emoji-picker__emoji')
#     for emojiwow in emwow:
#         if "Wow" in emojiwow.get_attribute("title"):
#             sleep(2)
#             emojiwow.click()
#             break


# Function to test resizing functionality inside Session


# calling all the functions to the yard


# def full_build_test():
#     nav.navigate_to(driver, URL1)
#     if not interact.login(driver, username, userpassword):
#         _logger.error("Unsuccessful Login :(")
#         return
#     _logger.info("Successful Login :D")
#     interact.logout(driver)
#     sleep(3)
#     interact.login(driver, username, userpassword)
#     test_audio_video()
#     nav.navigate_to(driver, URL2, 5)
#     check_audio()
#     check_video()
#     type_in_chat()
#     emoji_react()
#
# full_build_test()
