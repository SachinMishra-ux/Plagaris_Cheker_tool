from constants import chrome_driver_path
from selenium import webdriver
import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def search_image_on_google(image_path):
    options= webdriver.ChromeOptions()
    driver=  webdriver.Chrome(service= Service(chrome_driver_path), options= options)
    # Set up the WebDriver (assuming you are using Chrome)

    # Open Google Images search
    driver.get("https://images.google.com")

    # Click on the 'Search by image' button (camera icon)
    search_by_image_button = driver.find_element(By.CLASS_NAME, "Gdd5U")
    search_by_image_button.click()

    # Upload the image file
    upload_tab = driver.find_element(By.LINK_TEXT, "Upload an image")
    upload_tab.click()

    # Locate file input element and upload the image
    file_input = driver.find_element(By.NAME, "encoded_image")
    file_input.send_keys(image_path)

    # Allow time for the search to complete
    time.sleep(5)

    # Extract and print the results page URL (or you can further process it)
    print(driver.current_url)

    # Optionally, you can scrape the search results or capture the page
    # For now, just keep the page open for the user to explore results
    time.sleep(10)

    # Close the browser
    driver.quit()

# Example usage
image_path = "./extracted_images/image_page7_0.png"
search_image_on_google(image_path)
