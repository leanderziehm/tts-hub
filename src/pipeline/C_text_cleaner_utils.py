import re


def run(input_file_path: str, output_file_path: str):
    with open(input_file_path, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()

    # Replace newlines with spaces
    text = text.replace("\n", " ").replace("\r", " ")

    # Replace non-ASCII characters with spaces
    text = re.sub(r"[^\x00-\x7F]+", " ", text)

    # Collapse multiple whitespace into a single space
    text = re.sub(r"\s+", " ", text)

    # Trim leading/trailing spaces
    text = text.strip()

    with open(output_file_path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"Cleaned text written to {output_file_path}")


if __name__ == "__main__":
    input_file_path = "out/mlwl.txt"
    output_file_path = "out/mlwl_clean.txt"
    run(input_file_path, output_file_path)
