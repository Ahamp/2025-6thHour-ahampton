#Name:Aaden Hampton
#Class: 5th Hour
#Assignment: HW14


#1. Create a for loop with variable i that counts down from 5 to 1 and then prints "Hello World!"
#at the end.

for i in range(5, 0, -1):
    print(i)
else:
    print("Hello World")
#2. Create a for loop that counts up and prints only even numbers between 1 and 30.
for j in range(0, 30, 2):
    print(j)
#3. Create a for loop that prints from 1 to 30 and continues (skips the number) if the number is
#divisible by 3.
for l in range(1, 31):
    if l % 3 == 0:
        continue
    print(l)

#4. Create a for loop that prints 5 different animals from a list.
list_k=["dog", "cat", "tiger", "horse", "jaguar"]
for k in list_k:
    print(k)
#5. Create a for loop that spells out a word you input backwards.
#(HINT: Google "How to reverse a string in Python")
for i in input("Enter an Animal")[::-1]:
    print(i)
#6. Create a list containing 10 integers of your choice and print the list.
list_a=[1,3,5,7,11,13,17,19,23,27]
print(list_a)
#7. Create two empty variables named evenNumbers and oddNumbers.
even_count = 0
odd_count = 0
#8. Make a loop that counts the number of even and odd numbers in the list, and prints the
#result after the loop.

for number in list_a:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Number of even numbers: {even_count}")
print(f"Number of odd numbers: {odd_count}")
#9. Create a variable that asks the user for an integer and an empty integer variable.
var_d=int(input("Enter an integer: "))
var_e=1

#10. Create a loop with a range from 1 to the number the user input. Use the loop to find the
#factorial of that number and print the result. A factorial of a number is that number multiplied
#by every number before it until you reach 1. (For example: 5! is 5 x 4 x 3 x 2 x 1 = 120)
for q in range(1,var_d+1):
    var_e*=q
print(var_e)