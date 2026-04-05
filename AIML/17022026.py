#Take a string as an input and check if that's palindrome or not. "madam"#

#x = "madan"
#if x == x[::-1]:
 #   print("palindram")

#else:
 #   print("not a plindram")


"""
 y = input("Enter a string: ")

if y == y[::-1]:
    print("palindram")

elif y != y[::-1]:
    print("not a plindram")
###
"""
"""
# Find sum of ascii codes in a given string. "aAX" => {97, 65, 88} = 250

x = input("enter a ascii code ")
ascii = 0
for c in x:
   ascii += ord(c)
print("ascii value: ",ascii)

# Find the sum of digits in a given integer. 374833 => 28

x = int(input("Enter the number: "))
digit_sum = 0
while x > 0:
   digit_sum += x % 10  # remove last digit ==> digit sum
   x //= 10            # get last digit
print(digit_sum) 

def student(values):
    if len(values) == 0:   # check if list is empty
        return 0
    return sum(scores) / len(values)  # average calculation

scores = [85, 92, 78, 95, 88]
print("Average score:", student(scores)) 


def count_names(list_of_names):
    vowels = "AEIOUaeiou"
    count = 0   # initialize counter
    for name in list_of_names:
        if name[0] in vowels:   # check first letter against vowels
            count += 1
    return count   # return after the loop finishes

names = ["Alice", "Bob", "Emily", "David", "Oliver", "Sarah"]
print("count", count_names(names)) 


numbers = [45, 23, 67, 89, 12, 56]

maximumvalue = max(numbers)

indexposition = numbers.index(maximumvalue)

print("maximumvalue",maximumvalue)
print("indexposition",indexposition) 


#Create a single-element tuple containing your lucky number (7). Verify it's actually a 
# tuple by printing its type.

lucky_number = (7,)
print(lucky_number)
print(type(lucky_number)) 

red= (250, 0, 0)
green= (0, 255, 0)
blue= (0, 0, 255)
print("red colour",red)
print("green colour",green)
print("blue colour",blue)
print(type(red), type(green), type(blue)) 


numbers = [5, 2, 8, 2, 9, 2, 1, 2]
target = 2

# One-liner to get all indices
indices = [i for i in range(len(numbers)) if numbers[i] == target]

print("Index positions:", indices)


def introduce(name, age, city):
    print("Hi, I'm {name}")
    print("I'm {age} years old")
    print("I live in {city}")

introduce("Alice", 25, "New York")
introduce("Bob", 30, "London") 


def greeting(greet):
    print(greet)
greeting("Hello, World!") 

def print_seperator():
    print('-' * 30)
print_seperator() 

def circle_area():
    pi = 3.14159
    radius = 5
    area = pi * (radius ** 2)
    print("Area of the circle:", area)

# Call the function
circle_area() 


def greeting(name):
    print(f"welcome,{name}")
greeting("Madan") 


for i in range(10,0,-1):
    print(i, end=" ")
print()
print("Go!") 



def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)

# Call the function with 25°C
celsius_to_fahrenheit(25)

def is_prime_number():
    num = 17
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

# Call the function
is_prime_number() 

nums=[1,2,3,4]
total=0
for num in nums:
   total += num
print(total)  """


def greet():
    print("Hello!")


def say_hello():
    print("Hello, World!")
say_hello()
say_hello()
say_hello()


def greet(name):  # 'name' is a parameter
    print(f"Hello, {name}!")

greet("Alice")  # "Alice" is an argument
greet("Bob")    # "Bob" is an argument


def add(a, b):  # a and b are parameters
    sum_result = a + b
    print(f"{a} + {b} = {sum_result}")

add(5, 3)   # 5 + 3 = 8
add(10, 20) # 10 + 20 = 30
add(7, 2)   # 7 + 2 = 9


def introduce(name, age, city):
    print(f"Hi, I'm {name}")
    print(f"I'm {age} years old")
    print(f"I live in {city}")

introduce("Alice", 25, "New York")
introduce("Bob", 30, "London")
