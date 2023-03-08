import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up the Chrome driver
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the webpage
driver.get('https://example.com')

# Find and click on the sign-in button
sign_in_button = driver.find_element_by_xpath('//button[@id="sign-in-button"]')
sign_in_button.click()

# Find and click on the sign in with Google account button
google_sign_in_button = driver.find_element_by_xpath('//button[@id="google-sign-in-button"]')
google_sign_in_button.click()

# Wait for the Google sign-in page to load
time.sleep(2)

# Find the email input field and enter the email address
email_input = driver.find_element_by_xpath('//input[@type="email"]')
email_input.send_keys('your_email_address_here')

# Click on the next button
next_button = driver.find_element_by_xpath('//div[@id="identifierNext"]')
next_button.click()

# Wait for the password input field to appear
time.sleep(2)

# Find the password input field and enter the password
password_input = driver.find_element_by_xpath('//input[@type="password"]')
password_input.send_keys('your_password_here')

# Click on the next button
next_button = driver.find_element_by_xpath('//div[@id="passwordNext"]')
next_button.click()

# Wait for the sign-in to complete
time.sleep(2)

# Get the cookies after successful login
cookies = driver.get_cookies()

# Close the browser
driver.quit()

