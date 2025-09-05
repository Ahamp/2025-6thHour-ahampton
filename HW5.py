#Name:
#Class: 6th Hour
#Assignment: HW5


#1. Create a list with 9 different numbers inside.
num_list=[8, 9, 6, 7, 5, 3, 2, 22, 67]
print(num_list)
#2. Sort the list from highest to lowest.
num_list.sort(reverse=True)
print(num_list)
#3. Create an empty list.
empty_list=[]
print(empty_list)
#4. Remove the median number from the first list and add it to the second list.
medium=num_list[4]
empty_list.append(medium)
empty_list.remove(medium)
#5. Remove the first number from the first list and add it to the second list.
empty_list.append(num_list.pop(0))
#6. Print both lists.
print(num_list)
print(empty_list)
#7. Add the two numbers in the second list together and print the result.
fortnite=sum(num_list)
#8. Move the number back to the first list (like you did in #4 and #5 but reversed).
num_list.append(fortnite)
#9. Sort the first list from lowest to highest and print it.
num_list.sort()
print(num_list)