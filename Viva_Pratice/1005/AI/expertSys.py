def greet(Name):
 print("Welcome user!,My name is {0}.".format(Name))
 print("I am here to help you.")
def department(dep):
 print("On which department do you want to visit?")
 dep=input()
 if dep=="First year":
    print("The {0} department is on 1st floor.".format(dep))
 elif dep=="Mechanical":
    print("The {0} department is on 2nd floor.".format(dep))
 elif dep=="Civil":
    print("The {0} department is on 3rd floor".format(dep))
 elif dep=="Computer":
    print("The {0} department is on 4th floor.".format(dep))
 elif dep=="IT":
    print("The {0} department is on 5th floor".format(dep))
 elif dep=="ENTC":
    print("The {0} department is on 6th floor.".format(dep))
 elif dep=="MBA":
    print("The {0} department is on 7th floor".format(dep))
 else:
    print("Sorry we don't have an department which you want! ")
    print("Contact authorised person for related information ")
 print("Which room number do you want to go?")
 roomNo=input()
 if roomNo=="401":
    print("The {0} room is on right side.".format(dep))
 elif roomNo=="402":
    print("The {0} room is on left side.".format(dep))
 else:
    print("Sorry we don't have an room number which you want! ")
    print("Contact authorised person for related information ")

 print(input("Do you want to visit another department?"))
 y="yes"
 n="no"
 if y=="yes":
     return department(dep)
 elif n=="no":
     print ("Ok!")
 else:
     print("Ok!")
greet('Nilesh') # change it as you need
department("First year " or "Mechanical" or "Civil" or "Computer" or "IT" or "ENTC" or "MBA")
print("Thank you for visiting!")