import streamlit as st
from src.chunk_document import no_of_searches
from src.get_links import search_multiple_queries
from src.scrape_content import scrape_website_content
from src.text_clean_helper import clean_string,remove_queries_by_index
from src.constants import image_folder
from src.match_results import parse_and_compare
from src.process_images import process_images_in_directory
##from src.extract_images import extract_images_from_pdf
#from src.get_image_urls import search_image_on_google, search_results_url
import tempfile
import os



def get_file_path(uploaded_file):
    if uploaded_file is not None:
        # Save uploaded file to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(uploaded_file.read())
            temp_file_path = temp_file.name
        return temp_file_path

def get_quries(temp_file_path):
    with st.status("Extracting text from the PDF..."):
        # Extract text from the PDF using the temporary file path
        queries = no_of_searches(temp_file_path)  # Pass the file path to your function
        st.write("Generated Queries:")
        return queries


#remove_queries_by_index

# Open sidebar and display queries
with st.sidebar:
    st.header("Plagiarism Checker Tool")

    # File uploader to upload a PDF
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
    file_path= get_file_path(uploaded_file)

    # Button to trigger processing
    submit_button = st.button("Submit")
    text_report_button= st.button("Generate Text Report")
    image_report_button= st.button("Generate Image Report")
    exit_button = st.button("Exit")
    # Logic for Exit Button


# Sidebar logic when "Submit" button is clicked
if submit_button:
    if file_path:  # Ensure a file has been uploaded
        all_queries = get_quries(file_path)
        st.write("All Queries:", all_queries)
        
    else:
        st.warning("Please upload a PDF file before submitting.")
    
    

        
if text_report_button: 
    queries= get_quries(file_path)
    with st.status("Fetching Links..."):
        search_results= search_multiple_queries(queries[0:])
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

        
if image_report_button:
    with st.status("Extracting Images and searching for the match..."):
        process_images_in_directory(file_path,image_folder)
        st.write("Image search completed suscessfully !")

        file_path2= "./plagarism_results/image_search_results.txt"
        with open(file_path2 , "r", encoding="utf-8") as file:
            file_content = file.read()

        st.text(file_content)
        # Provide a download button for the text file
        st.download_button(
            label="Download Image Report",
            data=file_content,
            file_name="downloaded_image_file.txt",
            mime="text/plain"
        )

if exit_button:
    st.write("Exiting the application...")
    os._exit(0)  # Forcefully terminate the program

