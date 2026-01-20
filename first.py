#print("Hello World!!")

#Variables:Stores the values of the variable 
# Mentor_name ="Divya"
# print(Mentor_name)

#Data Types
# name = "Vignesh"
# num=87
# dec_num= 87.98
# print(type(name),type(num),type(dec_num),sep='\n')

#Invalid addition
# age = 20
# name = "Divya"
# print(age + name)

# #List Manipulation Examples
# fruits=["apple", "banana", "orange"]
# # print(fruits[-4])   #IndexError: list index out of range
# fruits[1] ="kiwi"
# print(fruits)
# fruits.append("grapes")
# fruits.insert(2,"guava")
# print(fruits)

# #Task1:
# animals = ["cat", "dog", "rabbit", "cow"]
# # Insert "lion" at index 1
# animals.insert(1,"lion")
# # Change "rabbit" to "horse"
# # Print the list.
# animals[-2] = "horse"
# print(animals)

# #Task2:
# # Given:
# marks = [45, 67, 89, 34, 67]
# #### Change the last value to 90
# marks[-1] = 90
# marks.insert(1,50)
# marks.append(100)
# marks.remove("67")    #removes the specific value
# marks.pop             #removes last index
# marks.pop(2)          #removes the specific index
# len(marks)            #returns the Length of the list 
# marks.sort()                 #sorts the number from ascending to descending
# marks.sort(reverse=True)     #sorts the number from descending to ascending
# print(marks.count(67))
# print(marks.index(34))
# print(marks)
# # Insert 50 at index 1
# # Append 100
# # Print the final list.

# ##Tuple
# mixed = ("vicky", 98, 69.89)
# mixed[1] = 10000
# print(mixed)

#Tuple with single element
# A = (4,)
# print(type(A))

##Dictionary
# student = {
#     "name" : "vicky",
#     "age"  : 29,
#     "city" : "coimbatore"
# }

# student["marks"] = 98  #adding a value to the dict
# student["age"] = 35  #updating a value to the dict
# print(student.get("marks"))
# print(student["age"])
# print(student)

# a = 2
# b = 2.0
# print(a==b)
# type(a) != type(b)
# print(10 <> 5)

# age = 25
# salary = 50000

# print(age > 18 and salary > 30000)

# age=20
# if age>=18:
#     print("eligible to vote")
# else:
#     print("not eligible to vote")

# num = 6
# if num%2==0:
#     print("Number is even")
# else:
#     print("Number is Odd")


# rad = int(input("Radius is:"))
# print("Area of the circle is:",3.14*rad*rad)
# print("Perimeter of the circle is:",2*3.14*rad)

# rad = int(input("Radius is:"))
# if rad > 0:
#     print("Number is Positive")
# elif rad < 0:
#     print("Number is Negative")
# elif rad == 0:
#     print("Number is Zero")
# else:
#     print("Give a valid number")
    
# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(year, "is a Leap Year")
# else:
#     print(year, "is not a Leap Year")

# username = input("Enter the user name:")
# password = input("Enter the password:")
# if username == "admin" and password == "1234":
#     print("Login successful")
# else:
#     print("Login unsuccessful")

# for i in (range(5,0,-1)):
#     print(list(i))
    
# H = ['Egg', 'Bacon', 'Ham']
# for item in H:
#     item=item[1]+'s'
#     print(item)

# a = range
# print(a)

# fruits = ["Apple", "Banana", "Kiwi", "Peach"]
# for index, fruit in enumerate(fruits):
#     print(index, fruit)
    
# scores = [87, 56, 34, 98, 90, 35]
# for i in scores:
#     # print(i)
#     if i >= 60:
#         print("Your score is above 60:",i)
# cumulative = 0
# for i in range(1,6):
#     cumulative = cumulative + i
# print(cumulative)
#     # c = i+j
    
# print(sum([1,5,6],8))

# i=2
# while i < 100:
#     ans = i % 2
#     if ans ==  0:
#         # print (ans)
#         i  = i+2
#         print(i)

# num = input("Enter the number")
# num = int(num)
# print(len(num)) 
# print(len(num))

scores = [87, 56, 34, 98, 90, 35]
sc=max(scores)
scores.sort()
greatest = scores[-1]
print(greatest)
#Last line added
