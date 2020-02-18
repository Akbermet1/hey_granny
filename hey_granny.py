def grannys_Response(greeting):
    if greeting.islower() == True:
        print("SPEAK UP, KID!")
    elif greeting.isupper() == True:
        print("NO, NOT SINCE 1946")
    elif greeting == "":
        print("WHAT?")

print("Hey kid!")
is_second_time = False

while True:
    users_response = input('Enter some text: ')
    if users_response == "GOODBYE" or users_response == "BYE":
        if is_second_time:
            print("LATER, SKATER")
            break
        else:
            is_second_time = True
            print('LEAVING SO SOON?')
    else:
        grannys_Response(users_response)
