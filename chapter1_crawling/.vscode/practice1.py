print("hello World")

print(15 / 7) # 나누기
print(15 // 3) # 몫
print(7 % 3) # 나머지

print(2 ** 3) # 2의 3승

digit = 1
name = "name" # string
num = True # boolean

print(34 == 100)
print(15 > 7)
print(3 <= 10)
print(3 != 100)

radius = 10
print("지름은?", radius * 2)

pi = 3.1415
print("둘레는?", pi * radius * 2)
print("넓이는?", pi * (radius ** 2))

# name = input("What is your name")
# print("Hi!", name)

# digit1 = int(input())
# digit2 = int(input())

# print(digit * digit2)

article = '''The error you're encountering is due to trying to concatenate \n
an integer (a and b) with a string in the print statement. \n
In Python, you cannot directly concatenate an integer \n
with a string using the + operator. To fix this issue, \n
you need to convert the integers to strings before concatenating \n
them with other strings. You can do this using the str() function.\n
 Here's the corrected code:'''
print(article.count("code"))
print(len(article))
print(article.find("T"))

print(article[-1])

string1 = "python"
print(string1[2:4])

string2 = "      computer     "
print(string2)
print(string2.strip()) # 공백 삭제 

string3 = "...computer..."
print(string3)
print(string3.strip(".")) # . 삭제


print("I have a {}, I have an {}".format("pen", "apple"))

interest = 0.087
print(format(interest, ".2f"))

location = ["서울시", "경기도", "인천시"]
print(location)

location.append("대전시")
print(location)

print(location[1:3])

location.remove("경기도")
print(location)

del location[0]
print(location)

a = list()
print(a)

a.insert(0, "경상남도")
print(a)

numbers = [2, 1, 4, 3]
numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

python_is_easy = "python is easy"
print(python_is_easy.split())