import random


gestures = ["Rock", "Paper", "Scissors"]

def rounds():
	n_rounds = int(input("How many maximum rounds?"))
	if n_rounds%2 == 0:
	n_rounds = n_rounds+1
return n_rounds
	print ("number of rounds:", n_rounds)

if n_rounds%2 == 0:
	n_rounds = n_rounds+1

n_rounds

def rounds_to_win():
	rounds_to_win = int((n_rounds+1)/2)
	return rounds_to_win
	print ("You need to win", rounds_to_win, "to win")



cpu_score=0
player_score=0

def cpu_gesture():
	return random.choice(gestures)

def player_choice():
	player_gesture =""
	while player_gesture not in gestures:
		player_gesture = input("Choose a gesture between Rock, Paper or Scissors:")
	return player_gesture

#player_gesture = "Rock"
#cpu_gesture = "Paper"

def Roundwin(player_gesture, cpu_gesture):
	if (player_gesture == cpu_gesture):
		return 0
	elif (player_gesture == "Scissors" and cpu_gesture == "Paper"):
		return 2
	elif (player_gesture == "Scissors" and cpu_gesture == "Rock"):
		return 1
	elif (player_gesture == "Rock" and cpu_gesture == "Paper"):
		return 1
	elif (player_gesture == "Rock" and cpu_gesture == "Scissors"):
		return 2
	elif (player_gesture == "Paper" and cpu_gesture == "Scissors"):
		return 1
	elif (player_gesture == "Paper" and cpu_gesture == "Rock"):
		return 2

def winner(player_gesture, cpu_gesture):
	print ("The player chose:", player_gesture)
	print ("The CPU chose:", cpu_gesture)
	if Roundwin(player_choice, cpu_gesture) == 1:
		print ("The CPU won!")
		global player_score
		player_score +=1
	elif Roundwin(player_choice, cpu_gesture) == 2:
		print ("The player won!")
		global cpu_score
		cpu_score +=1
	elif Roundwin(player_choice, cpu_gesture) == 0:
		print ("It's a tie!")

rounds()
rounds_to_win()
cpu_gesture()
player_choice()
Roundwin(player_gesture, cpu_gesture)
winner(player_gesture, cpu_gesture)


