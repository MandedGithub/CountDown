import time
import pyttsx3

friend = pyttsx3.init()

seconds = int(input("How many seconds?"))
for i in range(seconds):
    print(str(seconds - i) + " seconds remain") 
    time.sleep(1)

friend.say("Times UP")
print("Times UP!")