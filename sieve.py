import math
def sieve(n): 
	A = []
	for i in range(0,n-1):
		A.append(True)
	if n < 2:
		return
	for i in range(2,int(math.floor((math.sqrt(n)))),1):
		if A[i] is True:
			for j in range(i*i,n-1,i):
				A[j] = False
	num_prime = 0
	for i in range(2,n-1):
		if A[i] is True:
			print("Prime: " + str(i))
			num_prime+=1
	print("Number of prime numbers between 0 and " + str(n) + " is: " + str(num_prime) + "\n")

def show_instr():
	print("Press h for help\nPress q to quit (or ctrl-c)\nThe application will prompt for a number, this is the upper limit of the prime numbers that will be generated, all prime numbers between 2 and your input (n) will be displayed, followed by the count.\n")

print("Welcome to the the Sieve Solver")
show_instr()
while True:
	n = raw_input("Enter a number: ")
	
	if n == "h":
		show_instr()
		continue
	if n == "q":
		break
	
	sieve(int(n))
