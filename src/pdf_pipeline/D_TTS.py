import subprocess

def synthesize(text: str,out_file):
        subprocess.run(
            ["espeak-ng", text, "--stdout"],
            # ["espeak", text, "--stdout"],
            check=True,
            stdout=open(out_file, "wb")
        )


if __name__ == "__main__":
    input_file_path =  "output/1571170655_cleanmanual_clean.txt"
    output_path = "output/1571170655.wav" 
    with open(input_file_path, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()
    synthesize(text,output_path)


#  sudo apt update && sudo apt install espeak-ng libespeak1