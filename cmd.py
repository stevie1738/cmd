import os
def loop():
    c = input("\n> ")
    os.system(c)
    loop()
loop()