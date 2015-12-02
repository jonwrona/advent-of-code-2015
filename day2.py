data = open("input/day2-input.txt")

# PART 1
# How much total wrapping paper do we need?
# 2*l*w + 2*w*h + 2*h*l
# add area of shortest side

# PART 2
# How much ribbon do they need?
# perimeter of shortest side + volume 

total_area = 0
total_length = 0
for dimStr in data:
	# get and sort dimensions
	d = sorted([int(dim) for dim in dimStr.split("x")])
	# PART 1 code
	area = 3 * d[0] * d[1] + 2 * d[1] * d[2] + 2 * d[2] * d[0];
	total_area += area
	# PART 2 code
	length = 2 * d[0] + 2 * d[1] + d[0] * d[1] * d[2]
	total_length += length
print total_area, total_length
# CORRECT ANSWER: 1598415 3812909