directions = open("input/day3-input.txt").read()

# Helper function to facilitate movement in a direction.
def move(loc, direction):
	if direction == "^":
		loc[1] += 1
	elif direction == ">":
		loc[0] += 1
	elif direction == "v":
		loc[1] -= 1
	elif direction == "<":
		loc[0] -= 1
	return loc

# PART 1
# How many houses has at least one gift?
loc = [0, 0]
visited = [tuple(loc)]
for direction in directions:
	loc = move(loc, direction)
	loc_tup = tuple(loc)
	if loc_tup not in visited:
		visited.append(loc_tup)
print len(visited)
# CORRECT ANSWER: 2081

# PART 2
# There is a robot version of Santa.
# They alternate following directions.
# How many houses has at least one gift?
loc_santa = [0, 0]
loc_robot = [0, 0]
visited_2 = [tuple(loc_santa)]
for i, direction in enumerate(directions):
	if i % 2 == 0:
		# move santa
		loc_santa = move(loc_santa, direction)
		loc_santa_tup = tuple(loc_santa)
		if loc_santa_tup not in visited_2:
			visited_2.append(loc_santa_tup)
	else:
		# move robot
		loc_robot = move(loc_robot, direction)
		loc_robot_tup = tuple(loc_robot)
		if loc_robot_tup not in visited_2:
			visited_2.append(loc_robot_tup)
print len(visited_2)
# CORRECT ANSWER: 2341