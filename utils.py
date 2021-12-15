import winsound
import command

info = {
    "duration": 200,
    "pitch_level": 2
}

A = 440
Asharp = 466
B = 494
C = 262
Csharp = 277
D = 294
Dsharp = 311
E = 330
F = 349
Fsharp = 370
G = 392
Gsharp = 415

C_higher = 524

note_keys = {
    "q": C,  # Q
    "a": Csharp,  # A

    "w": D,  # W
    "s": Dsharp,  # S

    "e": E,  # E

    "r": F,  # R
    "d": Fsharp,  # D

    "u": G,  # U
    "j": Gsharp,  # J

    "i": A,  # I
    "k": Asharp,  # K

    "o": B,  # O

    "p": C_higher  # P
}

functional_commands = {
    "!": command.stop_exec,
    "-": command.decrease_pitch,
    "+": command.increase_pitch,
    "<": command.decrease_duration,
    ">": command.increase_duration,
    ":": command.reset

}

def interpret(code):
    for line in code:
        for char in line:
            if char in note_keys:
                winsound.Beep(note_keys[char] * info['pitch_level'], info["duration"])
            
            elif char in functional_commands:
                functional_commands[char](info)