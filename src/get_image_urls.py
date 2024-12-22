from src.constants import chrome_driver_path
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
import time

def search_image_on_google(image_path):

    """
    Automates the process of searching for an image on Google Images.

    Args:
        image_path (str): The local file path of the image to be searched.

    Returns:
        str: The URL of the Google search results page for the uploaded image.

    Functionality:
        1. Sets up a Chrome WebDriver instance in headless mode.
        2. Opens Google Images search page.
        3. Checks for and dismisses any sign-in iframe or pop-up modal that might block interaction.
        4. Locates the 'Search by image' button and clicks it.
        5. Locates the file upload input field, scrolls it into view if necessary, and uploads the image file.
        6. Waits for the URL of the search results to update and retrieves it.
        7. Closes the browser and returns the search results URL.

    Notes:
        - Requires the ChromeDriver executable (`chrome_driver_path` should be set) and the Selenium WebDriver library.
        - The WebDriver must be configured to work with the correct version of Google Chrome.
        - Ensure that the class names and XPath selectors used in the code are updated to match the current Google Images DOM structure, as these may change over time.
        - The `image_path` should point to a valid image file on the local filesystem.
        - This function may fail if Google's DOM structure changes or network issues occur.

    Exceptions Handled:
        - `NoSuchElementException`: Raised if expected elements are not found on the page.
        - `TimeoutException`: Raised if elements do not become interactable within the specified timeout period.
        - `ElementNotInteractableException`: Raised if elements are present but cannot be interacted with.

    Example:
        ```python
        image_url = search_image_on_google("/path/to/image.jpg")
        print(f"Search results can be found at: {image_url}")
        ```
    """
    # Set up the WebDriver (assuming you are using Chrome)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Enable headless mode
    options.add_argument("--disable-gpu")  # Disable GPU acceleration (recommended for headless mode)
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    # Open Google Images search
    driver.get("https://images.google.com")

    wait = WebDriverWait(driver, 12)

        # Check if there's an iframe or modal popup that blocks interaction
    try:
        print("Checking for sign-in iframe or pop-up...")
        iframe = driver.find_element(By.TAG_NAME, "iframe")
        if iframe:
            driver.switch_to.frame(iframe)
            print("Switched to iframe. Trying to dismiss pop-up.")
            stay_signed_out_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Stay signed out')]"))
            )
            stay_signed_out_button.click()
            print("Sign-in prompt dismissed from iframe.")
            driver.switch_to.default_content()  # Switch back to main content
        else:
            print("No iframe found.")
    except (NoSuchElementException, TimeoutException) as e:
        print(f"Sign-in iframe not found or did not appear: {e}")

    # Now proceed with the image search
    try:
        print("Attempting to locate 'Search by image' button...")
        search_by_image_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "nDcEnd"))  # Adjust the class name if necessary
        )
        print("Found 'Search by image' button.")
        ActionChains(driver).move_to_element(search_by_image_button).click().perform()

        print("Attempting to locate the file upload input field...")

        # Target the hidden input field using its type 'file'
        upload_file_input = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
        )

        # Scroll the input element into view (if necessary)
        driver.execute_script("arguments[0].scrollIntoView(true);", upload_file_input)
        time.sleep(2)  # Brief pause to ensure page settles

        # Directly interact with the input field by sending the file path
        upload_file_input.send_keys(image_path)
        print(f"File '{image_path}' successfully uploaded.")

        # Wait for the URL to update (optional step)
        WebDriverWait(driver, 5).until(
            EC.url_contains("search")
        )

        search_results_url = driver.current_url
        print("Search results URL:", search_results_url)

    except TimeoutException as te:
        print(f"Timeout while waiting for the upload file input: {te}")
    except ElementNotInteractableException as enie:
        print(f"Upload file input is not interactable: {enie}")
    

  
    finally:
        # Close the browser
        driver.quit()
        return search_results_url

