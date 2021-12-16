import argparse
import os
from utils import interpret

parser = argparse.ArgumentParser()

parser.add_argument("-m", "--mode", choices=["interpret", "debug"], required=True, help="Mode to interpret your file")
parser.add_argument("-f", "--file", required=True, help="File to interpret, pass in either file name (in the current working directory) or a file path")

args = parser.parse_args()

def path_parser():
    path = args.file.split("\\") if "\\" in args.file else args.file.split("/")
    file_name = path[-1]

    invalid_characters = ['"', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')' ',', '+', '{', '}', '\\', '"', '|', '<', '>', '?', '`', '=', '[', ']', ';' "'", '\\', '/']
    
    for entry in path:
        if any(char in entry for char in invalid_characters):
            print(f"error: invalid syntax '{args.file}'")
            return
    
    if len(path) != 1:
        for entry in path[:-1]:
            try:
                os.chdir(entry)
            except FileNotFoundError:
                print(f"error: directory '{entry}' doesn't exist in {os.getcwd()}")
                return
    
    try:
        if not file_name.endswith(".marble"):
            print(f"error: invalid file extension '{file_name[file_name.index('.'):]}'\nvalid extension: '*.marble'")
            return

        with open(f"./{file_name}", "r") as f:
            raw_code = f.readlines()
            pre_processed_code = []
            
            for line_number, content in enumerate(raw_code, start=1):
                try:
                    content = "".join(content[:content.index('"')].split())
                    
                    if not content:
                        continue

                    pre_processed_code.append((line_number, content))

                except ValueError:
                    if len(content) == 1 and "\n" in content:
                        continue

                    content = "".join(content.split())
                    
                    if "\n" in content:
                        content = content[:-1]
                    
                    pre_processed_code.append((line_number, content))
                
            interpret(pre_processed_code, args.mode)

    except FileNotFoundError:
        print(f"error: file '{file_name}' not found in {os.getcwd()}")
        return

if __name__ == "__main__":
    path_parser()

