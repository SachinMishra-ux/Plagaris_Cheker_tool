import fitz  # PyMuPDF
import io
from PIL import Image
import os
from src.constants import image_folder



def extract_images_from_pdf(pdf_path, image_folder):
    
    pdf_file = fitz.open(pdf_path)
    images = []
    
    # Iterate over each page in the PDF
    for page_number in range(len(pdf_file)):
        page = pdf_file.load_page(page_number)
        images_list = page.get_images(full=True)
        
        # If page contains images, extract them
        for img_index, img in enumerate(images_list):
            xref = img[0]
            base_image = pdf_file.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]  # image extension (jpg, png)
            image = Image.open(io.BytesIO(image_bytes))
            
            # Save the image to the "scraped images" directory
            image_path = os.path.join(image_folder, f"image_page{page_number+1}_{img_index}.{image_ext}")
            image.save(image_path)

            
            images.append(image)  # Append the PIL image object to the list
    
    return images  # Returns a list of images

if __name__ == "__main__":
    # Example usage
    pdf_path = "./data/LogisticRegression-LogisticRegression-1.pdf"
    images = extract_images_from_pdf(pdf_path, image_folder)

    # Display the extracted images
    #for img in images:
    #    img.show()  # Display the image
