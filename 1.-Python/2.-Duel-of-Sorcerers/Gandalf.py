gandalf = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]
saruman = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]
spells = 10
gandalf_wins = 0
saruman_wins = 0
tie = 0

results = [gandalf[i]-saruman[i] for i in range(spells)]
[-13, -55, 1, -13, 10, 1, -34, 10, 10, 5]


for x in range(spells):
	if results[x]>0:
		gandalf_wins += 1
	elif results[x]<0:
		saruman_wins += 1
	else:
		tie += 1

if gandalf_wins>saruman_wins:
	print ("Gandalf wins!")
elif gandalf_wins < saruman_wins:
	print ("Saruman wins!")
else:
	print (" Tie")

results.count (x>0)


results.count (results>0)



gandalf_wins = [results>0 for results ]

gandalf[0]-saruman[0]


for gandalf_rounds in xrange(1,10):
	pass


