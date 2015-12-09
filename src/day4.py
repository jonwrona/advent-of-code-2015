input = "iwrupvqb"
import hashlib

# Function to find number for answer.
def findHex(input, zeroCount):
	num = 1
	while True:
		if hashlib.md5(input + str(num)).hexdigest()[:zeroCount] == "0" * zeroCount:
			print num
			break
		num += 1

# PART 1
# Find a string which has an MD5 that starts with five
# zeroes, where the string consists of the input followed
# by a number that is at least 1.
findHex(input, 5)
# CORRECT ANSWER: 346386

# PART 2
# Same as part one with six zeroes.
findHex(input, 6)
# CORRECT ANSWER: 9958218