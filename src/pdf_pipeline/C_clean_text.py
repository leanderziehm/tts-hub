import re


def clean_text(text: str) -> str:
    # Replace newlines with spaces
    text = text.replace("\n", " ").replace("\r", " ")
    # Replace non-ASCII characters with spaces
    text = re.sub(r"[^\x00-\x7F]+", " ", text)
    # Collapse multiple whitespace into a single space
    text = re.sub(r"\s+", " ", text)
    # Trim leading/trailing spaces
    text = text.strip()

    # TODO: code for removeing references 
    # TODO: code for removing lines with just 0.001 
    # TODO: delete tables: TABLE II and then if there is 3 lines in a row that have more then 3 words then table is over.

    return text


if __name__ == "__main__":
    input_file_path = "output/1571170655_cleanmanual.txt"
    output_file_path = "output/1571170655_cleanmanual_clean.txt"
    with open(input_file_path, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()
    cleaned_text = clean_text(text)
    with open(output_file_path, "w", encoding="utf-8") as f:
        f.write(cleaned_text)
    print(f"Cleaned text written to {output_file_path}")

