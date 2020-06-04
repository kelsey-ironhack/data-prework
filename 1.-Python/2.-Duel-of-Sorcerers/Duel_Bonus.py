spells = 10

gandalf = [50, 40, 40, 10, 50, 10, 40, 50, 50, 50]
saruman = [45, 45, 25, 50, 25, 40, 10, 45, 10, 10]

gandalf_wins = 0
saruman_wins = 0

for i in range(spells):
    if gandalf[i] > saruman[i]:
        gandalf_wins += 1
        if gandalf_wins == 3:
            print(('Gandalf score: ' + str(gandalf_wins), 'Saruman score: ' + str(saruman_wins)))
            print('Gandalf wins')
            break
        else:
            saruman_wins = 0
            print(('Gandalf score: ' + str(gandalf_wins), 'Saruman score: ' + str(saruman_wins)))
    elif gandalf[i] < saruman[i]:
        saruman_wins += 1
        if saruman_wins == 3:
            print(('Gandalf score: ' + str(gandalf_wins), 'Saruman score: ' + str(saruman_wins)))
            print('Saruman wins')
            break
        else:
            gandalf_wins = 0
            print(('Gandalf score: ' + str(gandalf_wins), 'Saruman score: ' + str(saruman_wins)))


