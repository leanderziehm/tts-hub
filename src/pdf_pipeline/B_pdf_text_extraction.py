import pymupdf
import argparse
import os

def extract_text_from_pdf(pdf_path: str) -> str:
    print("extract_text_from_pdf")
    text = []

    with pymupdf.open(pdf_path) as doc:
        for page in doc:
            text.append(page.get_text())

    return "\n".join(text)


def default_usage():
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


def main():
    parser = argparse.ArgumentParser(
        description="Extract text from a PDF file and save it as a TXT file."
    )

    parser.add_argument(
        "input_pdf",
        help="Path to the input PDF file"
    )

    parser.add_argument(
        "-o",
        "--output",
        help="Path to the output TXT file. Defaults to input filename with .txt extension."
    )

    args = parser.parse_args()

    input_pdf = args.input_pdf

    if not os.path.exists(input_pdf):
        parser.error(f"Input file does not exist: {input_pdf}")

    if args.output:
        output_txt = args.output
    else:
        output_txt = os.path.splitext(input_pdf)[0] + ".txt"

    output_dir = os.path.dirname(output_txt)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    extracted_text = extract_text_from_pdf(input_pdf)

    with open(output_txt, "w", encoding="utf-8") as f:
        f.write(extracted_text)

    print(f"Extracted text written to: {output_txt}")


if __name__ == "__main__":
    main()