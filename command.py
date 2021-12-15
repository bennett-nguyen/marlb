from time import sleep

# !
def stop_exec(*args):
    sleep(0.5)


# -
def decrease_pitch(info):
    if not info["pitch_level"] - 1:
        print(f"Lowest level of pitch reached: {info['pitch_level']}")
        return

    info["pitch_level"] = info["pitch_level"] - 1

    print(f"Decreased pitch to level: {info['pitch_level']}")

# + 
def increase_pitch(info):
    if info["pitch_level"] + 1 == 17:
        print(f"Reached highest pitch possible: {info['pitch_level']}")
        return

    info["pitch_level"] = info["pitch_level"] + 1

    print(f"Increased pitch to level: {info['pitch_level']}")

# <
def decrease_duration(info):
    if info["duration"] - 100 < 0:
        print(f"Reached lowest duration possible: {info['duration']}ms")
        return

    info["duration"] = info["duration"] - 100

    print(f"Decreased duration to: {info['duration']}ms")

# >
def increase_duration(info):
    if info["duration"] + 100 > 15000:
        print(f"Reached highest duration possible: {info['duration']}ms")
        return

    info["duration"] = info["duration"] + 100
    print(f"Increased duration to: {info['duration']}ms")

def reset(info):
    info["duration"] = 200
    info["pitch_level"] = 2
    print("Set duration and pitch level to default")
