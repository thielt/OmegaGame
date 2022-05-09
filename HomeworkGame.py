from sys import exit

import sys
from time import sleep
def Sythr_Room():
	print("You decided to venture left...there seems to be a draft coming from it.")
	sleep(2.0)
	print("You feel cold and a bit tired...what's going on?")
	sleep(2.0)
	print("Sythr: It has been a while since I've had a soul...what a treat. Welcome to your demise.")
	sleep(2.0)
	print("Sythr launches a ball of dark energy towards you. What do you do?")
	sleep(1.0)

	def Sythr_Room_Action():
		Sythr_HP = 100
		Player_HP = 100
		while Player_HP > 0:
			while Sythr_HP > 0:
				choice = input("""Dodge or Attack?> """)
				if choice == "Dodge":
					sleep(0.5)
					print("The ball of dark scrapes you, taking a bit of your health")
					Player_HP = Player_HP - 20

					print(f"My Health is {Player_HP}")
					print(f"Sythr's Health is {Sythr_HP}")
				elif choice == "Attack":
					sleep(0.5)
					print("The energy narrowly misses you as you slash Sythr with your knife")
					Sythr_HP = Sythr_HP - 50

					print(f"My Health is {Player_HP}")
					print(f"Sythr's Health is {Sythr_HP}")

				if Player_HP <= 0:
					dead("Sythr takes your soul")
				if Sythr_HP <= 0:
					Win("You slay Sythr")
	Sythr_Room_Action()


def dead(why):
	print(why, "You died, try again")
	exit(0)
def Win(why):
	print(why, "Great Job!")
	exit(0)


def start():
	print("Please enter in your name")
	Player_name = input(">")
	print(f"""Hello {Player_name}. Welcome to George's Game, we shall start at the entrance of a cave.
You see a fork in the road, which way do you choose?""")

	def path():
		Choice = input(" Type left or right (Hint: Don't choose left) > ")
		Choice = Choice.casefold()	#aggressive lower case input string conversion, less aggressive: lower()

		if Choice == "left":
				dead("Curiosity killed the Cat")
		elif Choice == "right":
			Sythr_Room()
	path()
start()
