def grannys_Response(greeting):
    if greeting.islower() == True:
        print("SPEAK UP, KID!")
    elif greeting.isupper() == True:
        print("NO, NOT SINCE 1946")
    elif greeting == "":
        print("WHAT?")

print("Hey kid!")

while True:
    users_response = input('Enter some text: ')
    if users_response == "GOODBYE" or users_response == "BYE":
        print("LEAVING SO SOON?")
        input("Say bye for the last time: ")
        print("LATER, SKATER!")
        break
    else:
        grannys_Response(users_response)

    
   