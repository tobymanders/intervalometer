
from sh import gphoto2 as gp
from time import sleep
import sys

def captureImages(interval):
	while True:
		gp(["--trigger-capture"])
		sleep(interval)

if __name__=="__main__":
	interval = int(sys.argv[1])
	captureImages(interval)
