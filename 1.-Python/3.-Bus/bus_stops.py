stops = [(10, 0), (4, 1), (3, 5), (3, 4), (5, 1), (1, 5), (5, 8), (4, 6), (2, 3)]
len(stops)

#create list variation of passenger
var_p = []

#insert variation per stop in list
for p in stops:
    p_in, p_out = p
    var_p.append (p_in - p_out)

var_p



#creat list of passenger per stops
passenger_per_stops = []
total_passenger = 0
for x in var_p:
	total_passenger = total_passenger + x
	passenger_per_stops.append (total_passenger)

passenger_per_stops


max (passenger_per_stops)

x = float(len(stops))
y = float(sum(passenger_per_stops))
avg = y/x
avg


list1 =[]

for z in passenger_per_stops:
	z = (z - avg)**2
	list1.append (z)

stdev = (sum(list1)/len(list1))**(0.5)

stdev

