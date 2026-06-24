import src.pipeline.B_pdf_text_extraction as pdf_text_extraction
import src.pipeline.C_clean_text as clean_text
import os


def run():
    print("run")
    file_in_pdf = "1571170655.pdf"

    filename = file_in_pdf.split(".")[0]


    print(filename)

    base_path_in = "input"
    base_path_out = "output"
    file_out_txt = f"{filename}_raw.txt"

    full_path_input_pdf = os.path.join(base_path_in, file_in_pdf)
    full_path_extracted_txt = os.path.join(base_path_out, file_out_txt)

    # extract_text_from_pdf

    extracted_text = pdf_text_extraction.extract_text_from_pdf(full_path_input_pdf)
    with open(full_path_extracted_txt, "w") as f:
        f.write(extracted_text)

    # clean_text

    input(f"please clean the file: {full_path_extracted_txt}")

    file_out_clean_txt = f"{filename}_clean.txt"
    file_out_clean_path = os.path.join(base_path_out,file_out_clean_txt)
  
    with open(full_path_extracted_txt, "r", encoding="utf-8", errors="ignore") as f:
        human_cleaned_text = f.read()

    cleaned_text = clean_text.clean_text(human_cleaned_text)
    with open(file_out_clean_path, "w", encoding="utf-8") as f:
        f.write(cleaned_text)
    print(f"Cleaned text written to {file_out_clean_path}")



if __name__ == "__main__":
    run()




 

