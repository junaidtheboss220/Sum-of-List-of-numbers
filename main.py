numbers = [1,2,3,4,5,6,7,8,9,10]
sum = 0

# print each number of list
# 
for i in range (10):
    num = (numbers[i])
    sum += num 
print (sum)

#  therange function
# print the list which has numbers 0-5


print ([1,2,3,4,5])
print(list(range(1,6)))
print(list(range(2,9)))

# Print the list of numberes from two to seventeen and skip two numbers in between every number

print (list(range(2,18,2)))
print (list(range(2,101,6)))

# print 10 to 0

print (list(range(10,-1,-1)))

genres = ["rock" , "jazz", "rap" , "drill" , "pop"]

# Iterate over the list wwithout using the index

for nice in genres:
    print (f"I like {nice}")

#  else in for loop

digits = [1 , 2 , 3 , 4 ,5]

for num in digits:
    print (f"i am not {num}")
else:
    print ("no items left")

# else for loop with break

student_name = "jibran"

marks = {"mike":67,"mark":69 , "dequavius":68}

for student in marks:
    if student == student_name:
        print (marks[student])
else:
    print ("No entry with the name you have entered has been found ")