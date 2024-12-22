from src.text_clean_helper import extract_body_content, clean_body_content

from src.constants import chrome_driver_path

import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service

import time



# Example list of queries
#queries = ["Intro to classi cation - Logistic regression - 1 One should look for what is and not what he thinks should be. (Albert Einstein)DAT SOCI", "Logistic regression: Topic introduction In this part of the course, we will cover the following concepts: Logistic regression use cases and theory behind it Data transformation necessary for logistic regression Implementation of logistic regression on a dataset Model performance evaluation and tuning Logistic regression-1 1", "Quick Activity Suppose we want to predict whether a person will purchase a certain car or not What nume rical data might be relevant for making this prediction? What additional qualitative or categorical data might be relevant? How migh t you handle variables like marital status, education level, or gender? Logistic regression-1 2"]

def scrape_website_content(search_results):

    """
    Scrapes website content for a set of search results and returns the cleaned content for each query.

    Args:
        search_results (dict): A dictionary where keys are search queries (str) and values are lists of URLs (str) 
                               to scrape content from.

    Returns:
        dict: A dictionary where each key is a query (str) and its value is a list of dictionaries. 
              Each dictionary contains a URL (key) and its corresponding cleaned content (value).

    Functionality:
        1. Sets up a Selenium WebDriver in headless mode.
        2. Iterates over the search results:
            - For each query, fetches the list of URLs associated with it.
            - For each URL:
                - Loads the webpage using Selenium.
                - Extracts and processes the HTML content.
                - Stores the cleaned content along with the URL in a dictionary.
        3. Returns a dictionary containing the scraped content for each query.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Enable headless mode
    options.add_argument("--disable-gpu")  # Disable GPU acceleration (recommended for headless mode)
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
    
    # Dictionary to store the results
    query_content_dict = {}
    
    # Iterate through each query and its associated links
    for query, links in search_results.items():
        print(f"Scraping content for query: {query}")
        
        all_links = []
        scraped_content = []
        
        for link in links:
            print('Scraping..', link)
            try:
                # Open the link in the browser
                driver.get(link)
                
                # Wait for the page to load
                time.sleep(10)
                
                # Extract the page source
                html = driver.page_source
                print('Page loaded successfully..')
                
                # Process the HTML content (assuming you have extract and clean methods)
                body_content = extract_body_content(html)
                cleaned_body_content = clean_body_content(body_content)
                
                # Store the link and content
                all_links.append(link)
                scraped_content.append(cleaned_body_content)
                
            except Exception as e:
                print(f"Error while scraping {link}: {e}")
        
        # Create a list of dictionaries where each dict contains link-content pairs for the current query
        link_content_dict = [{link: content} for link, content in zip(all_links, scraped_content)]
        
        # Store the results for the current query
        query_content_dict[query] = link_content_dict
    
    # Quit the driver after all queries are processed
    driver.quit()
    
    return query_content_dict




