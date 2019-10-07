#Write a python program to solve a classic ancient Chinese puzzle.
#We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?


def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0
    flag = 0
    for i in range(0,heads+1):
        chicken_count = i
        rabbit_count = heads - chicken_count
        if(chicken_count * 2 + rabbit_count * 4 == legs):
            flag = 1
            break
    if flag == 0:
        print(error_msg)
    else:
        print(chicken_count,rabbit_count)
        

heads = (int)(input("enter head count:"))
legs = (int)(input("enter legs count:"))
solve(head,legs)
