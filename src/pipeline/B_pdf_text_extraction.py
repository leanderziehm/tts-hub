# pdf_text_extractor.py

import pymupdf
import os

def extract_text_from_pdf(pdf_path: str) -> str:
    print("extract_text_from_pdf")
    text = []

    with pymupdf.open(pdf_path) as doc:
        for page in doc:
            text.append(page.get_text())

    return "\n".join(text)


if __name__ == "__main__":
    base_path_in = "input"
    file_in_pdf = "1571170655.pdf"
    base_path_out = "output"
    file_out_txt = "1571170655.txt"

    full_path_in_pdf = os.path.join(base_path_in,file_in_pdf)
    full_path_out_txt = os.path.join(base_path_out,file_out_txt)


    extracted_text = extract_text_from_pdf(full_path_in_pdf)

    # print(extracted_text)

    with open(full_path_out_txt,"w") as f:
        f.write(extracted_text)