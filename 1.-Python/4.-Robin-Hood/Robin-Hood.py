points = [(4, 5), (-0, 2), (4, 7), (1, -3), (3, -2), (4, 5), (3, 2), (5, 7), (-5, 7), (2, 2), (-4, 5), (0, -2), (-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2), (5, 7), (5, 7), (2, 2), (9, 9), (-8, -9)]

#find duplicates, use set to count each point
duplicate = set()
for z in points:
	if points.count(z) > 1:
		duplicate.add(z)

duplicate

#sort buy quadrant
quadrant = []
for (x,y) in points:
	if x<=0 and y <= 0:
		quadrant.append("Q3")
	elif x<=0 and y>=0:
		quadrant.append("Q4")
	elif x>=0 and y>=0:
		quadrant.append("Q1")
	elif x>=0 and y<=0:
		quadrant.append("Q2")
	elif x==0 and y==0:
		quadrant.append("center")
	else: 
		quadrant.append("NULL")

quadrant

print ('quadrant Q1 has been hit by', quadrant.count ("Q1"), 'arrows')
print ('quadrant Q2 has been hit by', quadrant.count ("Q2"), 'arrows')
print ('quadrant Q3 has been hit by', quadrant.count ("Q3"), 'arrows')
print ('quadrant Q4 has been hit by', quadrant.count ("Q4"), 'arrows')



#Calculate distance to center
distance = []
for (x,y) in points:
	distance.append((x**2 + y**2)**0.5)

#find the minimum distance to center and return the index
position_distance = [i for i , x in enumerate(distance) if x == min(distance)]

position_distance

#find the points closest to center based on index (position distance)
points_closest = []

points_closest = [points[x] for x in position_distance]

points_closest


#Calculate distance to center
distance = []
for (x,y) in points:
	distance.append((x**2 + y**2)**0.5)

#find the distance to center > 9 and return the index
position_distance = [i for i , x in enumerate(distance) if x > 9]

position_distance

#find the points closest to center based on index (position distance)
points_over9 = []

points_over9 = [points[x] for x in position_distance]

points_over9
