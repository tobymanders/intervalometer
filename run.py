
from sh import gphoto2 as gp
import sleep

def captureImages():
	gp(["--trigger-capture"])
	sleep(3)

captureImages()