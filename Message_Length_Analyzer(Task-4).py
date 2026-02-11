messages = ["Hi", "Welcome to the platform", "OK"]

print("Message Length Analysis")
print(" ")

for msg in messages:
    length = len(msg)
    print("Message:", msg)
    print("Length :", length)
    
    if length > 10:
        print("Status : Long Message (More than 10 characters)")
    else:
        print("Status : Short Message")
    
    print(" ")
