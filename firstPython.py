def grannys_Response(greeting):
    if greeting.islower() == True:
        print("SPEAK UP, KID!")
    elif greeting.isupper() == True:
        print("NO, NOT SINCE 1946")
    elif greeting == "":
        print("WHAT?")

print("HEY KID!")
greeting = input()
grannys_Response(greeting)

second_Greeting = input()
grannys_Response(second_Greeting)

third_phrase = input()
grannys_Response(third_phrase)

first_bye = input()
print("LEAVING SO SOON?")
second_bye = input()
print("LATER, SKATER!")
