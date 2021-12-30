from time import sleep

# !
def stop_exec(*args, **kwargs):
    if kwargs["mode"] == "debug":
        print("Slept for 0.5 seconds")
    
    sleep(0.5)


# -
def decrease_pitch(info, mode):
    if not info["pitch_level"] - 1 and mode == 'debug':
        print(f"Lowest level of pitch reached: {info['pitch_level']}")
        return

    info["pitch_level"] = info["pitch_level"] - 1
    
    if mode == "debug":
        print(f"Decreased pitch to level: {info['pitch_level']}")

# + 
def increase_pitch(info, mode):
    if info["pitch_level"] + 1 == 17 and mode == "debug":
        print(f"Reached highest pitch possible: {info['pitch_level']}")
        return

    info["pitch_level"] = info["pitch_level"] + 1

    if mode == "debug":
        print(f"Increased pitch to level: {info['pitch_level']}")

# <
def decrease_duration(info, mode):
    if info["duration"] - 100 < 0 and mode == "debug":
        print(f"Reached lowest duration possible: {info['duration']}ms")
        return

    info["duration"] = info["duration"] - 100
    
    if mode == "debug":
        print(f"Decreased duration to: {info['duration']}ms")

# >
def increase_duration(info, mode):
    if info["duration"] + 100 > 15000 and mode == "debug":
        print(f"Reached highest duration possible: {info['duration']}ms")
        return

    info["duration"] = info["duration"] + 100
    
    if mode == "debug":
        print(f"Increased duration to: {info['duration']}ms")

# :
def reset(info, mode):
    info["duration"] = 200
    info["pitch_level"] = 2
    
    if mode == "debug":
        print("Set duration and pitch level to default")
