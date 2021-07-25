#Write your code below this row 👇

#The Fizzbuzz game challenge
n = input("Enter the maximum number for the range in the fizzbuzz competition \n")
#converting the user input to integer
num = int(n) +1
for number in range (1, num):
	if number%3 == 0 and number%5 == 0:
		print("FizzBuzz")
	elif number % 3 == 0:
		print("Fizz")
	elif number % 5 == 0:
		print("Buzz")
	else:
		print(number)
