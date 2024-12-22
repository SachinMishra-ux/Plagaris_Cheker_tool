from src.chunk_document import no_of_searches
from src.constants import chrome_driver_path

import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


def google_search(query, driver):

    """
    Performs a Google search for a given query and retrieves the top 3 result links.

    Args:
        query (str): The search query to be entered into Google.
        driver (webdriver): An instance of Selenium WebDriver, configured for browser automation.

    Returns:
        list: A list containing the URLs of the top 3 search results. If no results are found or an error occurs, an empty list is returned.

    Functionality:
        1. Opens the Google homepage.
        2. Locates the search bar using its `name` attribute and enters the provided query.
        3. Submits the search form and waits for the results to load.
        4. Extracts the URLs of the top 3 search results by:
            - Locating the result titles using their `CLASS_NAME`.
            - Navigating to the parent anchor (`<a>`) tag of each title to extract the `href` attribute.
        5. Handles scenarios where no search results are available or errors occur during execution.

    Notes:
        - Requires the Selenium WebDriver library for browser automation.
        - The `CLASS_NAME` used for locating search results ("LC20lb") must match Google's current DOM structure. This may change over time.
        - A pre-configured WebDriver instance must be passed as the `driver` argument, and it must be capable of accessing the internet.
    """

    try:
        # Open Google
        driver.get("https://www.google.com")
        
        # Find the search bar and enter the query
        #search_box = driver.find_element(By.NAME, "q")
        search_box= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q")))
        search_box.clear()
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
        
        # Allow some time for results to load
        time.sleep(5)

        # Wait for the search results to load and become visible
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "LC20lb"))
        )
        
        # Grab the links from the search result page
        links = []

        search_results = driver.find_elements(By.CLASS_NAME, "LC20lb")  # Adjust XPath if needed
        if not search_results:
                print(f"No search results for query: {query}")
        else:
            for i, result in enumerate(search_results):
                if i >= 3:  # Stop after the first 3 links
                    break
                try: 
                    parent = result.find_element(By.XPATH, "..")
                    href = parent.get_attribute("href")
                    links.append(href)

                except Exception as e:
                    print(f"Error: {e}")
    except Exception as e:
        # Log the error but do not stop execution
        print(f"An error occurred while searching for '{query}': {e}")
        return []
    
    return links

def search_multiple_queries(queries):

    """
    Performs Google searches for multiple queries and retrieves the top result links for each query.

    Args:
        queries (list): A list of search queries (strings) to be executed on Google.

    Returns:
        dict: A dictionary where keys are the queries and values are lists of URLs (top search result links) corresponding to each query. 
              If no results are found for a query, the value is an empty list.

    Functionality:
        1. Configures a Selenium WebDriver instance in headless mode for automated browser interaction.
        2. Iterates over each query in the provided list:
            - Calls the `google_search` function to perform the search.
            - Stores the resulting links in a dictionary with the query as the key.
        3. Prints the number of links fetched for each query during execution.
        4. Ensures the WebDriver instance is properly closed after processing all queries.

    Notes:
        - Requires the Selenium WebDriver library for browser automation.
        - The `google_search` function is expected to handle individual query searches and return a list of links.
        - A pre-configured WebDriver instance is created within this function with options for headless execution.
        - Ensure the Google DOM structure (e.g., class names used in `google_search`) matches the current Google page layout.
    """
    options= webdriver.ChromeOptions()
    options.add_argument("--headless")  # Enable headless mode
    options.add_argument("--disable-gpu")  # Disable GPU acceleration (recommended for headless mode)
    driver=  webdriver.Chrome(service= Service(chrome_driver_path), options= options)
    results = {}
    
    try:
        for query in queries:
            links = google_search(query, driver)
            results[query] = links
            print(f"Fetched {len(links)} links for query: '{query}'")
    
    finally:
        # Close the browser once done
        driver.quit()
    
    return results

if __name__ == "__main__":

    # Example list of queries
    
    queries = no_of_searches("./data/LogisticRegression-LogisticRegression-1.pdf")
    print(queries)
    # Call the function and get the results
    search_results = search_multiple_queries(queries)

    # Print the result dictionary
    for query, links in search_results.items():
        print(f"\nQuery: {query}")
        for link in links:
            print(f"- {link}")





