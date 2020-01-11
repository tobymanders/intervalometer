from time import sleep
from datetime import datetime
from sh import gphoto2 as gp
import signal, os, subprocess

shot_date = datetime.now().strftime("%Y-%m-%d")
shot_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
picID = "PiShots"

clearCommand = ["--folder", "/store_00010001/DCIM/100CANON", \
				"-R", "--delete-all-files"]
triggerCommand = ["--trigger-capture"]
downloadCommand = ["--get-all-files"]

folder_name = shot_date + picID
save_location = "/home/pi/timelapse/images/" + folder_name

def createSaveFolder():
	try:
		os.makedirs(save_location)
	except:
		print("Failed to create the new directory.")
	os.chdir(save_location)

def captureImages():
	gp(triggerCommand)
	sleep(3)
	
def renameFiles(ID):
	for filename in os.listdir("."):
		if len(filename) < 13:
			if filename.endswith(".JPG"):
				os.rename(filename, (shot_time + ID + ".JPG"))
				print("Renamed the JPG")
			elif filename.endswith(".CR2"):
				os.rename(filename, (shot_time + ID + ".CR2"))
				print("Renamed the CR2")

captureImages()