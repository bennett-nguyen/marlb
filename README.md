# marlb
A minimal esoteric programming language for making simple melodies. The name is suggested by my friend LOL!

# Getting Started
```
Requirements:
Python version: 3.10
Platform: Windows 10
```
`git clone https://github.com/bennett-nguyen/marlb.git`
<br>
<br>
File extension: `*.marble`
<br>
<br>
Interpret a file to sounds using the command:
<br>
`python marlb.py -m interpret -f path/to/file`
<br>
<br>
I wrote some script files and stored it in `./test`, run whatever script you want
<br>

# Syntax
**Comment**: notated by `"`, any code that stands after `"` will be ignored (although any character that this interpreter doesn't recognize will be considered as a comment as well, using a comment notation is still a best practice)
<br><br>
**Playing notes**:
Any character in the list below will play a specific note
<br>
`q`: C
<br>
`a`: C#
<br>
<br>
`w`: D
<br>
`s`: D#
<br>
<br>
`e`: E
<br>
<br>
`r`: F
<br>
`d`: F#
<br>
<br>
`u`: G
<br>
`j`: G#
<br>
<br>
`i`: A
<br>
`k`: A#
<br>
<br>
`o`: B
<br>
<br>
`p`: C (higher pitch)

**Functional commands**:
Any character in the list below will do a certain task to affect how notes are played
<br>
```
default:
  pitch_level: 2
  duration: 200ms
```
`+`: Increase pitch level by `1` (meaning the pitch of the note will get higher, max level: `16`)
<br>
`-`: Decrease pitch level by `1` (meaning the pitch of the note will get lower, min level: `1`)
<br>
`>`: Increase duration by `100ms` (meaning the length of playing a note will increase, max duration: `15s`)
<br>
`<`: Decrease duration by `100ms` (meaning the length of playing a note will decrease, min duration: `0ms`)
<br>
`!`: Stop the execution for `0.5` seconds
<br>
`:`: Reset `duration` and `pitch_level` to `default` (i.e `pitch_level: 2`, `duration: 200ms`)
# Update
See [CHANGELOG.md](./CHANGELOG.md)


# Tutorial
Today I'll instruct you to write happy birthday song in marlb for someone important to you :D
<br>
I'll assume that you have cloned this repository and got the interpreter so let's get started.
<br>
<br>
First, create a file that ends with `.marble` (in any directory you want). Open that file with your prefered text editor.
<br>
Then, get the music sheet of this song so you can convert each note in that song to marlb code<br>
<br>
I have a music sheet down here so you don't have to waste your time doing it.
<br>
![image](https://user-images.githubusercontent.com/83117848/146189003-d1b1dac5-d673-43ff-a517-13e5975f21ee.png)

Convert each note to marlb [command](https://github.com/bennett-nguyen/marlb#syntax) (e.g D will be converted to `w`, E will be converted to `e`, etc.), you can seperate each line of lyric and space out each command for readability.
<br>
<br>
![image](https://user-images.githubusercontent.com/83117848/146194381-b44b5e80-d544-4b97-99f6-5cd48bc3c037.png)
<br>
You'll also notice that the 3rd D note on the 3rd line is higher than other D's; to deal with that, increase the pitch level by 2 for that note then decrease it after that like this:
<br>
![image](https://user-images.githubusercontent.com/83117848/146194988-243c9a19-5add-41bb-ba16-bd0c54bfb2da.png)
<br>
But there's no break between each line so when you play it, you'll hear notes being played continuously; to prevent that, add a `!` at the end of each line so the program will sleep `0.5` seconds before executing the next line.
<br>
![image](https://user-images.githubusercontent.com/83117848/146197160-855f5577-ef45-4f87-ae49-e38678258c23.png)
<br>
Now save your file and copy the path that leads to your file as text and open `powershell` (or `command prompt`), then `cd` into the directory that the cloned repository is located. Interpret your text file using this command:
<br>
`python marlb.py -m interpret -f paste/the/path/here`
<br>
<br>
In my case, both the interpreter and my source file are in `D:\work_dir_3` (i.e same directory) so my command would be like:
<br>
```
>>> D:\
>>> cd work_dir_3
>>> python marlb.py -m interpret -f ./happy_birthday.marble
```
(If your file name has a whitespace character then put it in quotes when you're about to interpret it e.g `python marlb.py -m interpret -f "path/to/file"`)
<br>
(You can use an absolute path or relative path that leads to your file as well)
<br>
<br>
Press enter and enjoy your music :]
