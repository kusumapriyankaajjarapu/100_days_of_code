#Write a Python program to generate the next 15 leap years starting from a given year. Populate the leap years into a list and display the 
#list.


def is_leap_year(year):
    if(year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)):
        return True
    return False
    
def find_leap_years(given_year):
    list_of_leap_years = [0] * 15
    if(is_leap_year(given_year)):
        list_of_leap_years[0] = given_year
    else:
        while(is_leap_year(given_year) != True):
            given_year += 1
        list_of_leap_years[0] = given_year
    for i in range(1,len(list_of_leap_years)):
        year = list_of_leap_years[i-1] + 4
        if(is_leap_year(year)):
            list_of_leap_years[i] = year
        else:
            list_of_leap_years[i] = year + 4

    return list_of_leap_years


year = (int)(input("Enter year"))
list_of_leap_years=find_leap_years(year)
print(list_of_leap_years)
