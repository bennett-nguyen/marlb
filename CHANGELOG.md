# CHANGELOG
- (2022/01/02): Compress the compact version to 31 lines
- (2021/12/30): Added missing condition in `./src/command.py` -> `line 13`

- (2021/12/29): Compacted version of this interpreter is now available, the file weighs in at 2542 bytes and 44 lines long

- (2021/12/29): Fixed grammar mistake in `./src/command.py` -> `line 6`

- (2021/12/27): Used regex to match any character that this interpreter doesn't recognize (to remove it). 

- (2021/12/23): Added `utf-8` encoding support. Reordered some part of the code.

- (2021/12/20): Introduced [VS Code language support](https://github.com/bennett-nguyen/marlb-syntax/tree/master) for this language

- (2021/12/16): Added `debug` option: use this option to see more verbose logging information about the execution of the program, usage: `python marlb.py -m debug -f path/to/file`

- (2021/12/16): Added a feature to pre-process raw code (code taken from the script file) to remove any newline characters, whitespace's, and comments
