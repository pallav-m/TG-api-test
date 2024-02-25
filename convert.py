import shutil

from reportlab.pdfgen import canvas
from pdf2image import convert_from_path
from PIL import Image
import os

def convert_image_to_pdf(input_image_path, output_pdf_path):
    # Open the image file
    image = Image.open(input_image_path)

    # Create a PDF file
    pdf_canvas = canvas.Canvas(output_pdf_path, pagesize=image.size)

    # Draw the image on the PDF canvas
    pdf_canvas.drawImage(input_image_path, 0, 0, width=image.width, height=image.height)

    # Save the PDF file
    pdf_canvas.save()

    print(f"Conversion successful. PDF saved to {output_pdf_path}")

# if __name__ == "__main__":
#     # Defining input and output file paths
#     input_image_path = "photo_2024-02-08_11-18-54.jpg"
#
#
#     output_pdf_path = "./converted-pdf/"
#
#     convert_image_to_pdf(input_image_path, output_pdf_path)


def convert_pdf_to_image(input_pdf_path, output_image_path):
    # Convert PDF to list of images
    images = convert_from_path(input_pdf_path)

    # Save each page as a separate JPEG image
    for i, image in enumerate(images):
        image.save(f"{output_image_path}Page{i + 1}.jpg", "JPEG")
    print(dir(images))
    #return images

def clear_directory(directory_path):
    try:
        # Iterate over all files and subdirectories in the given directory
        for file_name in os.listdir(directory_path):
            file_path = os.path.join(directory_path, file_name)

            # Check if it's a file and delete it
            if os.path.isfile(file_path):
                os.unlink(file_path)
            # Check if it's a directory and delete it recursively
            # elif os.path.isdir(file_path):
            #     shutil.rmtree(file_path)

        print(f"Directory '{directory_path}' cleared successfully.")
    finally:
        pass


if __name__ == "__main__":
    # Replace 'input_file.pdf' with the path to your PDF file
    input_pdf_path = "Notice_CGL2022_01052023.pdf"

    # Replace 'output_image' with the desired output image file name (without extension)
    output_image_path = "./testing-images/"

    convert_pdf_to_image(input_pdf_path, output_image_path)

