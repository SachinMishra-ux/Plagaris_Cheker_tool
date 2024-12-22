from bs4 import BeautifulSoup
import re


def clean_string(input_string):

    """
    Cleans and processes an input string by removing unwanted characters, fixing spacing issues, 
    and improving readability.

    Args:
        input_string (str): The string to be cleaned.

    Returns:
        str: The cleaned and formatted string.

    Functionality:
        1. Removes null characters (`\x00`) and newline characters (`\n`).
        2. Adds spaces where needed:
            - Between lowercase and uppercase letters (e.g., "GPTis" -> "GPT is").
            - Before punctuation (e.g., "OpenAIandlaunched." -> "Open AI and launched .").
            - After punctuation if missing (e.g., "launched.This" -> "launched. This").
        3. Replaces multiple consecutive spaces with a single space.
        4. Strips leading and trailing whitespace.
    """
    # Remove \x00 and newline characters
    cleaned_string = input_string.replace("\x00", " ").replace("\n", " ")


    # Handle missing spaces by adding one between lower and uppercase letters or word breaks
    cleaned_string = re.sub(r'([a-z])([A-Z])', r'\1 \2', cleaned_string)
    cleaned_string = re.sub(r'(\w)([.,!?;:])', r'\1 \2', cleaned_string)  # Add space before punctuation

    # Add space between lowercase and uppercase letters (e.g., "GPTis" -> "GPT is")
    cleaned_string = re.sub(r'([a-z])([A-Z])', r'\1 \2', cleaned_string)
    
    # Add space after punctuation if missing (e.g., "Open AIandlaunched" -> "Open AI and launched")
    cleaned_string = re.sub(r'([.,!?;:])([A-Za-z])', r'\1 \2', cleaned_string)
    
    # Replace multiple spaces with a single space
    cleaned_string = re.sub(r'\s+', ' ', cleaned_string)
    
    # Strip leading and trailing white spaces
    cleaned_string = cleaned_string.strip()
    
    return cleaned_string


def extract_body_content(html_content):
    """
    Extracts the content of the `<body>` tag from the provided HTML content.

    Args:
        html_content (str): The HTML content as a string.

    Returns:
        str: A string representation of the content inside the `<body>` tag. 
             If the `<body>` tag is not found, an empty string is returned.

    Functionality:
        - Parses the HTML content using BeautifulSoup.
        - Searches for the `<body>` tag within the parsed HTML structure.
        - Returns the string representation of the content inside the `<body>` tag, 
          or an empty string if no `<body>` tag is present.
    """
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):

    """
    Cleans the content of an HTML `<body>` tag by removing unnecessary elements and formatting the text.

    Args:
        body_content (str): The raw HTML content of the `<body>` tag.

    Returns:
        str: The cleaned and formatted text content extracted from the `<body>` tag.

    Functionality:
        - Parses the provided HTML content using BeautifulSoup.
        - Removes `<script>` and `<style>` tags along with their content.
        - Extracts text content from the remaining HTML.
        - Strips leading and trailing whitespace from each line.
        - Joins non-empty lines with newline characters to create a clean, readable format.
    """
    
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


