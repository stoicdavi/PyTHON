#A code to sort the names in a list and print the number of names in the list 
name_List = []
number_of_names = int(input("Enter the number of Names you want to enter:"))
for i in range(number_of_names):
    names = input(f'Enter the name of at index {i} :')
    name_List.append(names)

# printing the list of names
print("Printing the list of names:")
for name in name_List:
    print(name, sep=" ")
print("The number of names in the list before removing duplicates is:", end=" ")
print(len(name_List))

# generating a sorted list of names
print("The sorted list of names is:")
sorted_list = sorted(name_List)
for name in sorted_list:
    print(name)

# removing duplicates from the list
unique_list = (set(sorted_list))
print("The number of names in the list after removing duplicates is:", end=" ")
print(len(unique_list))
for name in unique_list:
    print(name)