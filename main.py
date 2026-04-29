from pov_generator.local_pov_generator import (
    read_raw_text_from_file,
    write_pov_to_file,
    generate_pov_from_text,
)

import os

def main():
    raw_dir = r"C:\Users\deyro\Desktop\Projects\slop-ai\raw"
    pov_dir = r"C:\Users\deyro\Desktop\Projects\slop-ai\pov"
    
    for filename in os.listdir(raw_dir):
        if filename.endswith('.txt'):
            raw_filepath = os.path.join(raw_dir, filename)
            pov_filepath = os.path.join(pov_dir, filename.replace('.txt', '_pov.txt'))
            
            text:str = read_raw_text_from_file(raw_filepath)
            if text:
                pov = generate_pov_from_text(text)
                if pov:
                    write_pov_to_file(pov_filepath, pov)
                    print(f"Generated POV for {filename} and saved to {pov_filepath}")
                else:
                    print(f"Failed to generate POV for {filename}")
if __name__ == "__main__":
    main()
