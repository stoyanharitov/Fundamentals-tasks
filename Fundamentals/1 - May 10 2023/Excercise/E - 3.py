number = int(input())
message = ""
for i in range(number):
    command = int(input())
    if command == 88:
        message = "Hello"
    elif command == 86:
        message = "How are you?"
    elif command < 88:
        message = "GREAT!"
    else:
        message = "Bye."
    print(f'{message}')