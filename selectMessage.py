# program which prints a message based on user input/function implementation

print("Please enter 1 for printing message 1")
print("Please enter 2 for printing message 2")
print("Please enter 2 for printing message 3")
print("Please enter 4 for printing message 4")

def message1(choice):
    print(f"You have entered {choice}")
    print('''"All our dreams can come true, if we have the courage to pursue them."''')

def message2(choice):
    print(f"You have entered {choice}")
    print('''"The future belongs to those who believe in the beauty of their dreams."''')

def message3(choice):
    print(f"You have entered {choice}")
    print('''"Some men see things as they are and say why. I dream things that never were and say why not."''')

def message4(choice):
    print(f"You have entered {choice}")
    print('''"Show me a person who has never made a mistake and I'll show you someone who has never achieved much."''')

choice = input("Please enter your choice: ")
if(choice == "1"):
    message1(choice)
elif(choice == "2"):
    message2(choice)
elif(choice == "3"):
    message3(choice)
elif(choice == "4"):
    message4(choice)
else:
    print("Invalid input. Please enter 1,2,3,4")