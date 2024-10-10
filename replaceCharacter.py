# Program to replace all character in a text with a given character
text = (input("Please enter the text: "))
ch =  input("enter the character to replace with: ")[0]
if text == "" or ch == '':
    print("Invalid input")
else:
    print(ch * (len(text)))