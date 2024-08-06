from math import sqrt

while True:
    # Inputting number
    n = input("Input number: ")
    # Checking if number is above 0 and is a digit
    if not(n.isdigit()) or (n == '0'):
        print("Please enter an integer.")
        continue        
    elif n == '1':
        print("1 is not prime")
    else:
        n = int(n)            
        prime = True
        # Looping every number until the square root of the entered number 
        # (Since every factor of a number is lesser than or qual to the square root)
        for i in range(2, int(sqrt(n)+1)):
            # Checking if the looped number divides the entered number without remainders
            if n % i == 0:
                prime = False
                break
            else:
                continue
        # Outputting whether entered number is prime or not
        if prime:
            print(f"{n} is prime.")
        else:
            print(f"{n} is not prime.")
    print()
