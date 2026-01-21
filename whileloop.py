count = 1
while count <= 5:
    print(count)
    count += 1

print("---------------")

num = 2
while num < 10:
    print(num)
    num += 2

print("---------------")

password = "python123"
user_input = ""

while user_input != password:
    user_input = input("Enter password: ")

print("Access granted!")