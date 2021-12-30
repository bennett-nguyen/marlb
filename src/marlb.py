import argparse
import os
import re
from utils import interpret

parser = argparse.ArgumentParser()

parser.add_argument("-m", "--mode", choices=["interpret", "debug"], required=True, help="Mode to interpret your file")
parser.add_argument("-f", "--file", required=True, help="File to interpret, pass in either file name (in the current working directory) or a file path")

args = parser.parse_args()

def processor(file_name):
    if not file_name:
        return

    try:
        if not file_name.endswith(".marble"):
            print(f"error: invalid file extension '{file_name[file_name.index('.'):]}'\nvalid extension: '*.marble'")
            return

        with open(f"./{file_name}", "r", encoding="utf8") as f:
            raw_code = f.readlines()
            pre_processed_code = []
            
            for line_number, content in enumerate(raw_code, start=1):
                content = re.sub("[^qweruiopasdjk!:<>\+-]", "", re.match("^[^\"]*", content).group())
                
                if len(content) == 1 and "\n" in content or not content:
                    continue
                
                pre_processed_code.append((line_number, content))
                
            interpret(pre_processed_code, args.mode)

    except FileNotFoundError:
        print(f"error: file '{file_name}' not found in {os.getcwd()}")
        return
    except ValueError:
        print(f"error: '{file_name}' is not recognized as a file")
        return
    except KeyboardInterrupt:
        print("error: proccess has been interrupted")
        return




def path_parser():
    path = args.file.split("\\") if "\\" in args.file else args.file.split("/")
    
    if not path[-1]:
        path.pop()

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
            except OSError:
                print(f"error: invalid syntax '{args.file}'")
                return

    return file_name
    



if __name__ == "__main__":
    processor(path_parser())
