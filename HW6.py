#Name:Aaden hampton
#Class: 6th Hour
#Assignment:HW6

#1. Import the "random" library
import random
#2. print "Hello World!"
print("Hello World")
#3. Create three different variables that each randomly generate an integer between 1 and 10
random_number = random.randint(1,100)
random_number6 = random.randint(1,100)
random_number7 = random.randint(1,100)
print(random_number)
#4. Print the three variables from #3 on the same line.
print(random_number,random_number6, random_number7)
#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
random_number+=2
random_number6-=4
random_number7*=1.5
#6. Print each result from #5 on the same line.
print(random_number)
#7. Create a list containing four variables that each randomly generate an integer between 1 and 6
num_list=[random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6),]
print(num_list)
#8. Sort the list in #7 and print it.
num_list.sort()
print(num_list)
#9. Add together the highest three numbers in the list from #7 and print the result.
print(num_list[1]+ num_list[2]+ num_list[3])
#10. Create a list with 5 names of other students in this class and print the list.
name_list2=["Alisha", "Devin", "Jacob", "Sandler", "Victor"]
print(name_list2)
#11. Shuffle the list in #10 and print the list again.
random.shuffle(name_list2)
print(name_list2)
#12. Print a random choice from the list of names from #10.
print(random.choice(name_list2))