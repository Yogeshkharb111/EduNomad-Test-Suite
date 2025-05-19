from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

desired_caps = {
    "platformName": "Android",
    "deviceName": "Android Emulator",
    "appPackage": "com.your.edunomad",
    "appActivity": "com.your.edunomad.MainActivity",  # Or the activity that shows course list
    "automationName": "UiAutomator2",
    "noReset": True
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

try:
    time.sleep(5)
    
    # Scroll and find a course card
    course_list = driver.find_elements(AppiumBy.ID, "com.your.edunomad:id/courseCard")
    assert len(course_list) > 0
    print(f"✅ Found {len(course_list)} course(s) on the list.")

    # Click on the first course
    course_list[0].click()
    time.sleep(3)

    # Verify course detail screen by checking for topic list or course title
    detail_title = driver.find_element(AppiumBy.ID, "com.your.edunomad:id/courseTitle")
    assert detail_title is not None
    print("✅ Course detail screen loaded.")

except Exception as e:
    print("❌ Course list test failed:", e)

finally:
    driver.quit()
