import os
def d():
    print("[Enter the file with directory to be deleted]")
    c = input("\n> ")
    os.remove(c)
    d()
d()