from src.chunk_document import no_of_searches
from src.get_links import search_multiple_queries
from src.scrape_content import scrape_website_content
from src.text_clean_helper import clean_string
import re

def parse_and_compare(query_content_dict):
    # Open a text file for writing the output
    with open("./plagarism_results/query_matches.txt", "w") as file:
        file.write("\n")
        # Iterate through each query and its corresponding list of link-content dictionaries
        for query, link_content_list in query_content_dict.items():
            file.write(f"Query: {query}\n")
            found_match = False
            
            # Compare the query with each content
            for link_content in link_content_list:
                for link, content in link_content.items():
                    content = clean_string(content)
                    # Use regular expression to check if the query matches the content
                    if re.search(re.escape(query), content, re.IGNORECASE):
                        # If a match is found, write the matching content and link to the file
                        file.write(f"Matched in {link}\n")
                        found_match = True
            
            # If no match is found for the query, note it in the file
            if not found_match:
                file.write("No matching results found.\n")
            
            # Write a separator for better readability
            file.write("\n" + "-"*50 + "\n\n")
    
    print("Results written to 'query_matches.txt'")


if __name__ == "__main__":
    path= "./data/test1.pdf"
    queries= no_of_searches(path)

    print(type(queries))
    print(queries)

    queries= queries[0:6]

    # Call the function and get the results
    search_results = search_multiple_queries(queries)

    scraped_content_dict= scrape_website_content(search_results)
    # Call the function
    parse_and_compare(scraped_content_dict)

"""
# Example usage
query_content_dict = {
    'query1': [{'link1': 'some content1'}, {'link2': 'some content2'}, {'link3': 'some content2some content2'}],
    'query2': [{'link4': 'some content4'}, {'link5': 'some content5'}, {'link6': 'some content6'}],
    'query3': [{'link7': 'some content7'}, {'link8': 'some content8'}, {'link9': 'some content9'}]
}
"""

