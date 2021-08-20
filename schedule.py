import time
import subprocess

seconds_to_wait = 3600

while(True):
  subprocess.call(['sh', './sync.sh'])
  time.sleep(seconds_to_wait)
