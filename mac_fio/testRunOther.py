import time
import os
import threading

print("I'm start")

def runCMD(command):
    os.system(command)
    
t = threading.Thread(target = runCMD, args = {'python testRunOther.py'})

t.start()

time.sleep(1)
print("I'm stop")