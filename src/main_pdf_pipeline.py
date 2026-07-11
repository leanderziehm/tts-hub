import pdf_pipeline.pdf_pipeline as pdf_pipeline
import os

def main():

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

    pdf_pipeline.run(full_path_input_pdf,full_path_extracted_txt)


if __name__ == "__main__":
    main()
