msg = "Welcome to Python david"
print(msg.upper()) # WELCOME TO PYTHON
print(msg.lower()) # welcome to python
print(msg.capitalize()) # Welcome to python
print(msg.title()) # Welcome To Python
print(msg.swapcase()) # wELCOME TO pYTHON
print(len(msg))
print(msg.count('o')) 
msg1 = "Welcome to Python 101: Strings"
mani = msg1[-10]+" "+msg1[:8]+" "+msg1[25:30]+" "+msg1[8:10]+" Tyler"
print(mani.title())
print(mani[::-1].title())
print("""Welome herr
      how are you doing,
      I hope you are doing well""")#multiline string
list = ["Welcome", "to", "Python", "101", "Strings"]
print(" ".join(list))
list.sort()#sorts in alphabetical order
print(list)
list.sort(reverse=True)#sorts in reverse alphabetical order
print(list)
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))
print(max(numbers))
print(min(numbers))
print(min(msg))
list.append("david")#adds to the end of the list
print(list)
list.extend(["david", "is", "awesome"])#combines two lists
print(list)