#a code to check whether the user is eligible for a discount
goodWorth = int(input("Enter the value of the goods you are purchasing:"))
if goodWorth >= 1000:
    print("You are eligible for a discount")
    dicount = goodWorth * 0.05
    total = goodWorth - dicount
    print("The discount is: {}".format(dicount))
    print("Your total is: {}".format(total))
else:
    print("You are not eligible for a discount")
    print("Your total is: {}".format(goodWorth))