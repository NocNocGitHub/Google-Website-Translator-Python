from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# Set Chrome options to enable translation
options = Options()
options.add_experimental_option("prefs", {
    "translate_whitelists": {"en": ""},  # Translate any language to English
    "translate":{"enabled":"true"}
})

# Create a Chrome webdriver instance
driver = webdriver.Chrome(options=options)

# Replace with the link you want to open
link = "https://www.google.com/"
driver.get(link)

# Function to translate the current page
def translate_page():
    try:
        # Wait for the translation confirmation bar to appear
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "translate-bar"))
        )

        # Click the "Translate" button
        translate_button = driver.find_element(By.ID, "translate-button")
        translate_button.click()
    except NoSuchElementException:
        # Translation bar not found (page might already be in English)
        pass

# Translate the initial page
translate_page()

# Monitor for page changes and translate accordingly
while True:
    try:
        # Wait for any page change events (refresh, new page, etc.)
        WebDriverWait(driver, 10).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        translate_page()
    except Exception as e:
        print("Error occurred:", e)
        break

# Keep the browser open until manually closed
driver.quit()  # Uncomment this line to close the browser automatically
