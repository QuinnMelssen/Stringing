from pyclick import HumanClicker
import pyautogui, random, PIL.ImageGrab, time
hc = HumanClicker()



#Check For Level Up
def checkLevelUp():
	if PIL.ImageGrab.grab().load()[(471, 984)] == (182, 168, 138):
		time.sleep(2)
		#click on bow
		time.sleep(random.triangular(.3, .5, .4))
		hc.move((int(random.triangular(1773, 1784)), int(random.triangular(920, 902))), random.triangular(.0001, .5, .2))
		time.sleep(random.triangular(.3, .5, .4))
	
		pyautogui.mouseDown();
		time.sleep(random.triangular(.004, .024, .010))
		pyautogui.mouseUp();

		#click on last string
		time.sleep(random.triangular(.2, .5, .2))
		hc.move((int(random.triangular(1856, 1866)), int(random.triangular(1025, 1016))), random.triangular(.0001, .5, .2))
		time.sleep(random.triangular(.5, 1, .5))
 
		pyautogui.mouseDown();
		time.sleep(random.triangular(.004, .024, .010))
		pyautogui.mouseUp();

		time.sleep(random.triangular(.8, 1, .8))
		pyautogui.keyDown(' ')
		time.sleep(random.triangular(.004, .024, .010))
		pyautogui.keyUp(' ')

		time.sleep(random.triangular(.2, .5, .2))
		hc.move((int(random.triangular(-174, -43)), int(random.triangular(23, 35))), random.triangular(.0001, .5, .2))
		time.sleep(random.triangular(.5, 1, .5))

def startStringing():
	#click on bow
	time.sleep(random.triangular(.3, .5, .4))
	hc.move((int(random.triangular(1726, 1742)), int(random.triangular(816, 793))), random.triangular(.0001, .5, .2))
	time.sleep(random.triangular(.3, .5, .4))
	
	pyautogui.mouseDown();
	time.sleep(random.triangular(.004, .024, .010))
	pyautogui.mouseUp();

	

	#click on string
	time.sleep(random.triangular(.3, .5, .4))
	hc.move((int(random.triangular(1809, 1828)), int(random.triangular(924, 903))), random.triangular(.0001, .5, .2))
	time.sleep(random.triangular(.3, .7, .4))

	pyautogui.mouseDown();
	time.sleep(random.triangular(.004, .024, .010))
	pyautogui.mouseUp();


	#Wait for menu
	time.sleep(random.triangular(1, 1.5, 1.2))

	

	#Fletch LongBow
	pyautogui.keyDown(' ')
	time.sleep(random.triangular(.04, .024, .05))
	pyautogui.keyUp(' ')

	#Wait for stringing
	while PIL.ImageGrab.grab().load()[1869, 1030] == (117, 105, 74):
		checkLevelUp()
		continue



	#Open Bank
	time.sleep(random.triangular(.3, .4, .4))
	hc.move((int(random.triangular(1162, 1252)), int(random.triangular(700, 583))), random.triangular(.0001, .5, .2))
	time.sleep(random.triangular(.2, .5, .3))
	pyautogui.mouseDown();
	time.sleep(random.triangular(.004, .024, .010))
	pyautogui.mouseUp();

	

	#Deposit Strung Bows
	time.sleep(random.triangular(.2, .5, .2))
	hc.move((int(random.triangular(1787, 1767)), int(random.triangular(794, 813))), random.triangular(.0001, .5, .2))
	time.sleep(random.triangular(.3, .5, .3))

	pyautogui.mouseDown();
	time.sleep(random.triangular(.004, .024, .010))
	pyautogui.mouseUp();


	#Retrieve Bows
	time.sleep(random.triangular(.2, .5, .2))
	hc.move((int(random.triangular(654, 668)), int(random.triangular(167, 158))), random.triangular(.0001, .5, .2))
	time.sleep(random.triangular(.5, .6, .5))

	pyautogui.mouseDown();
	time.sleep(random.triangular(.004, .024, .010))
	pyautogui.mouseUp();


	#Retrieve Strings
	time.sleep(random.triangular(.2, .5, .2))
	hc.move((int(random.triangular(701, 718)), int(random.triangular(169, 157))), random.triangular(.0001, .5, .2))
	time.sleep(random.triangular(.5, .6, .5))

	pyautogui.mouseDown();
	time.sleep(random.triangular(.004, .024, .010))
	pyautogui.mouseUp();


	#Close Bank
	time.sleep(random.triangular(.2, .4, .3))
	hc.move((int(random.triangular(1057, 1066)), int(random.triangular(91, 84))), random.triangular(.0001, .5, .2))
	time.sleep(random.triangular(.5, .7, .5))

	pyautogui.mouseDown();
	time.sleep(random.triangular(.004, .024, .010))
	pyautogui.mouseUp();




startStringing()
while True:
	startStringing()
