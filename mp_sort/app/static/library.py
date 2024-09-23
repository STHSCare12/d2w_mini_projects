from org.transcrypt.stubs.browser import *
import random
import copy

def gen_random_int(number, seed):
	random.seed(seed)
	my_list = []
	for i in range(number):
		my_list.append(i)
	random.shuffle(my_list)
	result = copy.copy(my_list)
	return result

def generate():
	number = 10
	seed = 200

	# call gen_random_int() with the given number and seed
	# store it to the variable array
	array = None
	array = gen_random_int(number, seed)
	n = len(array)

	# convert the items into one single string 
	# the number should be separated by a comma
	# and a full stop should end the string.
	
	array_str = None
	if array_str is None:
		array_str = ""

	for i in range(n):
		array_str += str(array[i]) + ','
	array_str = array_str[:-1]
	array_str = array_str + '.'
	# return array_str

	# This line is to placed the string into the HTML
	# under div section with the id called "generate"	
	document.getElementById("generate").innerHTML = array_str


def sortnumber1():
	'''	This function is used in Exercise 1.
		The function is called when the sort button is clicked.

		You need to do the following:
		- get the list of numbers from the "generate" HTML id, use document.getElementById(id).innerHTML
		- create a list of integers from the string of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	generateNum = document.getElementById('generate').innerHTML
	array = []
	for i in generateNum.split(','):
		array.append(int(i))
	n = len(array)
	swapped = True
	while swapped == True:
		swapped = False
		new_n = 0
		for si in range(1, n):
			if array[si-1] > array[si]:
				array[si-1], array[si] = array[si], array[si-1]
				swapped = True
				new_n = si
		n = new_n
	array_str = None
	if array_str is None:
		array_str = ""

	for i in range(len(array)):
		array_str += str(array[i]) + ','
	array_str = array_str[:-1]
	array_str = array_str + '.'
	
	document.getElementById("sorted").innerHTML = array_str

def sortnumber2():
	'''	This function is used in Exercise 2.
		The function is called when the sort button is clicked.

		You need to do the following:
		- Get the numbers from a string variable "value".
		- Split the string using comma as the separator and convert them to 
			a list of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	# The following line get the value of the text input called "numbers"
	value = document.getElementsByName("numbers")[0].value

	# Throw alert and stop if nothing in the text input
	if value == "":
		window.alert("Your textbox is empty")
		return

	# Your code should start from here
	# store the final string to the variable array_str
	array = []
	for i in value.split(','):
		array.append(int(i))
	n = len(array)
	swapped = True
	while swapped == True:
		swapped = False
		new_n = 0
		for si in range(1, n):
			if array[si-1] > array[si]:
				array[si-1], array[si] = array[si], array[si-1]
				swapped = True
				new_n = si
		n = new_n
	array_str = None
	if array_str is None:
		array_str = ""

	for i in range(len(array)):
		array_str += str(array[i]) + ','
	array_str = array_str[:-1]
	array_str = array_str + '.'

	document.getElementById("sorted").innerHTML = array_str


