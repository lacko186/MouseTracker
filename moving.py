from tkinter import *
import random

hópelyhekszáma = 1000
gyorsaság = 2


def main(hópelyhekszáma=hópelyhekszáma, gyorsaság=gyorsaság):
    root = Tk()
    root.title("Hóesés")
    root.geometry("600x650")

    canvas = Canvas(root, width=600, height=550)
    canvas.pack()

    canvas.config(bg="black")

    snowflakes = []
    for _ in range(hópelyhekszáma):
        x = random.randint(0, 600)
        y = random.randint(0, 550)
        size = random.randint(2, 6)
        flake = canvas.create_oval(x, y, x + size, y + size, fill="white", outline="")
        speed = random.uniform(1, gyorsaság)
        drift = random.uniform(-1, 1)
        snowflakes.append([flake, speed, drift])

    def animate():
        for flake_data in snowflakes:
            flake, speed, drift = flake_data
            canvas.move(flake, drift, speed)

        root.after(30, animate) 

    animate()
    root.mainloop()


if __name__ == "__main__":
    main()