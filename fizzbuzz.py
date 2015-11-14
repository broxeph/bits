import random

SEQUENCE = range(1,21)

def method_one():
	# This way
	for i in SEQUENCE:
		if i % 15 == 0:
			print('fizzbuzz')
		elif i % 3 == 0:
			print('fizz')
		elif i % 5 == 0:
			print('buzz')
		else:
			print(i)

def method_two():
	# That way
	for i in SEQUENCE:
		output = ''
		if i % 3 == 0:
			output += 'fizz'
		if i % 5 == 0:
			output += 'buzz'
		if not output:
			output = i
		print(output)

if __name__ == '__main__':
	if random.randint(0,1):
		method_one()
		print ('(This way)')
	else:
		method_two()
		print ('(That way)')