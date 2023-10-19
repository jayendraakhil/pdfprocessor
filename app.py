from PyPDF2 import  PdfWriter,PdfReader
from PIL import Image
import os

class PdfProcessor:
    def combine_pdfs(self, input_files, output_file):
        pdf_writer = PdfWriter()
        for pdf_file in input_files:
            pdf_reader = PdfReader(pdf_file)
            for page_num in range(pdf_reader.getNumPages()):
                page = pdf_reader.getPage(page_num)
                pdf_writer.addPage(page)
        with open(output_file, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

    def separate_pdf_pages(self, input_file, output_directory):
        pdf_reader = PdfReader(input_file)
        for page_num in range(pdf_reader.getNumPages()):
            pdf_writer = PdfWriter()
            pdf_writer.addPage(pdf_reader.getPage(page_num))
            output_filename = os.path.join(output_directory, f"page_{page_num + 1}.pdf")
            with open(output_filename, 'wb') as output_pdf:
                pdf_writer.write(output_pdf)

    def remove_password_security(self, input_file, output_file, password=None):
        pdf_reader = PdfReader(input_file)
        pdf_writer = PdfWriter()
        if password:
            pdf_reader.decrypt(password)
        for page_num in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page_num))
        with open(output_file, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

    def extract_text(self, input_file, output_txt_file):
        pdf_reader = PdfReader(input_file)
        text = ''
        for page_num in range(pdf_reader.getNumPages()):
            text += pdf_reader.getPage(page_num).extractText()
        with open(output_txt_file, 'w', encoding='utf-8') as txt_file:
            txt_file.write(text)

    def convert_images_to_pdf(self, image_files, output_pdf_file):
        images = []
        for image_file in image_files:
            img = Image.open(image_file)
            images.append(img)

        images[0].save(output_pdf_file, save_all=True, append_images=images[1:])

if __name__ == "__main__":
    pdf_processor = PdfProcessor()

    # Example usage:
    pdf_processor.combine_pdfs(["a1.pdf", "a2.pdf"], "a1a2.pdf")
    pdf_processor.separate_pdf_pages("ipt.pdf", "output_pages")
    pdf_processor.remove_password_security("secu.pdf", "safe.pdf", password="pwd")
    pdf_processor.extract_text("input.pdf", "output.txt")
    pdf_processor.convert_images_to_pdf(["a.jpg", "b.png"], "op.pdf")
