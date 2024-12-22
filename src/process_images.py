from src.get_image_urls import search_image_on_google, search_results_url
from src.extract_images import extract_images_from_pdf
from src.constants import image_folder
import os

def process_images_in_directory(pdf_path, image_directory,output_file="./plagarism_results/image_search_results.txt"):
    """
    Extracts images from a PDF, processes each image in a directory, searches for its source on Google, 
    and writes the results to an output file.

    Args:
        pdf_path (str): Path to the input PDF file from which images will be extracted.
        image_directory (str): Path to the directory where extracted images will be saved.
        output_file (str): Path to the output text file where search results will be stored. Defaults to 
                           './plagarism_results/image_search_results.txt'.

    Returns:
        None: Writes the results of image searches to the specified output file.

    Functionality:
        1. Creates the image directory if it does not exist.
        2. Extracts images from the PDF using `extract_images_from_pdf` and saves them in the specified directory.
        3. Iterates through all files in the image directory:
            - Processes only image files (e.g., `.png`, `.jpg`).
            - Searches for each image on Google using `search_image_on_google`.
            - Appends the image path and result URL to a list if a URL is found.
        4. Writes all results (image paths and corresponding result URLs) to the specified output file.
    """
    # Create the directory if it doesn't exist
    if not os.path.exists(image_directory):
        os.makedirs(image_directory)
    
    extract_images_from_pdf(pdf_path, image_directory)

    # Initialize a list to store results
    all_results = []

    
    # Loop through each image file in the directory
    for filename in os.listdir(image_directory):
        if filename.endswith(".png") or filename.endswith(".jpg"):  # Add other image formats if needed
            image_path = os.path.join(image_directory, filename)

            # Search for the image on Google and get the result URL
            result_url = search_image_on_google(image_path)

            if result_url:
                # Append result to the list
                all_results.append((image_path, result_url))
                # Pass the image path and result URL to search_results_url function
                #search_results_url(image_path, result_url)

            else:
                print(f"No result URL found for image: {filename}")
        else:
            print(f"Skipping non-image file: {filename}")
    
    # Write all results to the output file at once
    with open(output_file, "w", encoding="utf-8") as f:
        for image_path, result_url in all_results:
            f.write(f"Image Path: {image_path}\n")
            f.write(f"Result URL: {result_url}\n")
            f.write("\n" + "-" * 40 + "\n")

if __name__ == "__main__":
    process_images_in_directory('/Users/sachinmishra/Desktop/Testing/plagarism_checker/data/LogisticRegression-LogisticRegression-1.pdf', '/Users/sachinmishra/Desktop/Testing/plagarism_checker/extracted_images')