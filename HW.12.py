#Name:Aaden Hampton
#Class: 5th Hour
#Assignment: HW12

#1. Create a while loop with variable i that counts down from 5 to 0 and then prints
#"Hello World!" at the end.
print("Hello World")
#2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).
''' 
i = 0
while i <= 30:
print(i)
time.sleep(0.4)
1+=2
'''
#3. Create a while loop that prints from 1 to 30 and continues (skips the number) if the
#number is divisible by 3.
num = 1
while num <= 30:
    if num % 3 == 0:
        num += 1
        continue
    print(num)
    num += 1
#4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
#and then breaks the loop if it's a 1.
import random

while True:
    roll = random.randint(1, 6)
    print("Roll is", roll)
    if roll == 1:
        break
#5. Create a while loop that asks for a number input until the user inputs the number 0.
ask= int(input("Enter 0 to quit"))
while ask !=0:
    ask = int(input("Enter 0 to quit"))

