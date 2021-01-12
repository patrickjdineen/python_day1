#Create a while loop that displays the names of the 30th to the 44th President - Hint create a list first
presidents = ["Calvin Coolidge", "Herbert Hoover" ,"Franklin D. Roosevelt","Harry S. Truman" ,"Dwight D. Eisenhower" ,"John F. Kennedy", "Lyndon B. Johnson" ,"Richard M. Nixon" ,"Gerald R. Ford", "James Carter", "Ronald Reagan","George H. W. Bush", "William J. Clinton", "George W. Bush", "Barack Obama"]

for president in presidents:
    print(president)

#Write a loop to multiply all the numbers in a list. Sample List : [1, 2, 3, -4] Expected Output : -24

list = [1,2,3,-4]
i=0
sum=1
while i < len(list):
    sum *= list[i]
    i += 1
print(sum)


#Using Python Produce the following: (HINT: You would want to use a string, for loop[possibly multiple for loops], and concatenation for this)
#*
#**
#***
#****
#*****

star = "*"

for i in range(5):
    print(star)
    star+= "*"

#Sum of Integers Up To n
#  Write a function, add_it_up(), that takes a single integer as input
#  and returns the sum of the integers from zero to the input parameter.
#
#  The function should return 0 if a non-integer is passed in.

def add_it_up(i):
    j = 0
    sum = 0
    while j < i:
        sum = j+1
        j+=1
    print(sum)
add_it_up(5)