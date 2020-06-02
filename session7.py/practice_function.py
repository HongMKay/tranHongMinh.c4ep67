#bài 1: find the max of the three numbers
def max_of_two( x, y ):
    if x > y:
        return x
    return y

def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )
print(max_of_three(3, 6, -5))
#Bài 2: Count sum in a list
def sum_of_list(lst):
    return sum(lst)

print(sum_of_list([3, 4, 5, 6]))

#Bài 3: to multiply all the numbers in a list
def multiply_list(lst):
    product = 1
    for x in lst:
        product *= x
    return product
 
print(multiply_list([3, 4, 5]))

#Bài 4: reverse a string
def reverse_string(content):
    a = content[::-1]
    return a

print(reverse_string("1234abcd"))

#Bài 5: calculate the factorial of a number. The function accepts the number as an argument

def cal_factorial(content):
    factorial = 1
    if int(content) >= 0:
        for i in range(1, int(content)):
            factorial *= i
    else:
        print("Làm gi có :)")
    return factorial

print(cal_factorial(9))
print(cal_factorial(0))

#Bài 6: check whether a number is in a given range
def in_given_range(content):
    if int(content) in range(3,12):
        print( "%s is in the range"%str(content))
    else :
        print("The number is outside the given range.")
in_given_range(5)

#Bài 7: Write a function that accepts a string and 
# calculate the number of upper case letters and lower case letters.
def count_the_upperCase(content):
    upperCase = 0
    lowerCase = 0
    for i in content:
        if i.isupper() == True:
            upperCase += 1
        else:
            lowerCase += 1
    print("The number of upperCase letters is:",upperCase)
    print("The number of lowerCase letters is:",lowerCase)
count_the_upperCase("HiHiDoDien")
#Bài 8: Write a function that takes a list and returns a new list with unique elements of the first list. 
def unique_lst(lst):
    a = list(set(lst)) #set chỉ chứa những phần tử unique
    print(a)
unique_lst([1,1, 2, 3, 4, 4, 3, 2, 3, 4, 5])

#Bài 9: Check if a number is prime or not (số nguyên tố)
def prime_number(num):
    if num > 1:
        for i in range(2,num):
            if (num%i) == 0:
                print(num,"is not a prime number")
                break
        else:
            print(num,"is a prime number")        
prime_number(23475)

#Bài 10:  Write a Python function to print the even numbers from a given list.
#Bài 11: Write a function to check whether a number is perfect or not. (là số bằng tổng các ước của nó)