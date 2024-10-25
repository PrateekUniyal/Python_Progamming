email = input("Please enter the email: ")
print()
username = ""
domain_name = ""

slice_index = email.index('@')
username = email[:slice_index]
domain_name = email[slice_index+1:]

print(f"The user name is :{username}")
print(f"The domain name is : {domain_name}")