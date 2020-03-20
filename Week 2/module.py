import os

def listdir(path):
    files = []
    for f in os.walk(path):
        for file in f:
            files.append(file)

    f2w = open("files.txt", "w")

    for f in files:
        for f2 in f:
            f2w.write(f2)
    
    f2w.close()
