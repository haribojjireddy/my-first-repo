"""
age = 25
# message = "Age: " + age  # ❌ Error!
message = "Age: " + str(age) 
print(message)


x = int(input("Enterscore "))
if x < 0 or x > 100 :
    print("Invalid score! Please enter a value between 0 and 100.")
elif x == 100 :
     print("Perfect score")
elif x >=90 :
     print("Grade: A" , "Excellent work!")
elif x >= 80 :
     print(" Grade B " , "Good Job")
elif x >= 70 :
     print(" Grade C " , "Satisfactory")
elif x >= 60 :
     print(" Grade D " , "Needs Improvement")
elif x <= 50 :
     print(" Grade F " , "Failed")
     print("Please see instructor") """


"""age = float(input("Enter your age: "))
student = input("Are you a student? (yes/no): ").strip().lower()
if age < 18 and student == "yes":
    print("Ticket price: $5")


age = float(input("Enter your age: "))
student = input("Are you a student? (yes/no): ").strip().lower()
if age < 0 or age > 100:
    print("Invalid age! Please enter a value between 0 and 100.")
elif age < 18 and student == "yes":
    print("Ticket price: $5")
elif age < 18 and student == "no":
    print("Ticket price: $7")
elif age >= 18 and student == "yes":
    print("Ticket price: $8")
else:
    print("Ticket price: $10") 


username = input("Enter your username").strip()
password = input("enter your password").strip()
if not username:
    print("Username Required")
elif not password:
    print("Password Required")
elif username != "admin":
    print("Enter correct username")
elif username != "secret123":
    print("Enter correct password")
else:
    print("login successful") 


BillAmount = float(input("Enter bill amount"))
Tipamount = BillAmount * 0.18 # 18% tip
total = BillAmount + Tipamount
Splitamount = total / 4
print("Total Bill",total)
print("Split Amount:", Splitamount ) 




hours = 2
minutes = 30
seconds = 45
totalseconds = hours * 3600 + minutes * 60 + seconds
print("TotalSeconds: " , totalseconds) 

num = int(input("Enter a 3-digit number: "))

hundreds = num // 100          # remove last two digits
tens = (num // 10) % 10        # remove last digit, then take remainder
ones = num % 10                # last digit


print("Hundreds:", hundreds, ", Tens:", tens, ", Ones:", ones) """



x = "madan"
if x == x[::-1]:
    print("palindram")

else:
   print("not a plindram")