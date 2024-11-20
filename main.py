import streamlit as st
from src.chunk_document import no_of_searches
#from src.chunk_pdf import no_of_searches
from src.get_links import search_multiple_queries
from src.scrape_content import scrape_website_content
from src.text_clean_helper import clean_string
from src.constants import image_folder
from src.match_results import parse_and_compare
from src.process_images import process_images_in_directory
from src.extract_images import extract_images_from_pdf
from src.get_image_urls import search_image_on_google, search_results_url
import tempfile



def get_file_path(uploaded_file):
    if uploaded_file is not None:
        # Save uploaded file to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(uploaded_file.read())
            temp_file_path = temp_file.name
        return temp_file_path

def get_quries(temp_file_path):
    # Extract text from the PDF using the temporary file path
    st.write("Extracting text from the PDF...")
    
    queries = no_of_searches(temp_file_path)  # Pass the file path to your function
    st.write("Generated Queries:")
    return queries



st.title("PDF Query Generator")

# File uploader to upload a PDF
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
file_path= get_file_path(uploaded_file)

if st.button("Submit"):
    all_queries= get_quries(file_path)
    st.write(all_queries)

    
if st.button("Generate Text Report"):
    
    queries= get_quries(file_path)
    with st.status("Fetching Links..."):
        search_results= search_multiple_queries(queries[0:2])
        st.write("Links Fetched Sucessfully...!")
    
    with st.status("Scrapping  Content..."):
        query_content_dict= scrape_website_content(search_results)
        st.write("Scrapping  Sucessfull...!")

    with st.status("Generating Report...!"):
        parse_and_compare(query_content_dict)
        st.write("Report Generated & Results written to 'query_matches.txt file")
        
        file_path= "./plagarism_results/query_matches.txt"
        with open(file_path , "r", encoding="utf-8") as file:
            file_content = file.read()

        # Display the text content on the Streamlit app
        st.write("Detailed Report")
        st.text(file_content)

        # Provide a download button for the text file
        st.download_button(
            label="Download Report",
            data=file_content,
            file_name="downloaded_text_file.txt",
            mime="text/plain"
        )

    
if st.button("Generate Image Report"):
    with st.status("Extracting Images and searching for the match..."):
        process_images_in_directory(file_path,image_folder)
        st.write("Image search comapleted suscessfully !")

        file_path1= "./plagarism_results/image_search_results.txt"
        with open(file_path1 , "r", encoding="utf-8") as file:
            file_content = file.read()

        # Provide a download button for the text file
        st.download_button(
            label="Download Image Report",
            data=file_content,
            file_name="downloaded_image_file.txt",
            mime="text/plain"
        )


