""""
1. ask for login or sign up
2. if sign up, make new file which saves a password
    i. ask for password and save into variable
    ii. make new text file
    iii. save password into the text file
3. if log in, check if user input matches up with password in the file
"""

# print(var)
# with open("filename.txt", "r/w/a") as varName
# varName = input("What do you want to input? ")
#if loginyes == "yes":
    #uiohaweducv
# sam = 25 
# is sam == 25
# file.write() 

choice = input("Signup or Login?")

if choice == "signup":
    password = input("What is your password?")
    with open("filename.txt", "w") as file:
        file.write(password)


elif choice == "login":
    login = input ("what is your password?")
    with open("filename.txt", "r") as file:
       correctpas = file.read()

    if login == correctpas:
        print ("correct password") 

    else:
        print ("wrong password")



    



 