def search_results_url(image_path, result_url,output_file="./plagarism_results/image_search_results.txt"):

    """
    Automates the retrieval of search results from a Google Images search URL and logs the results or errors.

    Args:
        image_path (str): The local file path of the image being searched.
        result_url (str): The URL of the Google Images search results page.
        output_file (str): The file path where results or error messages will be logged. Default is 
                           "./plagarism_results/image_search_results.txt".

    Functionality:
        1. Sets up a Chrome WebDriver instance in headless mode.
        2. Opens the specified search results URL.
        3. Attempts to locate and click the "Find image source" button.
        4. Handles the following scenarios:
            - If an error message is displayed, logs the error message along with the image path and result URL.
            - If no error message is found, retrieves up to the top 5 result URLs and logs them.
            - If no results are found, logs a message indicating no duplicate images or webpages were located.
        5. Writes all relevant data to the specified output file.
        6. Prints the top URLs or relevant messages to the console.

    Returns:
        None

    Notes:
        - Requires the ChromeDriver executable (`chrome_driver_path` should be set) and the Selenium WebDriver library.
        - Ensure that the class names and CSS selectors used in the code match the current Google Images DOM structure.
        - The output file will be appended to if it already exists.

    Exceptions Handled:
        - General exceptions are caught and logged, along with the exception message.

    Example:
        ```python
        search_results_url(
            image_path="/path/to/image.jpg",
            result_url="https://www.google.com/search?tbs=sbi:XYZ...",
            output_file="./results/image_search_results.txt"
        )
        ```
    """
    # Set up the WebDriver (assuming you are using Chrome)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Enable headless mode
    options.add_argument("--disable-gpu")  # Disable GPU acceleration (recommended for headless mode)
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
    wait = WebDriverWait(driver, 6)
    try:
        driver.get(result_url)
        # Click the "Find image source" button
        find_image_source_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "VTbk7c"))
        )
        find_image_source_button.click()

        # Check if the error message is present
        try:
            error_message_element = wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.U4WWNb"))
            )
            error_message = error_message_element.text
            print("Error message:", error_message)

            # Save the error message in the output file
            with open(output_file, "a") as f:
                f.write(f"\nImage Path: {image_path}\n")
                f.write(f"Result URL: {result_url}\n")
                f.write(f"Error: {error_message}\n")
                f.write("\n" + "-" * 40 + "\n")
        except:
            # Wait for the result to load
            wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "li.anSuc"))
            )

            # If error message is not found, proceed to get the URLs
            urls = driver.find_elements(By.CSS_SELECTOR, "li.anSuc a")
            if urls:
                top_urls = [url.get_attribute('href') for url in urls[:5]]
                print("Top 5 URLs:")
                for url in top_urls:
                    print(url)
                
                # Write the results to the file
                with open(output_file, "a") as f:
                    f.write(f"\nImage Path: {image_path}\n")
                    f.write(f"Result URL: {result_url}\n")
                    f.write("Top 5 URLs:\n")
                    for i, url in enumerate(top_urls, 1):
                        f.write(f"{i}. {url}\n")
                    f.write("\n" + "-" * 40 + "\n")
            else:
                print("Couldn't find webpages or duplicate images.")
                with open(output_file, "a") as f:
                    f.write(f"\nImage Path: {image_path}\n")
                    f.write(f"Result URL: {result_url}\n")
                    f.write("No webpages or duplicate images found.\n")
                    f.write("\n" + "-" * 40 + "\n")
    
    except Exception as e:
        print('An error occurred:', str(e))   




if __name__ == '__main__':

    # Example usage
    image_path = '/Users/sachinmishra/Desktop/Testing/plagarism_checker/extracted_images/imageedit_3_8309563390.png'  # Update the image path as needed
    url= search_image_on_google(image_path)

    #url1= "https://lens.google.com/search?ep=gisbubb&hl=en-IN&re=df&p=AbrfA8ogVr_7MqgQmTdHi9ekeBThTBFH4dqqBFb8W38RNFKnShnRA8Wt1Na4fw2b622kj4vgCCnpJLwMxF8nxSrz7YKH4ReewI_C456RekrQULYbk3zf2PWZzuvo1j74D8tUM5eg-VdU7YKec7D-ErTh85n1pSO2OLilu8s0x6X5tu-5A-ZJFNj4DJRgYMMASP5g69vfU6qbH6nprtm4E4Ud#lns=W251bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsIkVrY0tKR0ptWXpRME1USmlMVGMzWm1NdE5HVmpZeTFpTURObExUSm1ORGMyTTJVM01XVTNaUklmWnkxelZUSmFZMFYyTWpobGMwWldkMUYzZG5veE4wZ3ljMmRwTmtoNGF3PT0iLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsWyIzYTk5YmRmMC05ODE5LTRlOWItODMxYS1lN2I4MjEwYjBjYjUiXV0="
    #url2= "https://lens.google.com/search?ep=cntpubb&hl=en-US&re=df&s=4&p=AbrfA8oZWX7QIGwaQt9Kr3LuB9Teh3B7aSK3hSWiuohb-grbPYn6S8T58X_qsDmi6tUBjh4Gd-n_utFbdYSkodyAVl6tXnyKSaTKjuDLWOMJujZkHOlVR_GkyN3cneUX9-Xl1TfW0PWIx7IED1Q6nRRpx9Mf_a9rM4c6PcYQ6Y-MfTgK5J7gTwEPxneMixkybxRKsqIKfa3TAvSKGWnMAzwOk8Mds8jwOqnDLzGaI9N81lRVoaFBOYT4NG1Aea-Kz-MT7SLtuLaKtKsStEn5f6tysqspRAPTrf9xGzQo#lns=W251bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsIkVrY0tKR1ZoTW1NMk5XRmpMVGRrTkRndE5EaG1aUzFpTTJNeUxURm1ZMkU1WTJReU5XVmtaUklmV1RaUWNqbDJRbTVYZUVGU2MwWldkMUYzZG5veE4wWnRWakI1TmtoNGF3PT0iLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsWyIxOGJjZTgwYi1iMjhjLTRmZWUtYjhhYy0yNDZmMzIzYmQ3ZWYiXV0="
    search_results_url(image_path,url)

