import time
import sys
import os

while True:
    if os.path.exists("fruits.txt"):
        with open ("fruits.txt") as file:
            print (file.read())
    else:
        print("file does not exist") 
    time.sleep(25)


