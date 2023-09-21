with open('fileprocessor.input', 'r') as file:
    lines = file.readLines()

print("Printing out User Data:\n")

for line in lines:

    user_data = line.strip().split(':")

    if user_data[0].startswitch('#'):
        continue 
    username = user_data[0]
    password = user_data[1]
    userid = user_data[2]
    groupid = user_data[3]

    print(f"The user {username} has a password of {password} and has userid {userid and groupid {groupid}")
    print("\nEnd of User Data")
