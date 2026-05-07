import mouse
import time

timer = time.time() + 30
visszaszamlalo = timer - time.time()

print("Keresd meg Sanyit🐀")

while True:
    visszaszamlalo = timer - time.time()

    jelenlegi_pozicio = mouse.get_position()
    print(f"Jelenlegi pozíció: {jelenlegi_pozicio}")
    time.sleep(1)
    print(f"Visszaszámláló: {int(visszaszamlalo)} másodperc")


    if jelenlegi_pozicio == (100, 100):
        print("Megtaláltad Sanyit 🐀")
        break
    
    if visszaszamlalo <= 0:
        print("Sanyi elmenekült")
        break
    
    
    

