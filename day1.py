instructions = open("input/day1-input.txt").read()

# ( = Go up a floor
# ) = Go down a floor

# PART 1
# What floor do we need to go to?
print instructions.count("(") - instructions.count(")");
# CORRECT ANSWER: 280

# PART 2
# At what step will we hit the basement?
floor = 0
for ind in range(len(instructions)):
	if floor == -1:
		print ind
		break
	elif instructions[ind] == "(":
		floor += 1
	elif instructions[ind] == ")":
		floor -= 1
# CORRECT ANSWER: 1797