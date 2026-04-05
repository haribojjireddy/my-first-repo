x = 1
y = 10.5
z = x + y
print(float(z))



int_num = 10
float_num = 3.5
result = int_num + float_num
print(result)        # 13.5
print(type(result))


base = 2
exponent = 3
result = base ** exponent
print(result)  # 8 (2³ = 2 × 2 × 2)


total_score = 475
num_tests = 5
average = total_score // num_tests
print(average)  # 95

total_bill = 100
num_people = 3
per_person = total_bill // num_people
print(per_person)  # 33
remainder = total_bill % num_people
print(remainder)  # 1 (someone pays extra dollar)

""" Integers are whole numbers (no decimals)
Use / for float division, // for integer division
Use % to get remainder
Integer + float = float
Python integers have no size limit
Use integers when you don't need decimal precision """

result = 0.126 + 0.223
print(round(result, 2))  # 0.3


int_num = 10
float_num = 3.5
result = int_num + float_num
print(result)        # 13.5
print(type(result))  # <class 'float'>

text2 = 'She said, "Hi!"'
print(text2)

first = "Hello"
second = "World"
result = first + " " + second
print(result)  # "Hello World"


age = 25
# message = "Age: " + age  # ❌ Error!
message = "Age: " + str(age) 

laugh = "ha" * 3
print(laugh)  # "hahaha"
line = "=" * 20
print(line)  # "===================="


name = "Alice"
print(name.upper())  # "ALICE"
print(name.lower())  # "alice"

text = "   hello  "
print(text.strip())  # "hello"

text = "Hello World"
new_text = text.replace("World", "Python")
print(new_text)  # "Hello Python"

email = "user@example.com"
print(email.startswith("user"))  # True
print(email.endswith(".com"))    # True
print("@" in email)              # True

name = "Bob"
age = 25
message = "Name: " + name + ", Age: " + str(age)
print(message)  # "Name: Bob, Age: 25"


age = 17
has_id = True

if age >= 18:
    if has_id:
        print("You can enter the club.")
    else:
        print("You need an ID.")
else:
    print("You are too young.")


