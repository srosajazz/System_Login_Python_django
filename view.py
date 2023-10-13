from controller import ControllerRegister
from controller import ControllerLogin
while True:
    print("=========[Menu]=========")
    choose = int(input('Type 1 for register\nType 2 for Logo on\nType 3for Exit:\n'))
    if choose == 1:
        name = input('Enter your name')
        email = input('Enter yor email')
        password = input('Enter your password')
        result = ControllerRegister.register(name, email, password)

        if result == 2:
            print("The size of the name is invalid")
        elif result == 3:
            print("Email must be longer than 200 characters")
        elif result == 4:
            print("Password invalid")
        elif result == 5:
            print("Email already register")
        elif result == 6:
            print("Error intern 500")
        elif result == 1:
            print("Register with Success!")
    elif choose == 2:
        email = input('Enter yor email')
        password = input('Enter your password')
        result = ControllerLogin.login(email, password)
        if not result:
            print("Invalid Email or Password")
        else:
            print(result)
    else:

        break
