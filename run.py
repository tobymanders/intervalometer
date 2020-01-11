
from sh import gphoto2 as gp
from time import sleep

def captureImages():
	gp(["--trigger-capture"])
	sleep(3)

captureImages()