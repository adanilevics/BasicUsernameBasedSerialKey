import hashlib
import os

database_path = r'mockdatabase.txt'
#database_path = 'Licensing'
#print(database_path+"\mockdatabase.txt")
print("\nSign up")
user_email = input("Enter your username :")

#this doesnt change, because it is based on the string that is being encoded, you must implement something for spaces
#because spaces affect the serial key outcome, any character affects the serial key outcome
#print(hashlib.md5(user_email.encode('utf-8')).hexdigest())

with open(database_path, 'a') as f:
    f.write(str(user_email)+'\n')
    f.close

print("\nSerial key assigned to user : " + str(hashlib.md5(user_email.encode('utf-8')).hexdigest()))

print("\nLog in")
user_input_email = input("Enter your username :")
user_input_serial = input("Enter your serial key :")

def search_str(file_path, string_to_search):
    with open(file_path, 'r') as file:
        # read all content of a file
        content = file.read()
        # check if string present in a file
        if user_input_email in content:
            print('User exists')
            out_search_result = True
        else:
            print('User does not exist')
            out_search_result = False
    return out_search_result

if search_str(database_path, user_input_email) == True:
    user_input_serial_check = hashlib.md5(user_email.encode('utf-8')).hexdigest()
    print("Correct serial " + user_input_serial_check)
    print("Entered serial " + user_input_serial)
    if user_input_serial == user_input_serial_check:
        print("Access granted")
    else:
        print("Acess denied, serial key is invalid")
else:
    print("Email not found")
