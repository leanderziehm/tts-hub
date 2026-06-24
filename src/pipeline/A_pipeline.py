import src.pipeline.B_pdf_text_extraction as pdf_text_extraction
import os


def run():
    print("run")
    pdf_extraction()


def pdf_extraction():
    base_path_in = "input"
    file_in_pdf = "1571170655.pdf"
    base_path_out = "output"
    file_out_txt = "1571170655.txt"
    full_path_in_pdf = os.path.join(base_path_in, file_in_pdf)
    full_path_out_txt = os.path.join(base_path_out, file_out_txt)
    extracted_text = pdf_text_extraction.extract_text_from_pdf(full_path_in_pdf)
    with open(full_path_out_txt, "w") as f:
        f.write(extracted_text)
