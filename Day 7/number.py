"""
Write a python program which finds the maximum number from num1 to num2 (num2 inclusive) based on the following rules.

*Always num1 should be less than num2
*Consider each number from num1 to num2 (num2 inclusive). Populate the number into a list, if the below conditions are satisfied
  *Sum of the digits of the number is a multiple of 3
  *Number has only two digits
  *Number is a multiple of 5
Display the maximum element from the list
In case of any invalid data or if the list is empty, display -1.
"""


def find_max(num1, num2):
    max_num=-1
    if(num1 >= num2):
        return max_num
    while(num1 <= num2):
        if(num1 % 5 == 0 and num1 // 10 > 0 and num1 // 10 < 10 and num1 % 3 == 0):
            max_num = num1   
        num1 +=1       
    return max_num

num1 = (int)(input("Enter num1"))
num2 = (int)(input("Enter num2"))
max_num=find_max(num1,num2)
print(max_num)
