# marlb
A minimal estorical programming language for making simple melodies. The name is suggested by my friend LOL!

# Getting Started
```
Requirements:
Python version: 3.10
Platform: Windows 10
```
`git clone https://github.com/bennett-nguyen/marlb.git`
<br>
<br>
Interpret a file to sounds using the command:
<br>
`python random_proj.py -m interpret -f path/to/file`
<br>
In this case, it's `hello_world.txt` so do:
<br>
`python random_proj.py -m interpret -f hello_world.txt`

# Syntax
**Comment**: notated using `"`, any code that stands after `"` will be ignored (although any character that this program doesn't recognize will be considered as a comment as well, using a comment notation is still a best practice)
<br><br>
**Playing notes**:
Any character in the list below will play a specific note
<br>
`q`: C
<br>
`a`: C#
<br>
`w`: D
<br>
`s`: D#
<br>
`e`: E
<br>
`r`: F
<br>
`d`: F#
<br>
`u`: G
<br>
`j`: G#
<br>
`i`: A
<br>
`k`: A#
<br>
`o`: B
<br>
`p`: C (higher pitch)

**Functional commands**:
Any character in the list below will do a certain task to affect how notes are played
<br>
`+`: Increase pitch level (meaning the pitch of the note will get higher)
<br>
`-`: Decrease pitch level (meaning the pitch of the note will get lower)
<br>
`>`: Increase duration (meaning the length of playing a note will increased)
<br>
`<`: Decrease duration (meaning the length of playing a note will decrease)
<br>
`!`: Stop the execution for 0.5 seconds
<br>
`:`: Reset duration to `300ms` and pitch level to `2` 
