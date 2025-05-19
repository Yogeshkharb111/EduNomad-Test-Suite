from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

desired_caps = {
    "platformName": "Android",
    "deviceName": "Android Emulator",  
    "appPackage": "com.your.edunomad",  
    "appActivity": "com.your.edunomad.SignInActivity",  
    "automationName": "UiAutomator2",
    "noReset": True
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

try:
    time.sleep(3)
    
    # Input email
    email_field = driver.find_element(AppiumBy.ID, "com.your.edunomad:id/emailEditText")
    email_field.send_keys("testuser@gmail.com")
    
    # Input password
    password_field = driver.find_element(AppiumBy.ID, "com.your.edunomad:id/passwordEditText")
    password_field.send_keys("testpass123")
    
    # Click Login button
    login_button = driver.find_element(AppiumBy.ID, "com.your.edunomad:id/loginButton")
    login_button.click()

    time.sleep(5)

    # Verify redirection by checking for home screen element
    home_element = driver.find_element(AppiumBy.ID, "com.your.edunomad:id/homeWelcomeText")
    assert home_element is not None
    print("✅ Sign-in test passed.")

except Exception as e:
    print("❌ Sign-in test failed:", e)

finally:
    driver.quit()
