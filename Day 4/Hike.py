"""
An organization has decided to provide salary hike to its employees based on their job level. Employees can be in job levels 3 , 4 or 5.
Hike percentage based on job levels are given below:

Job level 	Hike Percentage (applicable on current salary)
  3		            15
  4		            7
  5		            5 
In case of invalid job level, consider hike percentage to be 0.
Given the current salary and job level, write a python program to find and display the new salary of an employee. 
"""

current_salary = (int) (input("Enter salary"))
job_level = (int) (input("Enter job level"))

def find_new_salary(current_salary,job_level):
    if(job_level == 3):
            new_salary = current_salary + current_salary * 0.15
     elif(job_level == 4):
            new_salary = current_salary + current_salary * 0.07
     elif(job_level == 5):
            new_salary = current_salary + current_salary * 0.05
     else:
            new_salary = current_salary
     return new_salary

new_salary = find_new_salary(current_salary,job_level)
print(new_salary)
