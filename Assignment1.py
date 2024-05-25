
#Lower Triangular Pattern

def lower_triangular(n):
    for i in range(n):
        for j in range(i + 1):
            print('*', end='')
        print()  # Move to the next line

n = 5 
lower_triangular(n) 

#Upper Triangular Pattern
def upper_triangular(n):
    for i in range(n):
        for j in range(n - i):
            print('*', end='')
        print()  # Move to the next line

n = 5 
upper_triangular(n)

#Pyramid Pattern
def pyramid(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(' ', end='')  
        for k in range(2 * i + 1):
            print('*', end='')  
        print()  # Move to the next line

n = 5  
pyramid(n)

