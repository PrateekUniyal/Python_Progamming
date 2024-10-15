# Program to practice split function
numbers = "1 2 3 4 5"
new_list = [int(num) for num in numbers.split()]
message = "This program is made to understand split function better"
new_message = message.split()
numbers1 = "12345678"
new_numbers1 = numbers1.split()
num = [int(digits) for digits in new_numbers1]
print("The length of num is :",len(num))
print("The length of new_numbers1 is: ", len(new_numbers1))
print("The type of num is :",type(num))
print("The type of new_numbers1 is: ", type(new_numbers1))
print(num)
print(new_message)
print(new_list)
print(new_numbers1)
sentence = "abcdefgdhijdklmndz"
# split_sentence = sentence.split()
split_sentence = sentence.split('d',2)
print(split_sentence)
sentence2 = "She sells sea shells on a sea shore."
split_sentence2 = sentence2.split("sea")
print(sentence2)
print(split_sentence2)
