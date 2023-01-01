import time
from playsound import playsound

cumle = input("Write something »» ")
result = ""

class Morse():
    def __init__(self, cumle, result):
        self.cumle = cumle.lower()
        self.result = result
        
    def morse(self):
        morse_dict = {
            "a": ".-", "b": "-...", "c": "-.-.",
            "d": "-..", "e": ".", "f": "..-.",
            "g": "--.", "h": "....", "i": "..",
            "j": ".---", "k": "-.-", "l": ".-..",
            "m": "--", "n": "-.", "o": "---",
            "p": ".--.", "q": "--.-", "r": ".-.",
            "s": "...", "t": "-", "u": "..-",
            "v": "...-", "w": ".--", "x": "-..-",
            "y": "-.--", "z": "--..",
        }

        time.sleep(2)

        for i in self.cumle:

            try:
                for a in morse_dict[i]:
                    if a == ".":
                        playsound("short_bip.mp3")
                        
                    elif a == "-":
                        playsound("long_bip.mp3")
                    
                    self.result+=a
                    time.sleep(0.1)

            except: 
                time.sleep(1)
                self.result+=" "    

        print("Morse Result: ", self.result)


Morse(cumle, result).morse()
