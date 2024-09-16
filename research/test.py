from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def google_search(query, driver):
    # Open Google
    driver.get("https://www.google.com")
    
    # Find the search bar and enter the query
    search_box = driver.find_element(By.NAME, "q")
    search_box.clear()
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    
    # Allow some time for results to load
    time.sleep(2)
    
    # Grab the links from the search result page using the class you specified
    links = []
    search_results = driver.find_elements(By.CLASS_NAME, "LC20lb")
    for result in search_results:
        parent = result.find_element(By.XPATH, "..")  # Get the parent <a> tag of the heading
        href = parent.get_attribute("href")
        links.append(href)
    
    return links

def search_multiple_queries(queries):
    # Initialize WebDriver (Make sure to provide the correct path to your chromedriver)
    driver = webdriver.Chrome()  # or webdriver.Firefox() if using Firefox
    
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

# Example list of queries
queries = ["Python web scraping", "LangChain framework", "Selenium with Python"]

# Call the function and get the results
search_results = search_multiple_queries(queries)

# Print the result dictionary
for query, links in search_results.items():
    print(f"\nQuery: {query}")
    for link in links:
        print(f"- {link}")

