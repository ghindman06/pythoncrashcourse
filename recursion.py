def factorial(x):
    #base
    if x <= 1:
        return 1
    #recursive
    else:
        return x * (factorial(x-1))
    


def fibonacci(x):
    #base
    if x <= 1:
        return x
    #recursive
    else:
        return fibonacci(x-1) + fibonacci(x-2)
    
def cleanString(input):
    output = ""
    for c in input:
        if c.isalpha():
            output += c.lower()
    return output

def isPalindrome(input):
    #base
    if len(input) <= 1:
        return True
    #recursive
    else:
        if input[0] == input[-1]:
            return isPalindrome(input[1:-1])
        else:
            return False
        
def hanoiSolver(start, end, mid, discs):
    #base
    if discs == 0:
        return
    #recursive
    else:
        hanoiSolver(start, mid, end, discs-1)
        print(f"Move disc from {start} to {end}")
        hanoiSolver(mid, end, start, discs-1)

hanoiSolver("A", "C", "B", 3)
