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
                if i >= 2:  # Stop after the first 3 links
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





