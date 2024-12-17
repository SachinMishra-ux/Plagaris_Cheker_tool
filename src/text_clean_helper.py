from bs4 import BeautifulSoup


def clean_string(input_string):
    # Remove \x00 and newline characters
    cleaned_string = input_string.replace("\x00", " ").replace("\n", " ")
    
    # Strip leading and trailing white spaces
    cleaned_string = cleaned_string.strip()
    
    return cleaned_string

def remove_queries_by_index(queries, indices_to_remove):
    """
    Removes queries at specified index positions from the list.
    
    Parameters:
        queries (list): The list of queries.
        indices_to_remove (list): List of index positions to remove.
    
    Returns:
        list: The updated list of queries with specified indices removed.
    """
    # Convert indices_to_remove to a set for faster lookups
    indices_to_remove = set(indices_to_remove)
    
    # Use list comprehension to filter out queries at specified indices
    updated_queries = [query for idx, query in enumerate(queries) if idx not in indices_to_remove]
    
    return updated_queries

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    # Get text or further process the content
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip())

    return cleaned_content

if __name__ == "__main__":
    print('testing')
    #body_content= extract_body_content(html_content)
    #clean_body_content(body_content)


