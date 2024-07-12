import random as rd

def random_password_generator():
    length = rd.randint(8,20)
    password = []
    Final = ""
    Choice = ["Uppercase","Lowercase","numbers","special characters"]
    for i in range(length):
        choice = rd.choice(Choice)
        if choice == "Uppercase":
            password.append(chr(rd.randint(65,90)))
        elif choice == "Lowercase":
            password.append(chr(rd.randint(97,122)))
        elif choice == "numbers":
            password.append(chr(rd.randint(48,57)))
        else:
            password.append(chr(rd.randint(33,47)) or chr(rd.randint(58,64)) or chr(rd.randint(91,96)) or chr(rd.randint(123,126)))
    for j in password:
        Final+=j
    return Final
