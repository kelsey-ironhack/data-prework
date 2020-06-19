import random

gestures = ["Rock", "Paper", "Scissors"]

random.choice(gestures)

n_rounds == 0
rounds_to_win ==0
cpu_score==0
player_score==0

def function(x):
	for x in gestures:
		print x
		if raw_input("Choose a gesture between Rock, Paper or Scissors:") not in gestures:
			raw_input("Choose a gesture between Rock, Paper or Scissors:")
		elif raw_input("Choose a gesture between Rock, Paper or Scissors:") in gestures:
			print ("OK")

for x in gestures:
	if raw_input("Choose a gesture between Rock, Paper or Scissors:") not in gestures:
		raw_input("Choose a gesture between Rock, Paper or Scissors:")
	elif raw_input("Choose a gesture between Rock, Paper or Scissors:") in gestures:
		print ("OK")

x = raw_input("Choose a gesture between Rock, Paper or Scissors:")

if x not in gestures:
	x = input("Choose a gesture between Rock, Paper or Scissors:")

print("Hello, " + x)


if raw_input("Choose a gesture between Rock, Paper or Scissors:") not in gestures:
	raw_input("Choose a gesture between Rock, Paper or Scissors:")
elif raw_input("Choose a gesture between Rock, Paper or Scissors:") in gestures:
	print ("OK")


def function(x):
	return x + 5

function(1)

gestures = ["Rock", "Paper", "Scissors"]
def choice(gestures):
	print (gestures)