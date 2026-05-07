import keyboard

keyboard.press("end")
keyboard.write("#Szia!", delay=1)


while True:
    billentyű = keyboard.read_key()
    if billentyű:
        print(f"{billentyű}")
        if billentyű == "esc":
           break